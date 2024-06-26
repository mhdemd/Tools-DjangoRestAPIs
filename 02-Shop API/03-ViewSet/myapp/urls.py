## Manual URL Routing
# from django.urls import path
# from . import views
# urlpatterns = [
# 	path('products/', views.Shop.as_view(
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


## Using Routers
from rest_framework.routers import DefaultRouter
from .views import Shop
router = DefaultRouter()
router.register(r'products', Shop, basename='product')

urlpatterns = router.urls
