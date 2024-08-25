from django import forms

from .models import Machine, Maintenance, Claims


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['machineSerialNumber', 'machineModel', 'engineModel',
                  'engineNumber', 'transmissionModel', 'transmissionNumber',
                  'driveAxleModel', 'driveAxleNumber', 'steerableAxleModel',
                  'steerableAxleNumber', 'deliveryContractNumber',
                  'shipmentDate', 'consignee', 'deliveryAddress',
                  'equipment', 'client', 'serviceCompany']

        # def __str__(self):
        #     return f'{self.machineSerialNumber} : {self.machineModel}'


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['maintenanceType', 'maintenanceDate', 'motorResource',
                  'workOrderNumber', 'workOrderDate', 'organMaintenance',
                  'machine', 'serviceCompany']


class ClaimsForm(forms.ModelForm):
    class Meta:
        model = Claims
        fields = ['failureDate', 'operatingTime', 'failureNode',
                  'failureDescription', 'repairMethod', 'usedSpareParts',
                  'repairDate', 'equipmentDowntime', 'machine',
                  'serviceCompany']
