"""
Relative URLs for the teacher feedback API.
"""
from django.conf.urls import url, include
from rest_framework import routers
from teacherfeedback import views

router = routers.DefaultRouter()
router.register(r'user', views.UsersAPI, 'users')

urlpatterns = [
    url(r'^', include(router.urls)),
]

