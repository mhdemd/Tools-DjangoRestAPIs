from django.urls import path
from myapp.views import (
    ShopCreateAPIView,
    ShopRetrieveAPIView,
    ShopDestroyAPIView,
    ShopUpdateAPIView,
    ShopListCreateAPIView,
    ShopRetrieveUpdateAPIView,
    ShopRetrieveDestroyAPIView,
    ShopRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('products/', ShopListCreateAPIView.as_view(), name='product-list-create'),  # GET, POST
    path('products/<int:pk>/', ShopRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),  # GET, PUT, PATCH, DELETE

    # Individual operations
    path('products/create/', ShopCreateAPIView.as_view(), name='product-create'),  # POST
    path('products/<int:pk>/retrieve/', ShopRetrieveAPIView.as_view(), name='product-retrieve'),  # GET
    path('products/<int:pk>/destroy/', ShopDestroyAPIView.as_view(), name='product-destroy'),  # DELETE
    path('products/<int:pk>/update/', ShopUpdateAPIView.as_view(), name='product-update'),  # PUT, PATCH

    # Combined operations
    path('products/<int:pk>/retrieve-update/', ShopRetrieveUpdateAPIView.as_view(), name='product-retrieve-update'),  # GET, PUT, PATCH
    path('products/<int:pk>/retrieve-destroy/', ShopRetrieveDestroyAPIView.as_view(), name='product-retrieve-destroy'),  # GET, DELETE
]
