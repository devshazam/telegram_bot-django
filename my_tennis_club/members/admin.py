from django.contrib import admin
from .models import Clients
# Register your models here.
# admin.site.register(Clients)

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'id')
    search_fields = ['name', 'email', 'id']

    def my_function(self, obj) :
        return self.stock
    my_function.short_description = 'This is the Column Name'
    my_function.allow_tags = True
admin.site.register(Clients, ClientsAdmin)