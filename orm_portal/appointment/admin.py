from django.contrib import admin
from .models import Appointment

# Register your models here.

class customAdmin(admin.ModelAdmin):
    list_display=['Doctor_Name','Date_of_Schedule','Time_of_Schedule']
    

admin.site.register(Appointment,customAdmin)