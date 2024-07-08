from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.products),
    path('products/<int:id>/', views.single_product),
    path('category/<int:pk>',views.category_detail, name='category-detail'),  # API 42
]
