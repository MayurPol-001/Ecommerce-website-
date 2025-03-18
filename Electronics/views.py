from django.shortcuts import render
from .models import Product

# Create your views here.


def Home(request):
    return render(request,'Electronics/Home.html')


def Product_details(request):
    prod = Product.objects.all()
    return render(request,'Electronics/Product_details.html',{'prod':prod})