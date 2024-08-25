from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from account.models import UserAuth
from .forms import *


from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from rest_framework import permissions
from rest_framework import viewsets

import django_filters.rest_framework
from .serializers import *



# from django.views.generic import ListView



from .models import Role, Clients, Managers, MachineModel, EngineModel, \
    TransmissionModel, DriveAxleModel, SteerableAxleModel, ServiceCompany, \
    Machine, MaintenanceType, OrganMaintenance, Maintenance, FailureNode, \
    RepairMethod, Claims
from .models import *
from .serializers import (UserSerializer, RoleSerializer,
                            ClientsSerializer, \
    ManagersSerializer, MachineModelSerializer, EngineModelSerializer, \
    TransmissionModelSerializer, DriveAxleModelSerializer, \
    SteerableAxleModelSerializer, ServiceCompanySerializer, MachineSerializer, \
    MaintenanceTypeSerializer, OrganMaintenanceSerializer, \
    MaintenanceSerializer, FailureNodeSerializer, RepairMethodSerializer, \
    ClaimsSerializer)
#



# from .serializers import *


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['id', 'username', 'first_name', 'last_name',
                        'email', 'is_superuser', 'is_active']
    permission_classes = [permissions.IsAuthenticated]


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name']
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', 'role']
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class ManagersViewSet(viewsets.ModelViewSet):
    queryset = Managers.objects.all()
    serializer_class = ManagersSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', 'role']
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class MachineModelViewSet(viewsets.ModelViewSet):
    queryset = MachineModel.objects.all()
    serializer_class = MachineModelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class EngineModelViewSet(viewsets.ModelViewSet):
    queryset = EngineModel.objects.all()
    serializer_class = EngineModelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']
    permission_classes = [permissions.IsAdminUser]


class TransmissionModelViewSet(viewsets.ModelViewSet):
    queryset = TransmissionModel.objects.all()
    serializer_class = TransmissionModelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']
    permission_classes = [permissions.DjangoModelPermissions]


class DriveAxleModelViewSet(viewsets.ModelViewSet):
    queryset = DriveAxleModel.objects.all()
    serializer_class = DriveAxleModelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class SteerableAxleModelViewSet(viewsets.ModelViewSet):
    queryset = SteerableAxleModel.objects.all()
    serializer_class = SteerableAxleModelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class ServiceCompanyModelViewSet(viewsets.ModelViewSet):
    queryset = ServiceCompany.objects.all()
    serializer_class = ServiceCompanySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', 'role']
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'machineSerialNumber', 'machineModel',
                        'engineModel', 'engineNumber', 'transmissionModel',
                        'transmissionNumber', 'driveAxleModel',
                        'driveAxleNumber', 'steerableAxleNumber',
                        'deliveryContractNumber', 'shipmentDate',
                        'consignee', 'deliveryAddress', 'equipment',
                        'client', 'serviceCompany']
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class MaintenanceTypeViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceType.objects.all()
    serializer_class = MaintenanceTypeSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class OrganMaintenanceViewSet(viewsets.ModelViewSet):
    queryset = OrganMaintenance.objects.all()
    serializer_class = OrganMaintenanceSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'maintenanceType', 'maintenanceDate',
                        'motorResource', 'workOrderNumber', 'workOrderDate',
                        'organMaintenance', 'machine', 'serviceCompany']
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class FailureNodeViewSet(viewsets.ModelViewSet):
    queryset = FailureNode.objects.all()
    serializer_class = FailureNodeSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class RepairMethodViewSet(viewsets.ModelViewSet):
    queryset = RepairMethod.objects.all()
    serializer_class = RepairMethodSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description']
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class ClaimsViewSet(viewsets.ModelViewSet):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'failureDate', 'operatingTime',
                        'failureNode', 'failureDescription', 'repairMethod',
                        'usedSpareParts', 'repairDate',
                        'equipmentDowntime', 'machine', 'serviceCompany']
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


# class MachineList(ListView):
#     model = Machine
#     template_name = 'catalog/machine_all.html'
#     context_object_name = 'machines'


def machine_list(request):
    user = request.user


    machine_models_name = MachineModel.objects.values_list('name', flat=True).distinct()


    engine_models_name = EngineModel.objects.values_list('name',
                                                         flat=True).distinct()


    transmission_models_name = TransmissionModel.objects.values_list(
        'name', flat=True).distinct()
    steerable_axle_models_name = SteerableAxleModel.objects.values_list(
        'name', flat=True).distinct()

    drive_axle_models_name = DriveAxleModel.objects.values_list('name',
                                                                flat=True).distinct()



    filter_machine_model = request.GET.get('machine_model')
    filter_engine_model = request.GET.get('engine_model')
    filter_transmission_model = request.GET.get('transmission_model')
    filter_steerable_axle_model = request.GET.get('steerable_axle_model')
    filter_drive_axle_model = request.GET.get('drive_axle_model')


    try:
        machine_model_id = MachineModel.objects.get(name=filter_machine_model)

    except:
        machine_model_id = ''

    try:
        engine_model_id = EngineModel.objects.get(name=filter_engine_model)
    except:
        engine_model_id = ''

    try:
        transmission_model_id = TransmissionModel.objects.get(name=filter_transmission_model)

    except:
        transmission_model_id = ''
    try:
        steerable_axle_model_id = SteerableAxleModel.objects.get(name=filter_steerable_axle_model)

    except:
        steerable_axle_model_id = ''

    try:
        drive_axle_model_id = DriveAxleModel.objects.get(name=filter_drive_axle_model)

    except:
        drive_axle_model_id = ''


    try:
        role_id = UserAuth.objects.filter(user_auth__username=user).values('role_auth')[0]['role_auth']

        role = Role.objects.get(id=role_id)
    except:
        role = 'Статус не определён'
    try:
        client_id = UserAuth.objects.filter(user_auth__username=user).values('client_auth')[0]['client_auth']

        client_name = Clients.objects.get(id=client_id)
    except:
        client_name = ''
    try:
        serviceCompany_id = UserAuth.objects.filter(user_auth__username=user).values('serviceCompany_auth')[0]['serviceCompany_auth']


        serviceCompany__name = ServiceCompany.objects.get(id=serviceCompany_id)

    except:
        serviceCompany__name = ''

    managers = False
    client = False
    serviceCompany = False
    role_error = False

    if str(role) == 'Managers':
        managers = True
    if str(role) == 'Client':
        client = True
    if str(role) == 'Service Company':
        serviceCompany = True
    if str(role) == 'Статус не определён':
        role_error = True

    q_filter = Q()
    if filter_machine_model:
        q_filter &= Q(machineModel=machine_model_id)
    if filter_engine_model:
        q_filter &= Q(engineModel=engine_model_id)
    if filter_transmission_model:
        q_filter &= Q(transmissionModel=transmission_model_id)
    if filter_steerable_axle_model:
        q_filter &= Q(steerableAxleModel=steerable_axle_model_id)
    if filter_drive_axle_model:
        q_filter &= Q(driveAxleModel=drive_axle_model_id)


    if client_name:
        machines = Machine.objects.filter(client=client_id)
    elif serviceCompany__name:
        machines = Machine.objects.filter(serviceCompany=serviceCompany_id)
    elif (filter_machine_model or filter_engine_model or
          filter_transmission_model or filter_steerable_axle_model or filter_drive_axle_model):

        machines = Machine.objects.filter(q_filter)
    else:
        machines = Machine.objects.all().order_by('-shipmentDate')



    if not user.is_authenticated:
        hideInfo = 'display: none;'
    else:
        hideInfo = ''

    return render(request, 'catalog/machine_all.html', {
        'machines': machines,
        'machine_models_name': machine_models_name,
        'selected_filter': filter_machine_model,
        'filter_engine_model': filter_engine_model,
        'transmission_models_name': transmission_models_name,
        'filter_transmission_model': filter_transmission_model,
        'steerable_axle_models_name': steerable_axle_models_name,
        'filter_steerable_axle_model': filter_steerable_axle_model,
        'drive_axle_models_name': drive_axle_models_name,
        'filter_drive_axle_model': filter_drive_axle_model,

        'user': user, 'hideInfo': hideInfo, 'role': role,
        'engine_models_name': engine_models_name,
        'client': client, 'client_name': client_name, 'managers': managers,
        'serviceCompany': serviceCompany,
        'serviceCompany__name': serviceCompany__name,
        'role_error': role_error
    })


def machine_create(request):
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('machines')
    else:
        form = MachineForm()
    return render(request, 'catalog/machine_create.html', {'form': form})


def maintenance_create(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('machines')
    else:
        form = MaintenanceForm()
    return render(request, 'catalog/maintenance_create.html', {'form': form})


def claims_create(request):
    if request.method == 'POST':
        form = ClaimsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('machines')
    else:
        form = ClaimsForm()
    return render(request, 'catalog/claims_create.html', {'form': form})
