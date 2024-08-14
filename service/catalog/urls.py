from rest_framework import routers
from django.urls import path, include

from . import views
from .views import MachineList



router = routers.DefaultRouter()
router.register(r'machine', views.MachineViewSet,
                basename='api_machine_model')

urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('', MachineList.as_view(), name='machines'),
]

