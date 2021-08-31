from django.urls import path,include

from rest_framework.routers import DefaultRouter

from cashback import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="BackEnd Cashback MaisTodos",
      default_version='v1',
      description="API desenvolvida para o desafio backenda da maisTodos. O objetivo dessa API é fazer todo o gerenciamento de valores enviados por clientes varegistas e repassar esses valores para uma outra API de cashback da maisTodos gerar de fato o cashback para o cliente.",
      terms_of_service="#",
      contact=openapi.Contact(email="marcocapozzoli90@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()
router.register('buy', views.BuyViewSet, basename='buy')
# router.register('product', views.ProductViewSet, basename='product')
# router.register('customer', views.CustomerViewSet, basename='customer')

urlpatterns = [
    path('', include(router.urls)),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]