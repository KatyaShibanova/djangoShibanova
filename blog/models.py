from django.db import models
from django.contrib.auth.models import User


class Dogs(models.Model):
    dogName = models.CharField(verbose_name='Имя',
                               max_length=50)

    description = models.TextField(verbose_name='Описание',
                                   blank=True)

    weight = models.FloatField(verbose_name='Вес',
                               blank=False)

    height = models.FloatField(verbose_name='Рост',
                               blank=False)

    age = models.FloatField(verbose_name='Возраст', blank=False)

    price = models.FloatField(verbose_name="Цена")

    photo = models.ImageField(verbose_name='Изображения',
                              upload_to='photos/%Y/%m/%d/', blank=True)

    dogClass = models.ManyToManyField('DogClasses', verbose_name='Классификация', blank=True)

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'

    def __str__(self):
        return self.dogName


class DogClasses(models.Model):
    className = models.CharField(verbose_name='Классификация',
                                 max_length=50)

    class Meta:
        verbose_name = 'Классификация'
        verbose_name_plural = 'Классификация'

    def __str__(self):
        return self.className


class Deals(models.Model):
    client = models.ForeignKey(User, verbose_name='Клиент', on_delete=models.PROTECT, null=False)

    dogs = models.ForeignKey('Dogs', verbose_name='Собака', on_delete=models.PROTECT, null=False)

    additionalInfo = models.TextField(verbose_name='Дополнительная информация', blank=True)

    date = models.DateTimeField(verbose_name='Дата покупки',
                                auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на покупку'
        verbose_name_plural = 'Заявки на покупку'
        ordering = ['date']
