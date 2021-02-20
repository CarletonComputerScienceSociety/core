from django.db import models
from django.contrib.auth.models import User

class JobPosting(models.Model):
    title = models.CharField(max_length=150) # represents the job title from the desired posting
    url = models.CharField(max_length=300) # represents the url of the desired posting
    company = models.CharField(max_length=50) # represents the company associated with the desired posting
    found_date = models.DateField() # represents the date the job posting was found or suggested by a volunteer or student
    country = models.CharField(max_length=100) # represents the country of the desired posting
    status = models.CharField(choices=( #represents the current state of the posting
            ('s', "suggested"), # represents a posting that may have been submitted by a student and therefore needs to be approved by a volunteer
            ('p', "public"), # represents a posting that can be publicly viewed
            ('e', "expired"), # represents a posting that a volunteer has confirmed to be expired
        ),
        max_length=1
    )

class ResourcePage(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField(null=True, blank=True)

    def public_sections(self):
        return self.resource_page_sections.filter(status='p').order_by('order')
        

    def __str__(self): 
        return self.title 

class ResourcePageSection(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    order = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    status = models.CharField(choices=(
            ('p', "public"),
            ('h', "hidden"),
        ),
        max_length=1
    )
    resource_page = models.ForeignKey(ResourcePage, related_name='resource_page_sections', on_delete=models.CASCADE, blank=True, null=True)

    def public_resources(self):
        return self.resources.filter(status='p').order_by('order')

    def __str__(self): 
        return self.title 

class Resource(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    found_date = models.DateField()
    organization = models.CharField(max_length=50, null=True, blank=True)
    order = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    status = models.CharField(choices=(
            ('s', "suggested"),
            ('p', "public"),
            ('e', "expired"),
        ),
        max_length=1
    )
    resource_page_section = models.ForeignKey(ResourcePageSection, related_name='resources', on_delete=models.CASCADE, blank=True, null=True)

