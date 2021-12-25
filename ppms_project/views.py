from django.shortcuts import render
from raspberry_pi import get_data
# import bluetooth
import time
import datetime

def about(request):
    context = {
        "title": "About | Portable Patient Monitoring System",
    }
    return render(request, "about.html", context)

def index(request):
    context = {
        "title": "Login | Portable Patient Monitoring System",
    }
    return render(request, "login.html", context)


def dashboard(request):
    context = {
        "title": get_data.bd_addr,
    }
    
    return render(request, "dashboard.html", context)

def faq(request):
    context = {
        "title": "FAQ | Portable Patient Monitoring System",
    }
    return render(request, "faq.html", context)


def patient(request):

    context = {
        "title": "Patient | Portable Patient Monitoring System",
    }
    return render(request, "patient.html", context)