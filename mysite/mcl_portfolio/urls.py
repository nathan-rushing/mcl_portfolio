from django.urls import path

from . import views

app_name = "mcl_portfolio"

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("achievements/", views.achievements, name="achievements"),
    path("report/", views.report, name="report"),
    ]