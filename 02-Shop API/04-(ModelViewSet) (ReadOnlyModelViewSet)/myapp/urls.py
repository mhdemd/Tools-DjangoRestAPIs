## Using Routers
from rest_framework.routers import DefaultRouter
from .views import Shop

router = DefaultRouter()
router.register(r'products', Shop, basename='product')

urlpatterns = router.urls
