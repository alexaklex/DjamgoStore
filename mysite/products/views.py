from django.shortcuts import render
from .models import *

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'products/product_detail.html', locals())
