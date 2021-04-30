from django.contrib import admin

# Register your models here.
from .models import Question, Submission, Event


@admin.register(Question)
class CustomerQuestion(admin.ModelAdmin):
    list_display = ("title", "body", "answer", "release_date", "expiration_date")


@admin.register(Submission)
class CustomerSubmission(admin.ModelAdmin):
    list_display = ("email", "correct")


@admin.register(Event)
class CustomerEvent(admin.ModelAdmin):
    list_display = ("title", "description")
