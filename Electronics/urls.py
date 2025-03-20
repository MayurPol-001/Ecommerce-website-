from django.urls import path
from Electronics import views

urlpatterns = [
    path('Product/', views.Product_details, name='Product_details'),
    path('update/<int:id>', views.update_product, name= 'update_product'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
]
