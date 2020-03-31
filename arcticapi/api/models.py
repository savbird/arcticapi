from django.db import models
from api.fields import JSONField


# Create your models here.
class Category(models.Model):
    title = models.TextField()

class Product(models.Model):
    #PK should never be a SSN, drivers license number, etc. They should not get released to the world
    #id = models.AutoField(primary_key=True)
    #product_id = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT) #foreign key 1-M relationship, on_delete=models.PROTECT fails cascading delete
    name = models.TextField()
    description = models.TextField()
    filename = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) #number field

class Sale(models.Model):
    name = models.TextField()
    address1 = models.TextField()
    address2 = models.TextField(null=True, blank=True)
    city = models.TextField()
    state = models.TextField()
    zipcode = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    items = JSONField(default=dict)
    payment_intent = JSONField(default=dict)

