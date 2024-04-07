from django.contrib import admin

from .models import Leave, Reimbusement, Employaccdata, Msgdata, Chatdata

# # Register your models here.

admin.site.register(Leave)
admin.site.register(Chatdata)
admin.site.register(Reimbusement)
admin.site.register(Employaccdata)
admin.site.register(Msgdata)
# admin.site.register(Clusterdata)