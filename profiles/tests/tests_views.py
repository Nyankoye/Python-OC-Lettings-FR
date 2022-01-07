from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create(
                password = '1234loua',
                username = 'Nyl95',
            )
        self.profile = Profile.objects.create(
            favorite_city = 'Buenos Aires',
            user_id = self.user.id
        )
    
    def test_index_view(self):

        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_profile_view(self):

        response = self.client.get(reverse('profiles:profile', kwargs={'username':'Nyl95'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')