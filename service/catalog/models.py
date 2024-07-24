from django.db import models
from django.contrib.auth.models import User


class Clients(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Managers(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class MachineModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class EngineModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class TransmissionModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class DriveAxleModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class SteerableAxleModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class ServiceCompany(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Machine(models.Model):
    machineSerialNumber = models.TextField()  # Зав. № машины
    machineModel = models.ForeignKey(MachineModel,
                                     on_delete=models.CASCADE)  # Модель машины
    engineModel = models.ForeignKey(EngineModel, on_delete=models.CASCADE)
    # Модель двигателя
    engineNumber = models.TextField()  # Серийный номер двигателя
    transmissionModel = models.ForeignKey(TransmissionModel,
                                          on_delete=models.CASCADE)  #
    # Модель трансмиссии
    transmissionNumber = models.TextField()  # Серийный номер трансмиссии
    driveAxleModel = models.ForeignKey(DriveAxleModel,
                                       on_delete=models.CASCADE)  #
    # Модель ведущего
    # моста
    driveAxleNumber = models.TextField()  # Серийный номер ведущего моста
    steerableAxleModel = models.ForeignKey(SteerableAxleModel,
                                           on_delete=models.CASCADE)  #
    # Модель управляемого моста
    steerableAxleNumber = models.TextField()  # Номер управляемого моста
    deliveryContractNumber = models.TextField()  # Номер контракта на поставку
    shipmentDate = models.DateField()  # Дата отгрузки с завода
    consignee = models.TextField()  # Грузополучатель
    deliveryAddress = models.TextField()  # Адрес доставки (эксплуатации)
    equipment = models.TextField()  # Оборудование (дополнительные опции)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    serviceCompany = models.ForeignKey(ServiceCompany,
                                       on_delete=models.CASCADE)  # Сервисная компания


class MaintenanceType(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class OrganMaintenance(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Maintenance(models.Model):
    maintenanceType = models.ForeignKey(MaintenanceType,
                                        on_delete=models.CASCADE)  # Тип техобслуживания
    maintenanceDate = models.DateField()  # Дата техобслуживания
    motorResource = models.IntegerField()  # Часы, м/час моторесурс
    workOrderNumber = models.TextField()  # Номер заказа на работу
    workOrderDate = models.DateField()  # Дата заказа на работу
    organMaintenance = models.ForeignKey(OrganMaintenance,
                                         on_delete=models.CASCADE)  # Организация, выполнившая техобслуживание
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Машина
    serviceCompany = models.ForeignKey(ServiceCompany,
                                       on_delete=models.CASCADE)  # Сервисная компания


class FailureNode(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class RepairMethod(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Claims(models.Model):
    failureDate = models.DateField()  # Дата отказа
    operatingTime = models.IntegerField()  # Наработка, м/ч
    failureNode = models.ForeignKey(FailureNode,
                                    on_delete=models.CASCADE)  # Узел отказа
    failureDescription = models.TextField()  # Описание отказа
    repairMethod = models.ForeignKey(RepairMethod,
                                     on_delete=models.CASCADE)  # Метод ремонта
    usedSpareParts = models.TextField()  # Используемые запасные части
    repairDate = models.DateField()  # Дата ремонта
    equipmentDowntime = models.IntegerField()  # Время простоя оборудования
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Машина
    serviceCompany = models.ForeignKey(ServiceCompany,
                                       on_delete=models.CASCADE)  # Сервисная компания
