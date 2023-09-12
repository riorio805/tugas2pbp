from django.test import TestCase, Client

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_landing_using_markdown(self):
        response = Client().get('/')
        self.assertTemplateUsed(response, 'md.html')

    def test_static(self):
        response = Client().get('/static/main/media/tricksnack.gif')
        self.assertEqual(response.status_code, 200)
