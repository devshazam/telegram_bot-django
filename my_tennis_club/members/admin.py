from django.contrib import admin
from .models import Clients
# Register your models here.
# admin.site.register(Clients)

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'id')
    search_fields = ['name', 'email', 'id']
	
admin.site.register(Clients, ClientsAdmin)