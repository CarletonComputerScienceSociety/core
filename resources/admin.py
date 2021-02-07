from django.contrib import admin

from .models import JobPosting, Resource

# admin.site.site_title = "Carleton Computer Science Society"
# admin.site.index_title = "Carleton Computer Science Society"
admin.site.site_header = "Carleton Computer Science Society"

#admin.site.register(JobPosting)
@admin.register(JobPosting)
class CustomerJobPosting(admin.ModelAdmin):
    list_display = ("title", "company", "found_date", "country", "status")


@admin.register(Resource)
class CustomerResource(admin.ModelAdmin):
    list_display = ("title", "found_date", "status")