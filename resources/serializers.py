from rest_framework import serializers
from resources.models import JobPosting, Resource, ResourcePage, ResourcePageSection


class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ("title", "url", "company", "found_date", "country")


class JobPostingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ("title", "url", "company", "found_date", "country", "status")


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ("title", "description", "url", "found_date")


class ResourcePageSectionSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True, required=False, source="public_resources")

    class Meta:
        model = ResourcePageSection
        fields = ("title", "description", "url", "resources")


class ResourcePageSerializer(serializers.ModelSerializer):
    resource_page_sections = ResourcePageSectionSerializer(
        many=True, required=False, source="public_sections"
    )

    class Meta:
        model = ResourcePage
        fields = ("title", "description", "resource_page_sections")
