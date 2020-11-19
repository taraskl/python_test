from django.db import models

# Create your models here.
class Order(models.Model):
    creation_date = models.DateTimeField()
    product = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.creation_date)

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateTimeField()
    registration_date = models.DateTimeField()
    order = models.ForeignKey(Order, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)