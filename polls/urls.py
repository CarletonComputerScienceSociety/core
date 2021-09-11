from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

urlpatterns = [
    path("", views.PollList.as_view(), name="poll-list"),
    path("<int:pk>/", views.PollDetails.as_view(), name="poll-view"),
]
