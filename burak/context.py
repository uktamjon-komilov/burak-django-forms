from vehicles.models import *

def vehicle(request):
    try:
        path = request.path

        path_splitted = path.split("/")

        id = path_splitted[3]

        try:
            id = int(id)
        except:
            id = None
        
        if not id:
            return {"vehicle": None}

        vehicle = None
        
        if path_splitted[2] == "hire":
            vehicle = Hire.objects.get(id=id).vehicle

        if path_splitted[2] == "service":
            vehicle = Service.objects.get(id=id).vehicle

        if path_splitted[2] == "supplier":
            vehicle = Supplier.objects.get(id=id).vehicle

        if path_splitted[2] == "finance":
            vehicle = Finance.objects.get(id=id).vehicle
        
        if path_splitted[2] == "sale":
            vehicle = Sale.objects.get(id=id).vehicle

        if path_splitted[2] == "vehicle":
            vehicle = Vehicle.objects.get(id=id)

        return {"vehicle": vehicle}
    except:
        return {}