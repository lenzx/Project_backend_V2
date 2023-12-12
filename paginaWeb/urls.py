from django.urls import path, include
from rest_framework import routers
from paginaWeb import views

router = routers.DefaultRouter()
router.register(r'markay', views.MarkayViewSet)
router.register(r'seccion', views.SeccionViewSet)
router.register(r'redSocial', views.RedSocialViewSet)


urlpatterns = [
    path('', include(router.urls)),
]