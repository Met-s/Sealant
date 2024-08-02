from rest_framework import routers
from django.urls import path, include
from . import views
# from .views import catalog import views
# from .views import
from .views import *


router = routers.DefaultRouter()
router.register(r'machine', views.MachineViewSet,
                basename='api_machine_model')

urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('main/', mainPage, name='mainPage'),

]

