from django.test import TestCase
from .models import *

# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="IceCream", price=80)
        self.assertEqual(str(item), "IceCream : 80")