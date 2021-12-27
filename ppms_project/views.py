from django.shortcuts import render
# from raspberry_pi import test_get_data
from .forms import LoginForm
import bluetooth
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
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        name = loginForm.data['username']
        macAddress = loginForm.data['macAddress']
        port = loginForm.data["port"]
        # save to session
        request.session['name'] = name
        request.session['licenseNumber'] = loginForm.data['licenseNumber']
        request.session['macAddress'] = macAddress
        request.session['port'] = port
        context = {
            "title": "Dashboard | Portable Patient Monitoring System",
            "name": name,
            "macAddress": macAddress,
            "port": port
        }
        return render(request, "dashboard.html", context)
    else:
        name = request.session['name']
        macAddress = request.session['macAddress']
        licenseNumber = request.session['licenseNumber']
        port = request.session['port']
        context = {
            "title": "Dashboard | Portable Patient Monitoring System",
            "name": name,
            "macAddress": macAddress,
            "port": port
        }
        return render(request, "dashboard.html", context)

def faq(request):
    # get name from session
    name = request.session['name']
    context = {
        "title": "FAQ | Portable Patient Monitoring System",
        "name": name,
    }
    return render(request, "faq.html", context)

def inputData(request):
    context = {
        "title": "Input data | Portable Patient Monitoring System",
    }
    return render(request, "input-data.html", context)


def patient(request):
    licenseNumber = request.session['licenseNumber']
    context = {
        "title": "Patient | Portable Patient Monitoring System",
        "licenseNumber": licenseNumber,
    }
    return render(request, "patient.html", context)

def submitPatient(request):
    bd_addr = request.session['macAddress']
    print("mac address: ", bd_addr)
    port = int(request.session['port'])
    print("port: ", port)
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((bd_addr, port))
    jam_file = str(datetime.datetime.now().strftime('%Y%m%d_%H%M'))
    suhu = '0'
    spo = '0'
    resp = '0'
    hr = '0'
    a = sock.recv(1024)
    jam = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c = '' 
    for i in range(len(a)):
        c = c + ' ' + str(a[i])
        #grab data
        index = len(a)
        if index == 6:
            if a[5] in range (232,238):
                resp = str(a[4])
        elif index == 8:
            suhu = str(a[5]) + '.' + str(a[6])
        elif index == 16:
            spo = str(a[13])
            hr = str(a[14])
        
        #cross check data
        if float(suhu) < 25 or float(suhu) > 40:
            suhu = '0'
        
        if float(spo) > 100:
            spo = '0'
        
        if float(hr) > 100:
            hr = '0'
        
        if float(resp) > 25:
            resp = '0'
        print(jam, suhu, spo, hr, resp)
    # end for
    sock.close()
    context = {
        "title": "Input data | Portable Patient Monitoring System",
        "jam": jam,
        "suhu": suhu,
        "spo": spo,
        "hr": hr,
        "resp": resp
    }
    return render(request, "input-data.html", context)

def submitMeasurement(request):
    pass

