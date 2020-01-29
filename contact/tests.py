from django.test import TestCase, Client
from contact.models import Contact

# Create your tests here.


class ContactTest(TestCase):

    client = Client()

    def test_if_it_displays_the_contact_us_template(self):

        response = self.client.get('/contato')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'contact/index.html')

    def test_if_it_stores_the_contact_us_form_data(self):

        response = self.client.post('/contato', {'name': 'foo', 'email': 'foo@bar.com', 'msg': 'foobar'})

        self.assertEqual(response.status_code, 200, 'Mensagem enviada!')

        self.assertTrue(Contact.objects.filter(name='foo').exists())
