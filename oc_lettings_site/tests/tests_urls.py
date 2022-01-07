from django.test import SimpleTestCase
from django.urls import resolve, reverse
from oc_lettings_site.views import index

class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)