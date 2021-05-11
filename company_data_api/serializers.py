from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields = ['company_name', 'job_title', 'job_location', 'job_type', 'job_link']
