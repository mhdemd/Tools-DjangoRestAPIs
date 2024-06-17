from django.urls import path
from .views import secret, manager_view, throttle_check, throttle_check_auth
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('secret/', secret, name='secret'),
    path('api-token-auth/', obtain_auth_token),
    path('manager-view/', manager_view),
    path('throttle-check/', throttle_check),
    path('throttle-check-auth/', throttle_check_auth),
]
