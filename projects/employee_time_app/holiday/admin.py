from django.contrib import admin
from holiday.models import Holiday, PersonalLeave, SpecialNotes
# Register your models here.
admin.site.register(Holiday)
admin.site.register(PersonalLeave)
admin.site.register(SpecialNotes)
