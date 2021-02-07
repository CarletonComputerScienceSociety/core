from rest_framework import serializers
from resources.models import JobPosting, Resource

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ("title", "url", "company", "found_date", "country")

class JobPostingCreateSerializer(serializers.ModelSerializer): # should only be used for the case where we need to create a posting
    class Meta:
        model = JobPosting
        fields = ("title", "url", "company", "found_date", "country", "status")

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ("title", "description", "category", "resource_type", "url", "found_date")
