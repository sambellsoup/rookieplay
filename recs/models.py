from __future__ import unicode_literals
from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date


# Create your models here.

class Companies(models.Model):
    company_id = models.BigIntegerField(primary_key=True)
    slug = models.SlugField()
    rank = models.IntegerField()
    name = models.CharField(max_length = 200)
    revenue = models.IntegerField()
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    underscored_name = models.CharField(max_length = 200)
    description = models.TextField()
    urls = models.URLField()
    adjectives = models.CharField(max_length = 200)
    logo = models.URLField()
    image = models.URLField()

    def __str__(Self):
        return self.text

    class Meta:
        verbose_name_plural = 'companies'


class Jobs(models.Model):
    job_id = models.BigIntegerField(primary_key=True)
    slug = models.SlugField()
    company_name = models.CharField(max_length = 200)
    job_title = models.CharField(max_length = 200)
    job_type = models.CharField(max_length = 200)
    job_location = models.CharField(max_length = 200)
    job_link = models.URLField()
    job_description = models.TextField()
    company_id = models.ForeignKey('Companies', on_delete=models.CASCADE)
    pub_date = models.DateField()

    def __str__(self):
        return "{} on {}".format(
        self.job_title,
        self.pub_date.strftime('%Y-%m-%d'))

    class Meta:
        verbose_name = 'job posting'
        verbose_name_plural = 'jobs'
        ordering = ['-pub_date']




class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Document(models.Model):
    """Document uploaded by user to be analyzed"""
    id = models.BigIntegerField(primary_key = True)
    document = models.FileField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.document

class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text[:50]

class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

class Teacher(models.Model):

    name = models.CharField(max_length=80)

    age = models.IntegerField()
