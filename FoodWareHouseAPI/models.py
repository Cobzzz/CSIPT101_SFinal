from django.db import models


# Create your models here.

class foods(models.Model):
    Mfd_id= models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    UnitPrice = models.DecimalField(max_digits=5,decimal_places=2)
    UnitsInStock = models.PositiveSmallIntegerField()
