from django.test import TestCase
from .models import Offer
# Create your tests here.
class OfferModelTestCase(TestCase):
    def test_offer_title_initializing(self):
        offer = Offer()
        self.assertIsNone(offer.title)
