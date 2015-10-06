"""
Relative URLs for the teacher feedback API.
"""
from django.conf.urls import url
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'user', views.UsersAPI)

urlpatterns = [
    url(r'^', include(router.urls)),
]

