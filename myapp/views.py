from django_filters.views import FilterView


from astropy.coordinates import get_moon, get_sun, SkyCoord, AltAz
from astropy import units as u
from astropy.time import Time
from datetime import datetime
from datetime import timedelta
import json
import copy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tom_targets.models import Target, TargetList, TargetExtra
from tom_targets.filters import TargetFilter
from tom_targets.views import TargetCreateView
from tom_targets.forms import TargetExtraFormset, TargetNamesFormset
from tom_targets.templatetags.targets_extras import target_extra_field

from django.db.models import Case, When

from tom_dataproducts.models import ReducedDatum

import numpy as np

def make_magrecent(all_phot, jd_now):
    all_phot = json.loads(all_phot)
    recent_jd = max([all_phot[obs]['jd'] for obs in all_phot])
    recent_phot = [all_phot[obs] for obs in all_phot if
        all_phot[obs]['jd'] == recent_jd][0]
    mag = float(recent_phot['flux'])
    filt = recent_phot['filters']['name']
    diff = jd_now - float(recent_jd)
    mag_recent = '{mag:.2f} ({filt}: {time:.2f})'.format(
        mag = mag,
        filt = filt,
        time = diff)
    return mag_recent

#computes priority based on dt and expected cadence
#if observed within the cadence, then returns just the pure target priority
#if not, then priority increases
def computePriority(dt, priority, cadence):
    ret = 0
    # if (dt<cadence): ret = 1 #ok
    # else:
    #     if (cadence!=0 and dt/cadence>1 and dt/cadence<2): ret = 2
    #     if (cadence!=0 and dt/cadence>2): ret = 3

    #alternative - linear scale
    if (cadence!=0):
        ret = dt/cadence
    return ret*priority


class BlackHoleListView(FilterView):
    paginate_by = 20
    strict = False
    model = Target
    filterset_class = TargetFilter
    permission_required = 'tom_targets.view_target' #or remove if want it freely visible
            
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        jd_now = Time(datetime.utcnow()).jd

        prioritylist = []
        pklist = []

        for target in qs:
            try:
                #if empty
                last = float(target_extra_field(target=target, name='jdlastobs'))
                target.dt = (jd_now - last)
                dt = (jd_now - last)
            except:
                dt = 10
                target.dt = -1.

            try:
                priority = float(target_extra_field(target=target, name='priority'))
                cadence = float(target_extra_field(target=target, name='cadence'))
            except:
                priority = 1
                cadence = 1 

            target.cadencepriority = computePriority(dt, priority, cadence)
            prioritylist.append(target.cadencepriority)
            pklist.append(target.pk)
        
        prioritylist = np.array(prioritylist)
        idxs = list(prioritylist.argsort())
        sorted_pklist = np.array(pklist)[idxs]
    
        clauses = ' '.join(['WHEN tom_targets_target.id=%s THEN %s' % (pk, i) for i, pk in enumerate(sorted_pklist)])
        ordering = '(CASE %s END)' % clauses
        qsnew= qs.extra(
            select={'ordering': ordering}, order_by=('-ordering',))

        return qsnew


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['target_count'] = context['paginator'].count
        context['groupings'] = (TargetList.objects.all()
                                if self.request.user.is_authenticated
                                else TargetList.objects.none())
        context['query_string'] = self.request.META['QUERY_STRING']
    
        jd_now = Time(datetime.utcnow()).jd

        prioritylist = []

        for target in context['object_list']:
            try:
                #if empty
                last = float(target_extra_field(target=target, name='jdlastobs'))
                target.dt = (jd_now - last)
                dt = (jd_now - last)
            except:
                dt = 10
                target.dt = -1.

            try:
                priority = float(target_extra_field(target=target, name='priority'))
                cadence = float(target_extra_field(target=target, name='cadence'))
            except:
                priority = 1
                cadence = 1 

            target.cadencepriority = computePriority(dt, priority, cadence)
            prioritylist.append(target.cadencepriority)

        return context
