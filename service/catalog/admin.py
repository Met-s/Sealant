from django.contrib import admin
from .models import (Clients, Managers, MachineModel, EngineModel,
                     TransmissionModel, DriveAxleModel, SteerableAxleModel,
                     ServiceCompany, Machine, MaintenanceType,
                     OrganMaintenance, Maintenance, FailureNode,
                     RepairMethod, Claims, Role)


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ManagersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MachineModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class EngineModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
    
class TransmissionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
    
class DriveAxleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class SteerableAxleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ServiceCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MachineAdmin(admin.ModelAdmin):
    pass


class MaintenanceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class OrganMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MaintenanceAdmin(admin.ModelAdmin):
    pass


class FailureNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class RepairMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ClaimsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Clients, ClientsAdmin)
admin.site.register(Managers, ManagersAdmin)
admin.site.register(MachineModel, MachineModelAdmin)
admin.site.register(EngineModel, EngineModelAdmin)
admin.site.register(TransmissionModel, TransmissionModelAdmin)
admin.site.register(DriveAxleModel, DriveAxleModelAdmin)
admin.site.register(SteerableAxleModel, SteerableAxleModelAdmin)
admin.site.register(ServiceCompany, ServiceCompanyAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(MaintenanceType, MaintenanceTypeAdmin)
admin.site.register(OrganMaintenance, OrganMaintenanceAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(FailureNode, FailureNodeAdmin)
admin.site.register(RepairMethod, RepairMethodAdmin)
admin.site.register(Claims, ClaimsAdmin)
admin.site.register(Role)
