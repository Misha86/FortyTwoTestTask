from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from apps.hello.views import contacts

# Create your tests here.


class ContactsViewTests(TestCase):
    def setUp(self):
        """ Every test needs a client"""
        self.factory = RequestFactory()

    def test_start_page_view(self):
        """Issue a GET request"""
        request = self.factory.get(reverse('contacts'))
        response = contacts(request)

        """Check that the response is 200 OK"""
        self.assertEqual(response.status_code, 200)


class ContactsModelTests(TestCase):
    def setUp(self):
        """ Create person for test"""
        Person(name = "Misha", last_name = "Polishchuk", date_of_birth='1986-09-17', bio='I live in Rivne')
        Contacts(person=self.person, email='misha86@ukr.net', jabber='misha86',
                                 skype='mp_user', other_contacts='phone number: +38977478910')

    def test_modes(self):
        """Issue a GET request"""
        lion = Person.objects.get(name="Misha")

        """Check that the person was created"""
        self.assertEqual(lion.last_name, 'Polishchuk')
        self.assertEqual(lion.contacts.skype, 'mp_user')
