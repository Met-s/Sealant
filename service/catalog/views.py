
import django_filters.rest_framework
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework import permissions

from .models import Role, Clients, Managers, MachineModel, EngineModel, \
    TransmissionModel, DriveAxleModel, SteerableAxleModel, ServiceCompany, \
    Machine, MaintenanceType, OrganMaintenance, Maintenance, FailureNode, \
    RepairMethod, Claims
from .serializers import UserSerializer, RoleSerializer, ClientsSerializer, \
    ManagersSerializer, MachineModelSerializer, EngineModelSerializer, \
    TransmissionModelSerializer, DriveAxleModelSerializer, \
    SteerableAxleModelSerializer, ServiceCompanySerializer, MachineSerializer, \
    MaintenanceTypeSerializer, OrganMaintenanceSerializer, \
    MaintenanceSerializer, FailureNodeSerializer, RepairMethodSerializer, \
    ClaimsSerializer
from django.contrib.auth.models import User
from .forms import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['id', 'username', 'first_name', 'last_name',
                        'email', 'is_superuser', 'is_active']


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name']


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', 'role']


class ManagersViewSet(viewsets.ModelViewSet):
    queryset = Managers.objects.all()
    serializer_class = ManagersSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', 'role']


class MachineModelViewSet(viewsets.ModelViewSet):
    queryset = MachineModel.objects.all()
    serializer_class = MachineModelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']


class EngineModelViewSet(viewsets.ModelViewSet):
    queryset = EngineModel.objects.all()
    serializer_class = EngineModelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']


class TransmissionModelViewSet(viewsets.ModelViewSet):
    queryset = TransmissionModel.objects.all()
    serializer_class = TransmissionModelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']


class DriveAxleModelViewSet(viewsets.ModelViewSet):
    queryset = DriveAxleModel.objects.all()
    serializer_class = DriveAxleModelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']


class SteerableAxleModelViewSet(viewsets.ModelViewSet):
    queryset = SteerableAxleModel.objects.all()
    serializer_class = SteerableAxleModelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']


class ServiceCompanyModelViewSet(viewsets.ModelViewSet):
    queryset = ServiceCompany.objects.all()
    serializer_class = ServiceCompanySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', 'role']


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'machineSerialNumber', 'machineModel',
                        'engineModel','engineNumber', 'transmissionModel',
                        'transmissionNumber', 'driveAxleModel',
                        'driveAxleNumber', 'steerableAxleNumber',
                        'deliveryContractNumber', 'shipmentDate',
                        'consignee', 'deliveryAddress', ' equipment',
                        'client', 'serviceCompany']


class MaintenanceTypeViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceType.objects.all()
    serializer_class = MaintenanceTypeSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']


class OrganMaintenanceViewSet(viewsets.ModelViewSet):
    queryset = OrganMaintenance.objects.all()
    serializer_class = OrganMaintenanceSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']


class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'maintenanceType', 'maintenanceDate',
                        'motorResource', 'workOrderNumber', 'workOrderDate',
                        'organMaintenance', 'machine', 'serviceCompany']


class FailureNodeViewSet(viewsets.ModelViewSet):
    queryset = FailureNode.objects.all()
    serializer_class = FailureNodeSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']


class RepairMethodViewSet(viewsets.ModelViewSet):
    queryset = RepairMethod.objects.all()
    serializer_class = RepairMethodSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']


class ClaimsViewSet(viewsets.ModelViewSet):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'failureDate', 'operatingTime',
                        'failureNode', 'failureDescription', 'repairMethod',
                        'usedSpareParts', 'repairDate',
                        'equipmentDowntime', 'machine', 'serviceCompany']


def indexPage(request):
    return render(request, 'catalog/flatpages/default.html')


def claim_edit(request, pk):
    try:
        claim = Claims.objects.get(id=pk)
    except Claims.DoesNotExist:
        return redirect('html_404')

    if request.method == 'POST':
        form = ClaimsForm(request.POST, instance=claim)
        if form.is_valid():
            form.save()
            return redirect('mainPage')
    else:
        form = ClaimsForm(instance=claim)

    return render(request, 'App/claim_create.html', {'form': form})