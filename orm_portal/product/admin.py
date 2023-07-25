from django.contrib import admin
from .models import Products
from django.utils.html import format_html


class customAdmin(admin.ModelAdmin):
    list_display=['Product_name','company_name','img_display','Product_price','EnteredBy']
    list_filter=['Product_name','Product_price']

    def img_display(self,obj):
        return format_html('<img scr="{}" width="90" height="100" />',obj.Product_image.url)

# Register your models here.

admin.site.register(Products,customAdmin)

