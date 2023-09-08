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
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0
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
