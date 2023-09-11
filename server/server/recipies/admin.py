from django.contrib import admin

from server.recipies.models import Recipie, Category, Photo, Review


@admin.register(Recipie)
class RecipieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    ...


@admin.register(Review)
class PhotoAdmin(admin.ModelAdmin):
    ...

# @admin.register(RecipieImage)
# class RecipieImageAdmin(admin.ModelAdmin):
#     ...
