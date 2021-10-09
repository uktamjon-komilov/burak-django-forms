from django.http import JsonResponse
import json
from django.http.response import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt

from vehicles.models import Vehicle

from .category import CATEGORY


def fetch_dvla(request):
    if request.method == "GET":
        return HttpResponse("Working")
    
    data = json.loads(request.body)

    url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

    payload = {
        "registrationNumber": data["number"]
    }
    headers = {
        "x-api-key": "h7h5LtDFbr6o6BOoS3GGn4ZzvSW1Kad339C5RYGH",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, headers=headers, json = payload)

    return JsonResponse(response.json())


@csrf_exempt
def sub_category(request):
    cat = json.loads(request.body)["cat"]
    subs = list(CATEGORY[cat].keys())
    return JsonResponse(subs, safe=False)


@csrf_exempt
def mini_category(request):
    cat = json.loads(request.body)["cat"]
    sub = json.loads(request.body)["sub"]
    minis = CATEGORY[cat][sub]
    return JsonResponse(minis, safe=False)


@csrf_exempt
def vec(request):
    vec = json.loads(request.body)["vec"]
    vehicle = Vehicle.objects.get(id=vec)
    return JsonResponse({"value": vehicle.vehicle_dvla_number})