from django.contrib import admin

from server.user_app.models import ExtendAppUser


# Register your models here.
@admin.register(ExtendAppUser)
class ExtendAppUserAdmin(admin.ModelAdmin):
    list_display = ['id',]