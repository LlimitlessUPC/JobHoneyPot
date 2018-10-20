from django.shortcuts import render
from .models import Offer
from django.http import HttpResponse

# Create your views here.

def load_offers(request):
    return HttpResponse(request)