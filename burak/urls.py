from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path("fetch_dvla/", include("vehicles.urls")),
    path("", admin.site.urls),
]
