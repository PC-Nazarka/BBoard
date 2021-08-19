# Generated by Django 3.2.5 on 2021-08-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20210816_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='id_room',
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='username',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
