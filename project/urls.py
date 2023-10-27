from django.urls import path
from . import views

urlpatterns = [
    path("", views.Product, name = "Product"),
    path('Product/<str:pk>',views.Products, name="Products"),
    path('create-project/',views.createProject, name="create-project"),
    path('update-project/<str:pk>',views.updateProject,name='update-project'),
    path('delete-project/<str:pk>',views.deleteProject,name='delete-project')
]