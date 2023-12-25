from django.urls import path, include
from rest_framework import routers
from servicio import views

router = routers.DefaultRouter()
router.register(r'convenios', views.ConvenioViewSet)
router.register(r'especialista', views.EspecialistaViewSet)
router.register(r'especialidad', views.EspecialidadViewSet)
router.register(r'servicio', views.ServicioViewSet)
router.register(r'consulta', views.ConsultaViewSet)
router.register(r'categoriaConvenio', views.CategoriaConvenioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]