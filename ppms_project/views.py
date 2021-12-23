from django.shortcuts import render
# from raspberry_pi import get_data
# import bluetooth
import time
import datetime

def index(request):
    context = {
        "title": "Login | Portable Patient Monitoring System",
    }
    return render(request, "login.html", context)


def dashboard(request):
    context = {
        "title": "Dashboard | Portable Patient Monitoring System",
    }
    
    return render(request, "dashboard.html", context)

def patient(request):

    context = {
        "title": "Patient | Portable Patient Monitoring System",
    }
    return render(request, "patient.html", context)