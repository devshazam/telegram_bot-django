from django.db import models

class Clients(models.Model):
    name = models.TextField(verbose_name='Имя')
    email = models.EmailField()
    documentNumber = models.CharField(max_length=255)
    documentDate = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    UrAddress = models.TextField(blank=True)
    ogrn = models.CharField(max_length=255, blank=True)
    inn = models.CharField(max_length=255, blank=True)
    kpp = models.CharField(max_length=255, blank=True)
    bank = models.CharField(max_length=255, blank=True)
    bik = models.CharField(max_length=255, blank=True)
    rs = models.CharField(max_length=255, blank=True)
    ks = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
