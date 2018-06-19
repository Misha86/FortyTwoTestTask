from django.test import TestCase, Client

# Create your tests here.


class ContactsViewTests(TestCase):
    def setUp(self):
        """ Every test needs a client"""
        self.client = Client()

    def test_start_page_view(self):
        """Issue a GET request"""
        response = self.client.get('/')

        """Check that the response is 200 OK"""
        self.assertEqual(response.status_code, 200)

        """Check that the response template"""
        self.assertEqual(response.template_name, ['contacts.html', ])

        """Check that the response function`s name is 'contacts'"""
        self.assertEqual(response.get.im_func.func_name, 'contacts')


