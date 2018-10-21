from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


from .models import Offer

from django.http import HttpResponse,JsonResponse
import matchFields
from jobhoneypot_backend.apirequest import get_job
# Create your views here.
@csrf_exempt
def load_offers(request):
    #return HttpResponse("Hello World")
    json_input = json.load(request)
    skill_list = matchFields.matchFields(json_input['cv'],json_input['category'])
    offers_output = get_job(skill_list)
    print("Offers Output")
    print(offers_output)
    simple_offers = {'offers':[]}
    for raw_offer_item in offers_output['offers']:
        simplified_offer = get_simplified_offer(raw_offer_item)
        simple_offers['offers'].append(simplified_offer)

    #r = json.dumps(offers_output)
    print("FINAL offers: ")
    print(simple_offers)
    return JsonResponse(simple_offers)


def get_simplified_offer(offer_json_item):
    result_offer = {}
    result_offer['id'] = offer_json_item['id']
    result_offer['title'] = offer_json_item['title']
    result_offer['link'] = offer_json_item['link']
    result_offer['location'] = "%s, %s" % (offer_json_item['city'],offer_json_item['province']['value'])
    if (offer_json_item['contractType']['value'] != ''):
        result_offer['contractType'] = offer_json_item['contractType']['value']
    else :
        result_offer['contractType'] = 'N/A'
    result_offer['workDay'] = offer_json_item['workDay']['value']
    result_offer['requirementMin'] = offer_json_item['requirementMin']
    result_offer['author_name'] = offer_json_item['author']['name']
    if (offer_json_item['salaryMax']['value'] != ''):
        result_offer['salaryMax'] = offer_json_item['salaryMax']['value']
    else :
        result_offer['salaryMax'] = 0
    return result_offer





