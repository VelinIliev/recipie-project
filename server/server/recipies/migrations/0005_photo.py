# Generated by Django 4.2.5 on 2023-09-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipies', '0004_recipie_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageUrl', models.URLField()),
                ('recipie_id', models.URLField()),
            ],
        ),
    ]
