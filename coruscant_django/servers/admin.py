from django.contrib import admin
from .models import Server

class ServerAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'ip_address', 'port']
admin.site.register(Server, ServerAdmin)