from django.urls import path, include
from rest_framework import routers
from producto import views


router = routers.DefaultRouter()
router.register(r'producto', views.ProductoViewSet)
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'productoCategoria', views.ProductoCategoriaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]