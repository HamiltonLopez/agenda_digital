from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    class Meta:
        abstract = True

# Create your models here.
class Contact(Person):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
