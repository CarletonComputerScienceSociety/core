from django.contrib import admin

from .models import Poll, MultipleChoiceOption, MultipleChoiceQuestion

# Register your models here.
@admin.register(Poll)
class CustomerPoll(admin.ModelAdmin):
    list_display = ("title", "description")


@admin.register(MultipleChoiceQuestion)
class CustomerMultipleChoiceQuestion(admin.ModelAdmin):
    list_display = ["body"]


@admin.register(MultipleChoiceOption)
class CustomerMultipleChoiceOption(admin.ModelAdmin):
    list_display = ["body"]
