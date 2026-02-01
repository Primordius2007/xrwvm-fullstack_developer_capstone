from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from .restapis import get_request
import json

from .models import CarMake, CarModel
from .populate import initiate


# =========================
# AUTHENTICATION
# =========================

@csrf_exempt
def login_user(request):
    """
    Handle user login from React frontend
    """
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("userName")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse(
                {
                    "userName": username,
                    "status": "Authenticated",
                }
            )

        return JsonResponse({"status": "Failed"}, status=401)

    return JsonResponse({"error": "Invalid request"}, status=400)


# =========================
# CARS (CarMake / CarModel)
# =========================

def get_cars(request):
    """
    Populate and return car makes and models
    """
    if CarMake.objects.count() == 0:
        initiate()

    car_models = CarModel.objects.select_related("car_make")
    cars = []

    for model in car_models:
        cars.append(
            {
                "CarModel": model.name,
                "CarMake": model.car_make.name,
            }
        )

    return JsonResponse({"CarModels": cars})


# =========================
# DEALERS (MOCK DATA)
# =========================

def get_dealer_details(request, dealer_id):
    """
    Return dealer details for Dealer.jsx
    (Backend service is mocked in this phase)
    """
    dealer = {
        "id": dealer_id,
        "full_name": f"Dealer {dealer_id}",
        "address": "123 Main Street",
        "city": "Austin",
        "state": "Texas",
        "zip": "73301",
    }

    return JsonResponse(
        {
            "status": 200,
            "dealer": [dealer],
        }
    )


def get_dealer_reviews(request, dealer_id):
    """
    Return reviews for a dealer
    (Empty list is valid)
    """
    return JsonResponse(
        {
            "status": 200,
            "reviews": [],
        }
    )


# =========================
# PLACEHOLDERS (REQUIRED)
# =========================

def logout_request(request):
    """
    Placeholder for logout
    """
    return JsonResponse({"status": "Logged out"})


def registration(request):
    """
    Placeholder for registration
    """
    return JsonResponse({"status": "Registered"})


def get_dealerships(request, state="All"):
    """
    Fetch all dealerships or filter by state
    """
    if state == "All":
        endpoint = "/fetchDealers"
    else:
        endpoint = f"/fetchDealers/{state}"

    dealerships = get_request(endpoint)

    return JsonResponse(
        {
            "status": 200,
            "dealers": dealerships,
        }
    )
