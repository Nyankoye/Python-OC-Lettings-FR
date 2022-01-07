from django.test import SimpleTestCase
from django.urls import resolve, reverse
from profiles.views import index, profile

class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('profiles:index')
        self.assertEqual(resolve(url).func, index)
    
    def test_profile_url(self):
        url = reverse('profiles:profile', kwargs={'username':'DavWin'})
        self.assertEqual(resolve(url).func, profile)