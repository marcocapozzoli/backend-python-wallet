from django.urls import path,include

from rest_framework.routers import DefaultRouter

from cashback import views


router = DefaultRouter()
router.register('buy', views.BuyViewSet, basename='buy')
router.register('product', views.ProductViewSet, basename='product')
router.register('customer', views.CustomerViewSet, basename='customer')

urlpatterns = [
    path('', include(router.urls)),
]