from django.contrib import admin

from server.recipies.models import Recipie, Category, Photo, RecipieImage


@admin.register(Recipie)
class RecipieAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    ...

@admin.register(RecipieImage)
class RecipieImageAdmin(admin.ModelAdmin):
    ...
