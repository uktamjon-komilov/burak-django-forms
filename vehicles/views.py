from django.http import JsonResponse
import json
from django.http.response import HttpResponse
import requests


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
    print(response.status_code)

    return JsonResponse(response.json())