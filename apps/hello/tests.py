from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from apps.hello.models import Person, Contacts

# Create your tests here.


class ContactsViewTests(TestCase):
    fixtures = ['person_data.json']

    def setUp(self):
        """ Every test needs a client"""
        self.client = Client()

    def test_start_page_view(self):
        """Issue a GET request"""
        response = self.client.get(reverse('contacts'))

        """Check that the response is 200 OK"""
        self.assertEqual(response.status_code, 200)


class ContactsModelTests(TestCase):
    def setUp(self):
        """ Create person for test"""
        person = Person.objects.create(name="Misha", last_name="Polishchuk",
                                       date_of_birth='1986-09-17',
                                       bio='I live in Rivne')
        Contacts.objects.create(person=person, email='misha86@ukr.net',
                                jabber='misha86', skype='mp_user',
                                other_contacts='phone number: +38977478910')
        self.person = Person.objects.get(name="Misha")

    def test_modes(self):
        """Check that the person was created"""
        self.assertEqual(self.person.last_name, 'Polishchuk')
        self.assertEqual(self.person.contacts.skype, 'mp_user')

    def test_str(self):
        """
        Method `__str__` should be equal to field `name`
        """
        self.assertEqual(str(self.person.contacts),
                         "Contacts for {}".format(self.person.name))
        self.assertEqual(str(self.person), self.person.name)
