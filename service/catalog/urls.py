from rest_framework import routers
from django.urls import path, include

from . import views
from .views import (machine_create, machine_list,
                    maintenance_create, claims_create)

router = routers.DefaultRouter()
router.register(r'machine', views.MachineViewSet,
                basename='api_machine_model')

router.register(r'claims', views.ClaimsViewSet, basename='api_claims')


urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('', machine_list, name='machines'),
    path('machine_create/', machine_create, name='machine_create'),
    path('maintenance_create/', maintenance_create, name='maintenance_create'),
    path('claims_create/', claims_create, name='claims_create'),
]

