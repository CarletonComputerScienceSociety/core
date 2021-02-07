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

class Resource(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=150)
    resource_type = models.CharField(choices=(
            ('study', "study"),
            ('award', "award"),
            ('event', "event"),
        ),
        max_length=5
    )
    url = models.CharField(max_length=300)
    found_date = models.DateField()
    status = models.CharField(choices=(
            ('s', "suggested"),
            ('p', "public"),
            ('e', "expired"),
        ),
        max_length=1
    )
