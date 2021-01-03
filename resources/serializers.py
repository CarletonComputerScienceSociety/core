from rest_framework import serializers
from resources.models import JobPosting

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ("title", "url", "company", "found_date", "country")

class JobPostingCreateSerializer(serializers.ModelSerializer): # should only be used for the case where we need to create a posting
    class Meta:
        model = JobPosting
        fields = ("title", "url", "company", "found_date", "country", "status")