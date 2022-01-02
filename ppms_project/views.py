import bluetooth
import time
import subprocess
from datetime import datetime
from django.shortcuts import render
from raspberry_pi import test_get_data
from .forms import LoginForm, PatientForm, MeasurementForm
from escpos.printer import Usb

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
        # get_port = int(port)
        # print("port: ", get_port)
        # sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
        # sock.connect((macAddress, get_port))
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
    # sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
    # sock.connect((bd_addr, port))
    # sock.close()
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

# old v1
def submitPatient(request):
    # get from session login
    bd_addr = request.session['macAddress']
    print("mac address: ", bd_addr)
    port = int(request.session['port'])
    print("port: ", port)
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM ) 
    sock.connect((bd_addr, port))
    print('Connected to ', bd_addr)
    # init for waktu lama di ambulance
    now = datetime.now()
    nowStr = now.strftime("%Y-%m-%d %H:%M:%S")
    request.session['now_in_patient'] = nowStr
    #define variabel
    suhu = '0'
    spo = '0'
    resp = '0'
    hr = '0'
    while float(suhu) <= 0:
        a = sock.recv(1024)
        # getRecv = request.session["recv"]
        jam = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c = '' 
        for i in range(len(a)):
            c = c + ' ' + str(a[i])
                # f.writelines('\n')
                # f.writelines(jam + ' ' +str(len(a)) +' ' + c)                
        #grab data
        if index is 6:
            if a[5] in range (232,238):
                resp = str(a[4])
        elif index is 8:
            suhu = str(a[5]) + '.' + str(a[6])
        elif index is 16:
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
    else:
        sock.close()
        if request.method == 'POST':
            # save to session
            patientForm = PatientForm(request.POST)
            patient_name = patientForm.data['patient_name']
            address = patientForm.data['address']
            dob = patientForm.data['dob']
            license_number = patientForm.data["license_number"]
            gender = patientForm.data["gender"]
            
            request.session['jam'] = jam
            request.session['suhu'] = suhu
            request.session['spo'] = spo
            request.session['hr'] = hr
            request.session['resp'] = resp
            request.session['patient_name'] = patient_name
            request.session['address'] = address
            request.session['dob'] = dob
            request.session['license_number'] = license_number
            request.session['gender'] = gender
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
    b_date = datetime.strptime(strBirthDate, '%Y-%m-%d')
    umur = (datetime.today() - b_date).days/365
    umurStr = str(umur)
    return umurStr
    

def submitMeasurement(request):
    if request.method == 'POST':
        measurementForm = MeasurementForm(request.POST)
        name = request.session['name']
        patient_name = request.session['patient_name']
        address = request.session['address']
        dob = request.session['dob']
        license_number = request.session['license_number']
        age = calcAge(dob)
        request.session['age'] = age[0:2]
        gender = request.session['gender']
        suhu = request.session['suhu']
        spo = request.session['spo']
        hr = request.session['hr']
        resp = request.session['resp']
        sys = measurementForm.data['systolic']
        dia = measurementForm.data['diastolic']
        request.session['sys'] = sys
        request.session['dia'] = dia
        context = {
            "title": "Print Data | Portable Patient Monitoring System",
            "name": name,
            "ambulance": license_number,
            "patient_name": patient_name,
            "address": address,
            "age": age[0:2],
            "gender": gender,
            "dia": dia,
            "sys": sys,
            "suhu": suhu,
            "spo": spo,
            "hr": hr,
            "resp": resp,
        }
    return render(request, "view-print.html", context)

# not yet
def printData(request):
    # get seesion
    name = request.session['name']
    gender = request.session['gender']
    patient_name = request.session['patient_name']
    address = request.session['address']
    dob = request.session['dob']
    license_number = request.session['license_number']
    gender = request.session['gender']
    suhu = request.session['suhu']
    spo = request.session['spo']
    hr = request.session['hr']
    resp = request.session['resp']
    sys = request.session['sys']
    dia = request.session['dia']
    age = request.session['age']
    time_from_patient = request.session['now_in_patient']
    convTimePatientToTime = datetime.strptime(time_from_patient, '%Y-%m-%d %H:%M:%S')
    now = datetime.now()
    count_time = now - convTimePatientToTime
    # setting printer
    idVendor = 0x2730
    idProduct = 0x0fff
    inpoint = 0x81
    outpoint = 0x02
    max_length = 32
    # execute print
    #p = Usb(idVendor, idProduct, 0, inpoint, outpoint)
    p = Usb(0x0416, 0x5011, 0, 0x81, 0x03)

    p.text('        RUMAH SAKIT UMM')
    p.text('\n')
    p.text('     www.hospital.umm.ac.id')
    p.text('\n')
    p.text('Jl. Raya Tlogomas No. 45 Malang')
    p.text('\n\n')

    jam = datetime.now().strftime('%a %Y-%m-%d %H:%M:%S')
    
    p.text(jam)
    p.text('\n\n')

    p.text('Nama : ')
    p.text(patient_name)
    p.text('\n')

    p.text('Jenis kelamin : ')
    p.text(gender)
    p.text('\n\n')

    p.text('Usia : ')
    # umur = calcAge(dob)
    p.text(age)
    p.text(' Tahun\n')

    p.text('Alamat : ')
    p.text(address)
    p.text('\n\n')

    p.text('Paramedis : ')
    p.text(name)
    p.text('\n')

    p.text('Ambulance : ')
    p.text(license_number)
    p.text('\n')

    p.text('Lama di ambulance : ')
    p.text(str(count_time))
    p.text('\n\n')

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
    p.text(str(suhu))
    p.text('\n')
    p.text('   ~ Pelayananku, pengabdianku ~')
    p.cut()
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