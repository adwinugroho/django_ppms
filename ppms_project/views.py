import bluetooth
import time
from datetime import datetime
from django.shortcuts import render
from raspberry_pi import get_data
from .forms import LoginForm
# from escpos.printer import Usb

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
    # # get from session login
    # bd_addr = "34:81:F4:6B:F1:01"
    # print("mac address: ", bd_addr)
    # port = 6
    # print("port: ", port)
    # sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    # sock.connect((bd_addr, port))
    # jam_file = str(datetime.now().strftime('%Y%m%d_%H%M'))
    # # testing with dummy data
    # suhu = '0'
    # spo = '0'
    # resp = '0'
    # hr = '0'
    # a = sock.recv(1024)
    # jam = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # c = '' 
    # for i in range(len(a)):
    #     c = c + ' ' + str(a[i])
    #     #grab data
    #     index = len(a)
    #     if index is 6:
    #         if a[5] in range (232,238):
    #             resp = str(a[4])
    #     elif index is 8:
    #         suhu = str(a[5]) + '.' + str(a[6])
    #     elif index is 16:
    #         spo = str(a[13])
    #         hr = str(a[14])
        
    #     #cross check data
    #     if float(suhu) < 25 or float(suhu) > 40:
    #         suhu = '0'
        
    #     if float(spo) > 100:
    #         spo = '0'
        
    #     if float(hr) > 100:
    #         hr = '0'
        
    #     if float(resp) > 25:
    #         resp = '0'
    #     print(jam, suhu, spo, hr, resp)
    # # end for
    # # close connection sock
    # sock.close()
    # get_data()
    # init and save to session
    request.session['jam'] = get_data.jam
    request.session['suhu'] = get_data.suhu
    request.session['spo'] = get_data.spo
    request.session['hr'] = get_data.hr
    request.session['resp'] = get_data.resp
    context = {
        "title": "Input data | Portable Patient Monitoring System",
        "jam": jam,
        "suhu": suhu,
        "spo": spo,
        "hr": hr,
        "resp": resp
    }
    return render(request, "input-data.html", context)

def calcAge(strBirthDate):
    b_date = datetime.strptime(strBirthDate, '%d/%m/%Y')
    umur = (datetime.today() - b_date).days/365
    umurStr = str(umur)
    return umurStr
    

def submitMeasurement(request):
    name = request.session['name']
    context = {
        "title": "Input data | Portable Patient Monitoring System",
        "jam": jam,
        "suhu": suhu,
        "spo": spo,
        "hr": hr,
        "resp": resp
    }
    return render(request, "input-data.html", context)

# not yet
def printData(request):
    # get seesion
    name = request.session['name']
    gender = request.session['gender']
    # setting printer
    idVendor = 0x2730
    idProduct = 0x0fff
    inpoint = 0x81
    outpoint = 0x02
    max_length = 32
    # execute print
    #p = Usb(idVendor, idProduct, 0, inpoint, outpoint)
    p = Usb(0x0416, 0x5011, 0, 0x81, 0x03)

    p.text('Nama : ')
    p.text(name)
    p.text('\n')

    p.text('Jenis kelamin : ')
    p.text(gender)
    p.text('\n')

    p.text('Usia : ')
    umur = calcAge(strBirthDate)
    p.text(umurStr[0:2])
    p.text(' Tahun\n')

    p.text('Alamat : ')
    p.text(request["address"])
    p.text('\n')

    p.text('Paramedis : ')
    p.text(request["paramedic"])
    p.text('\n')

    p.text('Ambulance : ')
    p.text(request["ambulance"])
    p.text('\n')

    p.text('Lama di ambulance : ')
    p.text(plat)
    p.text('\n')

    p.text('Data vital pasien : \n')
    p.text('SpO2 : ')
    p.text(str(spo))
    p.text('\n')

    p.text('Heart Rate : ')
    p.text(str(hr))
    p.text('\n')

    p.text('Sys : ')
    p.text(str(sys))
    p.text('\n')

    p.text('DIA : ')
    p.text(str(dia))
    p.text('\n')

    p.text('Resp : ')
    p.text(str(resp))
    p.text('\n')

    p.text('Temp : ')
    p.text(str(temp))
    p.text('\n')

    p.cut()