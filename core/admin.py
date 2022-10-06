from django.contrib import admin

# Register your models here.
from .models import AuthUser, ProfileImage, MemberProfile, Queue,QueueUser

admin.site.register(AuthUser)
admin.site.register(ProfileImage)
admin.site.register(MemberProfile)
admin.site.register(Queue)
admin.site.register(QueueUser)