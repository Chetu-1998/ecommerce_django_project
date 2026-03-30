from django.urls import include, path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('viewusers/', views.viewUsers, name='viewUsers')
]