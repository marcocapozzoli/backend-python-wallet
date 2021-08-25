from django.urls import path

from cashback import views

urlpatterns = [
    path('', views.api_root, name='api-root'),
]
