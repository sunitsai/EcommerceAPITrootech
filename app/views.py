from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizers


class DetailsCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizers


class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizers


class DetailsProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizers


class ListCart(generics.ListCreateAPIView):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer    


def ShowAllCategory(request):
    all_cat = Category.objects.all()
    return render(request,"app/ListCategory.html",{'key1':all_cat})


def ShowAllProduct(request):
    all_pro = Product.objects.all()
    return render(request,"app/ListProduct.html",{'key2':all_pro})


def EditCategory(request,pk):
    edata = Category.objects.get(id=pk)
    return render(request,"app/EditCat.html",{'key3':edata})

def EditProduct(request,pk):
    edata = Product.objects.get(id=pk)
    return render(request,"app/EditProduct.html",{'key4':edata})