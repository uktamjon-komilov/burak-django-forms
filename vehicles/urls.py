from django.urls import path

from . import views


urlpatterns = [
    path("", views.fetch_dvla, name="fetch_dvla")
]