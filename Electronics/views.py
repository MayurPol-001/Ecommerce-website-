from django.shortcuts import render,redirect,get_object_or_404
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
            form = ProductForm()
    return render(request,'Electronics/Product_details.html',{'prod':prod,'form':form})



def update_product(request, id):
    prod = get_object_or_404(Product, id=id)                    #get the product or return 404

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=prod)         #bind the form to product instance
        if form.is_valid():
            form.save()                                          #save the updates product
            return redirect('Product_details')                    #Redirect to the product list after saving
    else:         
        form = ProductForm(instance=prod)                        #populate the form with exsiting product data
           
    return render(request,'Electronics/Update_product.html',{'prod':prod,'form':form})


def delete_product(request, id):
    prod = get_object_or_404(Product, id=id)                        #Safe way to get product or return a 404 error
    prod.delete()            
    return redirect('Product_details')                               #Redirect back to product details page after deletion