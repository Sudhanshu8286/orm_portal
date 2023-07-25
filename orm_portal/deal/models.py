from django.db import models
from doctor.models import Doctors
from product.models import Products

# Create your models here.

class Deal(models.Model):
    Doctor_Name = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Product_Name = models.ForeignKey(Products,on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)
    Date= models.DateField(default=None)
    Entered_by = models.CharField(max_length=100)

    class Meta:
        db_table = 'Deal'


