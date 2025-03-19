from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.


def Home(request):
    return render(request,'Electronics/Home.html')


def Product_details(request):
    prod = Product.objects.all()          #Creating Objects
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'Electronics/Product_details.html',{'prod':prod,'form':form})