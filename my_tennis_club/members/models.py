from django.db import models

class Clients(models.Model):
    name = models.TextField(verbose_name='Имя')
    email = models.EmailField()
    documentNumber = models.CharField(max_length=255, verbose_name='Номер договора')
    documentDate = models.CharField(max_length=255, verbose_name='Дата договора')
    phone = models.CharField(max_length=255, blank=True, verbose_name='Номер телефона')
    address = models.TextField(blank=True, verbose_name='Адрес')
    UrAddress = models.TextField(blank=True, verbose_name='Юридический адрес')
    ogrn = models.CharField(max_length=255, blank=True, verbose_name='ОГРН')
    inn = models.CharField(max_length=255, blank=True, verbose_name='ИНН')
    kpp = models.CharField(max_length=255, blank=True, verbose_name='КПП')
    bank = models.CharField(max_length=255, blank=True, verbose_name='Банк')
    bik = models.CharField(max_length=255, blank=True, verbose_name='БИК')
    rs = models.CharField(max_length=255, blank=True, verbose_name='Расчетный счет')
    ks = models.CharField(max_length=255, blank=True, verbose_name='Кор. счет')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Journal(models.Model):
    name = models.CharField(max_length=255, unique=True)
    number = models.IntegerField()

class Errors(models.Model):
    description = models.TextField()