from django.urls import include, path
from . import views

urlpatterns = [
    path('addproduct/', views.addProduct, name='addProduct'),
    path('products/', views.viewProducts, name='viewProducts'),
    path('updateproduct/<int:id>/', views.updateProduct, name='updateProduct'),
    path('deleteproduct/<int:id>/', views.deleteProduct, name='deleteProduct'),
    path('viewproduct/<int:id>/', views.viewProduct, name='viewProduct'),
    path('addcategory/', views.addCategory, name='addCategory'),
    path('viewcategories/', views.viewCategories, name='viewCategory'),
    path('deletecategory/<int:id>/', views.deleteCategory, name='deleteCategory'),
    path('updatecategory/<int:id>/', views.updateCategory, name='updateCategory'),
    path('viewcategory/<int:id>/', views.viewCategory, name='viewCategory'),
]
