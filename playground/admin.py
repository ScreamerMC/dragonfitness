from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from .models import Room, Topic, Message, User


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(User)
admin.site.register(Room, MyModelAdmin)
admin.site.register(Topic)
admin.site.register(Message)

