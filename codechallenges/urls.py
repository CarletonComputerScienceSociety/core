from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

urlpatterns = [
    path("expired/questions/", views.ExpiredQuestionList),
    path("current/questions/", views.CurrentQuestionList),
    path("questions/", views.QuestionList),
    path("submissions/", views.SubmissionList),
    path("questions/<int:pk>/", views.QuestionDetails),
]
