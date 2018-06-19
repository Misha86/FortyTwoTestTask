from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField('name', max_length=50)
    last_name = models.CharField('last name', max_length=50)
    date_of_birth = models.DateField('date of birth')
    bio = models.TextField('bio', max_length='1000', unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = 'person'
        verbose_name_plural = "persons"

    def __str__(self):
        return self.name


class Contacts(models.Model):
    person = models.OneToOneField(Person, related_name='contacts',
                                  on_delete=models.CASCADE)
    email = models.EmailField('email')
    jabber = models.CharField('jabber', max_length=50)
    skype = models.CharField('skype', max_length=50)
    other_contacts = models.TextField('other_contacts', max_length=500)

    class Meta:
        ordering = ["person"]

    def __str__(self):
        return "Contacts for {}".format(self.person.name)
