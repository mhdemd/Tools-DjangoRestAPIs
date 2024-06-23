from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # A jazzy skin for the Django admin interface 
    path('admin/', admin.site.urls),
]
