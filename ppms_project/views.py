from django.shortcuts import render
from raspberry_pi import get_data
from .forms import LoginForm
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
    loginForm = LoginForm(request.POST or None)
    # loginForm = LoginForm(request)
    getName = ""
    getAddress = ""
    getPort = ""
    if request.method == 'POST':
        name = loginForm.data['username']
        # print("get name:", name)
        macAddress = loginForm.data['macAddress']
        port = loginForm.data['port']
        getName = name
        getAddress = macAddress
        getPort = port
    request.session['name'] = getName
    context = {
        "title": "Login | Portable Patient Monitoring System",
        "name": getName,
        "macAddress": getAddress,
        "port": getPort
    }
    return render(request, "dashboard.html", context)

def faq(request):
    # get name from session
    name = request.session['name']
    context = {
        "title": "FAQ | Portable Patient Monitoring System",
        "name": name
    }
    return render(request, "faq.html", context)

def inputData(request):
    context = {
        "title": "Input data | Portable Patient Monitoring System",
    }
    return render(request, "input-data.html", context)


def patient(request):

    context = {
        "title": "Patient | Portable Patient Monitoring System",
    }
    return render(request, "patient.html", context)