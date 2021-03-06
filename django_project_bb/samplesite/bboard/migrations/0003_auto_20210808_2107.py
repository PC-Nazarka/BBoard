# Generated by Django 3.2.5 on 2021-08-08 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bboard', '0002_auto_20210722_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ID пользователя'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bboard.rubric', verbose_name='Рубрика'),
        ),
    ]
