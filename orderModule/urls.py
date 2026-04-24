from django.urls import include, path

from . import views

urlpatterns = [
    path("dashboardstats/", views.dashboard_stats, name="dashboard-stats"),
    path("placeorder/", views.placeOrder, name="place-order"),
    path("vieworders/", views.viewOrders, name="view-orders")
]
