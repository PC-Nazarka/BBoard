# Generated by Django 3.2.5 on 2021-08-16 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_auto_20210816_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='id_room',
        ),
        migrations.AddField(
            model_name='message',
            name='id_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.chat'),
        ),
        migrations.AlterField(
            model_name='message',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
