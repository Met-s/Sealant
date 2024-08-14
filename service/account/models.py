from django.db import models
from django.contrib.auth.models import User

from catalog.models import Role, Clients, ServiceCompany


class UserAuth(models.Model):
    user_auth = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    role_auth = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    clients_auth = models.ForeignKey(Clients, on_delete=models.DO_NOTHING,
                                     null=True, blank=True)
    serviceCompany_auth = models.ForeignKey(ServiceCompany,
                                            on_delete=models.DO_NOTHING,
                                            null=True, blank=True)
