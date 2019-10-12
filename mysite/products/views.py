from django.shortcuts import render

def product_detail(request, slug):
    print(request, slug)
