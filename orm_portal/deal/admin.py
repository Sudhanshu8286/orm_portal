from django.contrib import admin
from .models import Deal

# Register your models here.

class customAdmin(admin.ModelAdmin):
    list_display=['Doctor_Name','Product_Name','Quantity']
    

admin.site.register(Deal,customAdmin)
