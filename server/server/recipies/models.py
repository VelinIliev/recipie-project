from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

UserModel = get_user_model()

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
    avg_rating = models.FloatField(default=0)
    total_reviews = models.IntegerField(default=0)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


def upload_to(instance, filename):
    return '/'.join(['images', filename])


class Photo(models.Model):
    imageUrl = models.ImageField(upload_to=upload_to, blank=True, null=True)
    recipie = models.ForeignKey(Recipie, on_delete=models.CASCADE, related_name='photos')

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
    review_user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.rating} - {self.description} - {self.recipie}'


class Comment(models.Model):
    text = models.TextField(
        max_length=250,
        null=False,
        blank=False
    )
    recipie = models.ForeignKey(Recipie, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(
        UserModel,
        null=True,
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Comment by {self.comment_user or 'Anonymous User'}"
