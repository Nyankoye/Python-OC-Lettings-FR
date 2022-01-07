from django.conf.urls import url
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from lettings.views import index, letting

class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('lettings:index')
        self.assertEqual(resolve(url).func, index)
    
    def test_letting_url(self):
        url = reverse('lettings:letting', args='1')
        self.assertEqual(resolve(url).func, letting)
