"""
Relative URLs for the teacher feedback API.
"""
from django.conf.urls import url, include
from teacherfeedback import views

urlpatterns = [
    url(r'^user$', views.manage_users),
]

