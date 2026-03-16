from django.shortcuts import render
from .models import Supplier, WaterBottle

def view_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, "view_supplier.html", {"suppliers": suppliers})

# View Bottles View
def view_bottles(request):
    bottles = WaterBottle.objects.all()
    return render(request, "view_bottles.html", {"bottles":bottles})

    