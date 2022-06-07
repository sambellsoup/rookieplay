# Generated by Django 3.1.1 on 2021-05-24 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('company_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('slug', models.SlugField()),
                ('rank', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('revenue', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('underscored_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('urls', models.URLField()),
                ('adjectives', models.CharField(max_length=200)),
                ('logo', models.URLField()),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('job_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('slug', models.SlugField()),
                ('company_name', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=200)),
                ('job_type', models.CharField(max_length=200)),
                ('job_location', models.CharField(max_length=200)),
                ('job_link', models.URLField()),
                ('job_description', models.TextField()),
                ('pub_date', models.DateField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recs.companies')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recs.topic')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('document', models.FileField(null=True, upload_to='')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]