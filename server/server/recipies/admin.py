from django.contrib import admin

from server.recipies.models import Recipie


@admin.register(Recipie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']

