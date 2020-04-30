# Generated by Django 2.2.8 on 2020-04-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20200407_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpcs_user',
            name='matchDist',
            field=models.CharField(choices=[('2', '2 arcsec'), ('1', '1 arcsec'), ('6', '6 arcsec'), ('4', '4 arcsec')], default='1 arcsec', max_length=10, verbose_name='Matching radius'),
        ),
    ]