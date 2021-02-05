from django import forms
from .models import Job

# Allows recruiter to post a new job
class NewJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'description', 'skills_req', 'job_type', 'link']
        help_texts = {
            'skills_req': 'Enter all the skills required for the position each separated with a comma.',
            'link': 'Provide a link where applicants can apply on your company\'s website.'
        }

# Akkiws recruiter to update an existing job post.
class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'description', 'skills_req', 'job_type', 'link']
        help_texts = {
            'skills_req': 'Enter all the skills required for the position each separated with a comman.',
            'link': 'Provide a link where applicants can apply on your company\'s website.'
        }
