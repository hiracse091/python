from django.contrib import admin
from kk_user.models import UserProfile, UserType

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserType)