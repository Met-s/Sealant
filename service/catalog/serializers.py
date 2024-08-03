from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'is_superuser', 'is_active']


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ['id', 'name', 'description', 'role']


class ManagersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Managers
        fields = ['id', 'name', 'description', 'role']


class MachineModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MachineModel
        fields = ['id', 'name', 'description']


class EngineModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EngineModel
        fields = ['id', 'name', 'description']


class TransmissionModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransmissionModel
        fields = ['id', 'name', 'description']


class DriveAxleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DriveAxleModel
        fields = ['id', 'name', 'description']


class SteerableAxleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SteerableAxleModel
        fields = ['id', 'name', 'description']


class ServiceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCompany
        fields = ['id', 'name', 'description', 'role']


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['id', 'machineSerialNumber', 'machineModel', 'engineModel',
                  'engineNumber', 'transmissionModel', 'transmissionNumber',
                  'driveAxleModel', 'driveAxleNumber', 'steerableAxleNumber',
                  'deliveryContractNumber', 'shipmentDate', 'consignee',
                  'deliveryAddress', ' equipment', 'client', 'serviceCompany']


class MaintenanceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaintenanceType
        fields = ['id', 'name', 'description']


class OrganMaintenanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrganMaintenance
        fields = ['id', 'name', 'description']


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ['id', 'maintenanceType', 'maintenanceDate',
                  'motorResource', 'workOrderNumber', 'workOrderDate',
                  'organMaintenance', 'machine', 'serviceCompany']


class FailureNodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FailureNode
        fields = ['id', 'name', 'description']


class RepairMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RepairMethod
        fields = ['id', 'name', 'description']


class ClaimsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claims
        fields = ['id', 'failureDate', 'operatingTime', 'failureNode',
                  'failureDescription', 'repairMethod', 'usedSpareParts',
                  'repairDate', 'equipmentDowntime', 'machine',
                  'serviceCompany']

