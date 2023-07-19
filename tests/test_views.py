from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(
            title='IceCream', 
            price=80, 
            inventory=100
            )
        Menu.objects.create(
            title='Sandwich', 
            price=50, 
            inventory=100
            )
    def test_getall(self):
      IceCream = Menu.objects.get(title='IceCream')
      Sandwich = Menu.objects.get(title='Sandwich')
      self.assertEqual(str(IceCream), 'IceCream : 80.00')
      self.assertEqual(str(Sandwich), 'Sandwich : 50.00')