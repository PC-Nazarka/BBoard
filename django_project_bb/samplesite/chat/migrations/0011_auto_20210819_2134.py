# Generated by Django 3.2.5 on 2021-08-19 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_auto_20210817_2054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('date_added',), 'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Комната', 'verbose_name_plural': 'Комнаты'},
        ),
    ]
