from django.db import models

# Create your models here.


class TaskManager(models.Model):
    image = models.ImageField(upload_to="images/", verbose_name="Картинка");
    caption = models.TextField(verbose_name="Описание", blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Опубликовано")
    task_date = models.DateField(verbose_name="Дата публикации")
    task_time = models.TimeField(verbose_name="время публикации")

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

