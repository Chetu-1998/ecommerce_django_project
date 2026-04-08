from django.urls import include, path

from . import views

urlpatterns = [
    path("dashboardstats/", views.dashboard_stats, name="dashboard-stats"),
]
