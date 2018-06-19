from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.TextField('name', max_length=50, unique=True)
    last_name = models.TextField('last name', max_length=50, unique=True)
    date_of_birth = models.DateField('date of birth' )
