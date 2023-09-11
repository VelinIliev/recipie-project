from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


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
    _updated_at = models.DateTimeField(
        auto_now=True
    )

    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Photo(models.Model):
    imageUrl = models.URLField()
    recipie = models.ForeignKey(
        to=Recipie,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.imageUrl


class Review(models.Model):
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.CharField(
        max_length=250,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    recipie = models.ForeignKey(Recipie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'{self.rating} - {self.description} - {self.recipie}'
