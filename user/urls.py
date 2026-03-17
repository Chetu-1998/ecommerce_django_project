from django.urls import include, path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    # path('api/users/', views.user_list, name='user_list'),
    path('api/users/register/', views.register_user, name='register_user'),
    path('api/users/login/', views.login_user, name='login_user'),
    path('api/users/logout/', views.user_logout, name='user_logout'),
]