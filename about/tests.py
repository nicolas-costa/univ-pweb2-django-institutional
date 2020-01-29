from django.test import TestCase, Client

# Create your tests here.


class AboutTest(TestCase):

    def test_if_it_displays_the_about_us_template(self):

        client = Client()

        response = client.get('/sobre')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'about/index.html')

