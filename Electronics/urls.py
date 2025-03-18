from django.urls import path
from Electronics import views

urlpatterns = [
    path('Product/', views.Product_details, name='Product_details')
]
