from django.test import TestCase
#from django.core.urlresolvers import reverse
from django.urls import reverse
from boards import views

# Create your tests here.
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse(views.home)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)