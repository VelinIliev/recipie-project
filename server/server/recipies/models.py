from django.db import models


class Category(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Photo(models.Model):
    imageUrl = models.URLField()

    def __str__(self):
        return self.imageUrl


class Recipie(models.Model):
    title = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )
    ingredients = models.TextField(
        null=False,
        blank=False,
    )
    preparation = models.TextField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    preparation_time = models.IntegerField(
        null=True,
        blank=True,
    )
    cooking_time = models.IntegerField(
        null=True,
        blank=True,
    )
    portions = models.IntegerField(
        null=True,
        blank=True,
    )
    _created_at = models.DateTimeField(
        auto_now_add=True
    )
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class RecipieImage(models.Model):
    recipie = models.ForeignKey(
        Recipie,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Image for {self.recipie.title}"
