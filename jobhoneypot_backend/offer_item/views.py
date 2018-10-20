from django.shortcuts import render
from .models import Offer
# Create your views here.

def load_offers(request):
    offer_list = Offer.objects.all()