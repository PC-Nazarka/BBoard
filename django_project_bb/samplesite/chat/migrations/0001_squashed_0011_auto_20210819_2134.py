# Generated by Django 3.2.5 on 2021-08-19 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('chat', '0001_initial'), ('chat', '0002_auto_20210816_1723'), ('chat', '0003_auto_20210816_1751'), ('chat', '0004_auto_20210816_1935'), ('chat', '0005_auto_20210816_2106'), ('chat', '0006_auto_20210817_1740'), ('chat', '0007_auto_20210817_1758'), ('chat', '0008_auto_20210817_1843'), ('chat', '0009_room_name'), ('chat', '0010_auto_20210817_2054'), ('chat', '0011_auto_20210819_2134')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_first', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_first', to=settings.AUTH_USER_MODEL)),
                ('member_second', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_second', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.room')),
            ],
            options={
                'ordering': ('date_added',),
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
