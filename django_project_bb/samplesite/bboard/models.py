from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import os
from PIL import Image
from django.contrib.contenttypes.fields import GenericRelation


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name="Товар")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    img = models.ImageField(upload_to='images/', default='empty.jpg', null=True, verbose_name='Изображение')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.CASCADE, verbose_name='Рубрика')
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='ID пользователя')
    comment = GenericRelation('comment')

    class Meta:
        verbose_name_plural = "Объявления"
        verbose_name = "Объявление"
        ordering = ['-published']

    def get_absolute_url(self):
        return f'/item_bb_{self.id}'

    def save(self, *args, **kwargs):
        print(self.img.name)
        if self.img.path[-9:] != 'empty.jpg':
            size = (200, 200)
            time = datetime.now().strftime("%Y-%m-%d")
            end_extention = self.img.name.split(".")[-1]
            head = self.img.name.split(".")[0]
            file_name = head + "_" + time + "." + end_extention
            self.img.name = os.path.join(f"{self.title}/", f"user_{self.title}_{file_name}")
            super().save(*args, **kwargs)
            print(self.img.path)
            original_photo = Image.open(self.img.path)
            width, height = original_photo.size
            if (width != 0) and (height != 0):
                resized_image = original_photo.resize(size)
                resized_image.save(self.img.path)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = "Рубрика"
        ordering = ['name']

class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(verbose_name='Текст комментария')
    bb_id = models.ForeignKey(Bb, verbose_name='Объявление', on_delete=models.CASCADE, related_name='comment_bb', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, verbose_name='Дата написания комментарий')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Комментарии"
        verbose_name = "Комментарий"
