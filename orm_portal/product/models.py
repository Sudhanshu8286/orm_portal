from django.db import models

# Create your models here.

class Products(models.Model):
    Product_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    Product_image = models.ImageField(upload_to="media",default=None)
    Product_price = models.FloatField(default="10")
    EnteredBy = models.CharField(max_length=100)

    class Meta:
        db_table = 'Pro'