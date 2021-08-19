# Generated by Django 3.2.5 on 2021-08-17 11:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0007_auto_20210817_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='id_first_member',
        ),
        migrations.RemoveField(
            model_name='room',
            name='id_second_member',
        ),
        migrations.AddField(
            model_name='room',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
