# Generated by Django 3.2.5 on 2021-08-10 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0005_alter_bb_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='img',
            field=models.ImageField(default='default/empty.jpg', null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]
