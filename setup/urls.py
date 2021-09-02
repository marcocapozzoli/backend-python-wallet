from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views as view_auth
from users.views import CustomLoginView, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cashback.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token/', view_auth.obtain_auth_token, name='token'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
