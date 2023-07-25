from django.db import models
from doctor.models import Doctors

# Create your models here.

class Appointment(models.Model):
    Doctor_Name = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Date_of_Schedule = models.DateField()
    Time_of_Schedule = models.TimeField()
    Entered_by = models.CharField(max_length=100,default=None)

    class Meta:
        db_table = 'Appointment'


