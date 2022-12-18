from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Products
from .form import ProductsForm

def index(request):
    
    return render (request, 'index.html',{
        'products' : Products.objects.all()
    })


def create (request):
    return render (request , 'form.html',{
        'form' : ProductsForm
    })
    
    
def store (request):
    form = ProductsForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect(index)

def show (request , id:int):
    return render (request, 'show.html',{
        'products' : Products.objects.get(id = id)
    })
# Create your views here.


def edit (request, id:int):
    products = Products.objects.get(id = id)
    return render(request, 'form.html',{
        'form' : ProductsForm(instance=products),
        'products' : products
    })
    
def update(request, id:int):
    
    products = Products.objects.get(id = id)
    form = ProductsForm(request.POST, instance=products)
    
    if form.is_valid():
        form.save()
    return redirect(show,id=id)
    
    
def delete(request, id:int):
    Products.objects.get(id=id).delete()
    return redirect(index)