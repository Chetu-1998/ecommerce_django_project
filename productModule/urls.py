from django.urls import include, path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('', views.product_list, name='product_list'),
]