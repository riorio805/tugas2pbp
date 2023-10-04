from django.test import TestCase, Client
from main.models import Item

# Create your tests here.
class mainTest(TestCase):
    def setUpTestData(cls):
        Item.objects.create(
            name="Trick Snack",
            amount=124,
            description="A packet of cooked seeds. Eat a handful of them, and they'll launch themselves to the roof of your mouth like popping candy.",
            rarity=1,
            effect="Recovers 2 TP for the entire team.",
            image_dir="/static/main/images/Item_Trick_Snack.png",
            created_by=1)
        

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
        response = Client().get('/static/main/images/tricksnack.gif')
        self.assertEqual(response.status_code, 200)

    def test_create_item(self):
        response = Client().post('/main/create_item', {
            'name':"test",
            'amount':1,
            'description':"this is a test",
            'rarity':3,
            'effect':"mouse",
            'image_dir':"https://m.media-amazon.com/images/I/61nU0e78NgL._AC_UF894,1000_QL80_.jpg"}, follow=True)
        
        # Redirected
        self.assertRedirects(response, "/main/")
        # Item successfully added
        self.assertTrue(response.context["items"])
        
    def test_json(self):
        response = Client().get('/json/')

    def test_xml(self):
        response = Client().get('/xml/')
    
    