from django.contrib import admin
from django.urls import path, include
from djoser import urls

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # A jazzy skin for the Django admin interface 
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
