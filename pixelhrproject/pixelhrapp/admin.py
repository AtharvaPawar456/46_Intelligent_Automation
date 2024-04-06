from django.contrib import admin

from .models import Leave, Reimbusement

# # Register your models here.

admin.site.register(Leave)
admin.site.register(Reimbusement)
# admin.site.register(Clusterdata)