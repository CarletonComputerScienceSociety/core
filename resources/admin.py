from django.contrib import admin

from .models import JobPosting, Resource, ResourcePage, ResourcePageSection

admin.site.site_header = "Carleton Computer Science Society"

# @admin.register(JobPosting)
# class CustomerJobPosting(admin.ModelAdmin):
#    list_display = ("title", "company", "found_date", "country", "status")


@admin.register(Resource)
class CustomerResource(admin.ModelAdmin):
    list_display = ("title", "found_date", "status", "order", "resource_page_section")
    list_filter = ("resource_page_section", "status")


@admin.register(ResourcePage)
class CustomerResourcePage(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(ResourcePageSection)
class CustomerResourceSection(admin.ModelAdmin):
    list_display = ("title", "resource_page", "order", "status")
    list_filter = ("resource_page", "status")
