from django.contrib import admin
from .models import Clients, Journal
# Register your models here.
# admin.site.register(Clients)

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name')
    search_fields = ['id', 'email', 'name']



admin.site.register(Clients, ClientsAdmin)
admin.site.register(Journal)