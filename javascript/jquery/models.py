from django.db import models


# Create your models here.
class Person(models.Model):

  first_name= models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  designation=models.CharField(max_length=20)


class Map(models.Model):
  address = models.CharField(max_length=200)
  country = models.CharField(max_length=100)
  postal_code = models.CharField(max_length=100)



