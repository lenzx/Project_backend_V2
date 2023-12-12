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
router.register(r'especialidadServicio', views.EspecialidadServicioViewSet)
router.register(r'especialistaConvenio', views.EspecialistaConvenioViewSet)
router.register(r'especialistaEspecialidad', views.EspecialistaEspecialidadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]