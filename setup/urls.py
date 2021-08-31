from django.urls import path, include
from rest_framework.authtoken import views as view_auth

from users.views import SignUpView


urlpatterns = [
    path('api/', include('cashback.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token/', view_auth.obtain_auth_token, name='api-token-auth'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
