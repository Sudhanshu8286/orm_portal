from django.contrib import admin
from .models import Doctors
# Register your models here.

class customAdmin(admin.ModelAdmin):
    list_display=['Doctor_Name','Doctor_Specialisation','Doctor_Contact_Number','Doctor_Location','EnteredBy']
    

admin.site.register(Doctors,customAdmin)