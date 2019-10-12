from django.urls import path, include
from django.contrib import admin
from products import views


urlpatterns = [
    path('<slug:slug>/', views.product_detail, name='detail_product'),
]
