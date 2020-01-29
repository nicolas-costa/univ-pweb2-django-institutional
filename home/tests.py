from django.test import TestCase, Client

# Create your tests here.


class HomeTest(TestCase):

    def test_if_it_displays_the_home_template(self):

        client = Client()

        response = client.get('/')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'home/index.html')


