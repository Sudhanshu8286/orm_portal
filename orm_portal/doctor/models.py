from django.db import models

# Create your models here.

class Doctors(models.Model):

    # SPECIALISATION_CHOICES = (
    #     ('Chest', 'Chest'),
    #     ('Heart', 'Heart'),
    #     ('General', 'General'),
    #     ('Orthopaedic', 'Orthopaedic'),
    # )
    

    
    Doctor_Name = models.CharField(max_length=100)
    Doctor_Specialisation = models.CharField(max_length=100)
    Doctor_Contact_Number = models.CharField(max_length=10)
    Doctor_Location = models.CharField(max_length=100)
    EnteredBy = models.CharField(max_length=100)

    class Meta:
        db_table = 'Doc'