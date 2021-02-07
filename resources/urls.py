from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

#router = routers.DefaultRouter()
#router.register('jobpostings', views.JobPostingList)
#router.register('jobpostings/<int:id>', views.JobPostingDetail)

urlpatterns = [
    #url(r'^jobposting/', views.JobPostingList.as_view()),
    #url(r'^jobpostings/(?P<pk>[0-9]+)/$', views.JobPostingDetail.as_view()),
    path('jobpostings/', views.JobPostingList),
    path('jobpostings/<int:pk>/', views.JobPostingDetails),
    path('resources/', views.ResourceList),
    path('resources/<int:pk>/', views.ResourceDetails),
    #path('', include(router.urls)),
]