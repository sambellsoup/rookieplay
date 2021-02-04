from django import forms
from .models import Profile, Skill

# Allows user to update candidate profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'country', 'location', 'resume', 'grad_year', 'looking_for']

# Allows user to add a new skill to the skills model class for a user
class NewSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill']
