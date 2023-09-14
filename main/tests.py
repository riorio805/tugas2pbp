from django.test import TestCase, Client
from main.models import Item

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
        response = Client().get('/static/main/images/tricksnack.gif')
        self.assertEqual(response.status_code, 200)

    def test_main_items(self):
        test_item = Item(name="Trick Snack", amount= 124, description= "A packet of cooked seeds. Eat a handful of them, and they'll launch themselves to the roof of your mouth like popping candy.", rarity= 1, effect= "Recovers 2 TP for the entire team.", image_dir= "main/images/Item_Trick_Snack.png")
        test_item.save()
        response = Client().get('/main/')
        self.assertEqual(response.context["rarity"][1], "★☆☆☆☆")