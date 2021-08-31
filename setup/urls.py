from django.urls import path, include
from rest_framework.authtoken import views as view_auth


urlpatterns = [
    path('api/', include('cashback.urls')),
    path('api-token/', view_auth.obtain_auth_token, name='api-token-auth'),
]
