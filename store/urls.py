from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('category',views.category_list),
    path('store/category/json', views.category_list),
    path('product',views.product_list)
]
