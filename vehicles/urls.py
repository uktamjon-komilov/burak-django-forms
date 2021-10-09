from django.urls import path

from . import views


urlpatterns = [
    path("", views.fetch_dvla, name="fetch_dvla"),
    path("sub/", views.sub_category, name="sub"),
    path("mini/", views.mini_category, name="mini"),
    path("vec/", views.vec, name="vec"),
]