from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Group)
admin.site.register(GroupUsers)
admin.site.register(GroupJoinRequest)
admin.site.register(Message)
