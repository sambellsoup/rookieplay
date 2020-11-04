from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

from .models import

from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Document(models.Model):
    """Document uploaded by user to be analyzed"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    created_at = models.DateTimeField(default=date.today)
    title = models.CharField(max_length=100)
    document = models.FileField(null=True)

    def __str__(self):
        return self.title
