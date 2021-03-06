# Generated by Django 3.1.7 on 2021-02-28 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DogClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(max_length=30, verbose_name='Классификация')),
            ],
            options={
                'verbose_name': 'Классификация',
                'verbose_name_plural': 'Классификация',
            },
        ),
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dogName', models.CharField(max_length=30, verbose_name='Имя')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('weight', models.FloatField(verbose_name='Вес')),
                ('height', models.FloatField(verbose_name='Рост')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображения')),
                ('dogClass', models.ManyToManyField(blank=True, to='blog.DogClasses', verbose_name='Классификация')),
            ],
            options={
                'verbose_name': 'Собака',
                'verbose_name_plural': 'Собаки',
            },
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additionalInfo', models.TextField(blank=True, verbose_name='Дополнительная информация')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
                ('dogs', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.dogs', verbose_name='Собака')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['date'],
            },
        ),
    ]
