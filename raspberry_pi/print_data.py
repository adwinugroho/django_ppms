from datetime import datetime
from escpos.printer import Usb

#setting printer
idVendor = 0x2730
idProduct = 0x0fff
inpoint = 0x81
outpoint = 0x02
max_length = 32

def calcAge(strBirthDate):
    b_date = datetime.strptime(strBirthDate, '%d/%m/%Y')
    return (datetime.today() - b_date).days/365
umur = calcAge(strBirthDate)
umurStr = str(umur)

def execPrint(request):
    #p = Usb(idVendor, idProduct, 0, inpoint, outpoint)
    p = Usb(0x0416, 0x5011, 0, 0x81, 0x03)

    p.text('Nama : ')
    p.text(request["name"])
    p.text('\n')

    p.text('Jenis kelamin : ')
    p.text(request["gender"])
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