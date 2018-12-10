from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    cost = models.DecimalField(max_digits=20, decimal_places=2,  null=False, blank=False, verbose_name='Стоимость')

    def __str__(self):
        return self.name
