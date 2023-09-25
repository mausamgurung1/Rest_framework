from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('category/', views.category_list),  # Use a trailing slash for consistency
    path('product/', views.product_list),
]

