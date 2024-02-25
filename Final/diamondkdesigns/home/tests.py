from django.test import TestCase
from django.test import Client

# Create your tests here.
class PageViewTests(TestCase):

    c = Client()

    def test_page_status_code(self):
        response = self.c.get('/decal', follow= True)
        self.assertEquals(response.status_code, 200)