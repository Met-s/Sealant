from django.contrib import admin
from .models import UserAuth


class UserAuthAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_auth', 'role_auth')


admin.site.register(UserAuth, UserAuthAdmin)
