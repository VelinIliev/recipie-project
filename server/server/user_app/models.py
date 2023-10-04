from enum import Enum

from django.conf import settings
from django.contrib.auth import models as auth_models, get_user_model
from django.core import validators
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

UserModel = get_user_model()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        ExtendAppUser.objects.create(user=instance)


def upload_to(instance, filename):
    return '/'.join(['users_photos', filename])


class ExtendAppUser(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    imageUrl = models.ImageField(upload_to=upload_to, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(
        choices=(
            ('male', 'Male'),
            ('female', 'Female'),
            ('doNotShow', 'Do not show'),
        ),
        null=True,
        blank=True
        )
