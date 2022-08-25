from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    age = models.IntegerField()

class Segments(models.Model):
    segment_class = models.CharField(max_length=10)
    customers = models.ManyToManyField(Customer)

class NewModelClass(models.Model):
    name = models.CharField(max_length=10)

class NewClass2(models.Model):
    name = models.CharField(max_length=23)

"""
# pre_save -> instance
instance = Customer.objects.create() #save a new customer into database
# post_save -> instance, created = True

# pre_save -> instance
instance.save() #save it again
# post_save -> instance, created = False
"""