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
