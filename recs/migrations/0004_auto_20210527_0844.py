# Generated by Django 3.1.1 on 2021-05-27 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recs', '0003_auto_20210527_0843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobs',
            options={'ordering': ['-pub_date'], 'verbose_name': 'job posting', 'verbose_name_plural': 'jobs'},
        ),
    ]