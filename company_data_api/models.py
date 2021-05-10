from django.db import models

# Create your models here.
class Jobs(models.Model):
    company_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    job_location = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50)
    job_link = models.CharField(max_length=50)
    job_description = models.TextField()
    date_scraped = models.DateTimeField(auto_now_add=True)

class Companies(models.Model):
    company_name = models.CharField(max_length=50)
    company_city = models.CharField(max_length=60)
    company_state = models.CharField(max_length=15)
    company_description = models.TextField()
    company_url = models.CharField(max_length=50)
