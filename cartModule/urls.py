from django.urls import include, path

from . import views

urlpatterns = [
    path('addtocart/', views.addToCart, name='add_to_Cart'),
    path('viewcarts/', views.viewCarts, name='view_carts'),
    path('removecart/<int:id>/', views.removeCart, name='remove_cart'),
    path('updatecart/<int:id>/', views.updateCart, name='update_cart')
]