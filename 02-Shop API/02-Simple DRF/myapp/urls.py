from django.urls import path
from . import views

## Regular routes
# urlpatterns = [
#     path('products/', views.products),    
# ]

## Routing to a class method
# urlpatterns = [
# 	path('products/', views.Shop.products)
# ]

## Routing class-based views
# urlpatterns = [
#     path('products/<int:pk>',views.Shop.as_view())
# ]

## Routing classes that extend viewsets
# urlpatterns = [
# 	path('products', views.Shop.as_view(
#         {
#         	'get': 'list',
#         	'post': 'create',
#         })
# 	),
#     path('products/<int:pk>',views.Shop.as_view(
#         {
#         	'get': 'retrieve',
#         	'put': 'update',
#         	'patch': 'partial_update',
#         	'delete': 'destroy',
#         })
# 	)
# ]
