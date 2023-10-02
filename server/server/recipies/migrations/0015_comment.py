# Generated by Django 4.2.5 on 2023-10-02 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipies', '0014_remove_photo_recipie_recipie_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=250)),
                ('recipie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipies.recipie')),
                ('review_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
