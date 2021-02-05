from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from django.utils import timezone

# Create your models here.
CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)
# All information relevant to job post. The recruiter variable links it to the recruiter posting,
# All details about the job including title, location, company, description, skills required, and type of job.
class Job(models.Model):
    recruiter = models.ForeignKey(
        User, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    description = models.TextField()
    skills_req = models.CharField(max_length=200)
    job_type = models.CharField(max_length=30, choices=CHOICES, default='Full Time', null=True)
    link = models.URLField(null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# All data related to candidates who have applied to a post. Has a job variable linking to the relevant job,
# an applicant variable linking it to the candidate and a date when the candidate applied.
class Applicants(models.Model):
    job = models.ForeignKey(Job, related_name='applicants', on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant

# All data related to the candidates who have been selected for a job post. Has a job variable linking it to the relevant job.
# Has an applicant variable which links it to the candidate who was selected and when.
class Selected(models.Model):
    job = models.ForeignKey(Job, related_name='select_job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, related_name='select_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant
