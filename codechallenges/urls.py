from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

urlpatterns = [
    path("expired/questions/", views.ExpiredQuestionList.as_view(), name="expired-question-list"),
    path("current/questions/", views.CurrentQuestionList.as_view(), name="current-question-list"),
    path("questions/", views.QuestionList.as_view(), name="released-question-list"),
    path("submissions/", views.SubmissionList.as_view(), name="submission-view"),
    path("questions/<int:pk>/", views.QuestionDetails.as_view(), name="question-view"),
]
