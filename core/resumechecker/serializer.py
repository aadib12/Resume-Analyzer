# used to parse query set into JSON format
from rest_framework import serializers
from .models import JobDescription, Resume

class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'resume', 'job_description']