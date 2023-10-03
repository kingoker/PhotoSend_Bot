# Generated by Django 4.2.5 on 2023-09-30 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Картинка')),
                ('caption', models.TextField(verbose_name='Описание')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('task_time', models.DateTimeField(verbose_name='Дата и время публикации')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
