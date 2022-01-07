from django.test import TestCase
from django.urls import reverse
from lettings.models import Address, Letting

class TestViews(TestCase):
    
    def setUp(self):
        self.adresse = Address.objects.create(
                number = 7217,
                street ='Bedford Street',
                city = 'Brunswick',
                state = 'GA',
                zip_code = 31525,
                country_iso_code = 'USA'
            )
        self.letting = Letting.objects.create(
            title = 'Joshua Tree Green Haus /w Hot Tub',
            address_id = self.adresse.id
        )

    def test_index_view(self):

        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
    
    def test_letting_view(self):

        response = self.client.get(reverse('lettings:letting', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')