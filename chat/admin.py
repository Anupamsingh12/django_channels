from django.contrib import admin
from .models import Message,Room,groupMessage

admin.site.register(Message)
# Register your models here.
admin.site.register(Room)
admin.site.register(groupMessage)