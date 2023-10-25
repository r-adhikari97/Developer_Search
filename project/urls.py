from django.urls import path
from . import views

urlpatterns = [
    path("", views.Product),
    path('Product/<str:pk>',views.Products)
]