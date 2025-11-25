from django.shortcuts import render
from .models import Cupom

def cupons(request):
    cupons = Cupom.objects.all()
    return render(request, "cupom.html", {"cupons": cupons})

def home(request):
    return render(request, "home.html")
