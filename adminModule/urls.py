from django.urls import include, path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('', views.admin_list, name='admin_list'),
]