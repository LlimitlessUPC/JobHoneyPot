from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Offer
from django.http import HttpResponse
import matchFields
import jobhoneypot_backend.apirequest
# Create your views here.
@csrf_exempt
def load_offers(request):
    #return HttpResponse("Hello World")


    return HttpResponse(request)

