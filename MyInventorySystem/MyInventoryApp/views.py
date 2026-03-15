from django.shortcuts import render
from .models import Supplier

def view_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, "view_supplier.html", {"suppliers": suppliers})
# Create your views here.
    