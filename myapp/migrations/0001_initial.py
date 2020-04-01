# Generated by Django 2.2.8 on 2020-03-30 17:50

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BHEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='The name of the target, e.g. Gaia17bts or ASASSN-16oe', max_length=100, verbose_name='Name')),
                ('gaia_alert_name', models.CharField(default='', help_text='Name in Gaia Alerts, if available', max_length=100, verbose_name='Gaia Alert')),
                ('ztf_alert_name', models.CharField(default='', help_text='Name in ZTF Alerts, if available', max_length=100, verbose_name='ZTF Alert')),
                ('calib_server_name', models.CharField(default='', help_text='Name in the Calibration Server, if available', max_length=100, verbose_name='Calib.Server name')),
                ('ra', models.FloatField(help_text='Right Ascension, in degrees.', verbose_name='Right Ascension')),
                ('dec', models.FloatField(help_text='Declination, in degrees.', verbose_name='Declination')),
                ('classification', models.CharField(blank=True, default='', help_text='The classification of this target, e.g. Ulens, Be, FUORI', max_length=100, null=True, verbose_name='Target classification')),
                ('all_phot', models.TextField(blank=True, help_text='All photometry', null=True, verbose_name='All photometry')),
            ],
            options={
                'ordering': ('-id',),
                'get_latest_by': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Catalogs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(editable=False)),
                ('filters', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Cpcs_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obsName', models.CharField(max_length=255, verbose_name='Observatory name')),
                ('cpcs_hashtag', models.CharField(max_length=255)),
                ('lon', models.FloatField(verbose_name='Longitude')),
                ('lat', models.FloatField(verbose_name='Latitude')),
                ('prefix', models.CharField(blank=True, max_length=255, null=True)),
                ('user_activation', models.BooleanField()),
                ('matchDist', models.CharField(choices=[('2 arcsec', '2 arcsec'), ('4 arcsec', '4 arcsec'), ('1 arcsec', '1 arcsec'), ('6 arcsec', '6 arcsec')], default='1 arcsec', max_length=10, verbose_name='Matching radius')),
                ('allow_upload', models.BooleanField(verbose_name='Dry Run (no data will be stored in the database)')),
                ('fits', models.FileField(blank=True, null=True, upload_to='user_fits', verbose_name='Sample fits')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BHTomFits',
            fields=[
                ('fits_id', models.CharField(db_index=True, max_length=50, primary_key=True, serialize=False)),
                ('dataproduct_id', models.IntegerField()),
                ('status', models.CharField(choices=[('C', 'Created'), ('S', 'Send_to_ccdphotd'), ('I', 'In_progress'), ('R', 'Result_from_ccdphotd'), ('F', 'Finished'), ('E', 'Error'), ('U', 'User not active')], default='C', max_length=1)),
                ('status_message', models.TextField(blank=True, default='Fits upload', editable=False)),
                ('mjd', models.FloatField(blank=True, null=True)),
                ('expTime', models.FloatField(blank=True, null=True)),
                ('ccdphot_result', models.FileField(blank=True, editable=False, null=True, upload_to='photometry')),
                ('cpcs_time', models.DateTimeField(blank=True, editable=False, null=True)),
                ('filter', models.CharField(blank=True, max_length=255, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Cpcs_user')),
            ],
        ),
    ]
