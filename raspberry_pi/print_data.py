from datetime import date
import datetime
from escpos.printer import Usb

#setting printer
idVendor = 0x2730
idProduct = 0x0fff
inpoint = 0x81
outpoint = 0x02
max_length = 32

#dummy pasien
pasien = 'Bedjo Kusumo'
jk = 'laki - laki'
alamat = 'Jl Kalindeso 30A Pasuruan'
#lahir = 

#dummy paramedis
paramedis = 'Themon'
plat = 'N 1920 ABC'

#dummy data
spo = 98
hr = 100
sys = 110
dia = 150
resp = 10
temp = 37.5

# ga kepake
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d-%m-%Y')
    except ValueError:
        raise ValueError("Incorrect data format, should be DD-MM-YYYY")


# buat fungsi get age
born = datetime.datetime (1958,5,13)
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

#connect to printer
#p = Usb(idVendor, idProduct, 0, inpoint, outpoint)
p = Usb(0x0416, 0x5011, 0, 0x81, 0x03)

p.text('Nama : ')
p.text(pasien)
p.text('\n')

p.text('Jenis kelamin : ')
p.text(jk)
p.text('\n')

p.text('Usia : ')
umur = calculate_age(born)
p.text(str(umur))
p.text(' Tahun\n')

p.text('Alamat : ')
p.text(alamat)
p.text('\n')

p.text('Paramedis : ')
p.text(paramedis)
p.text('\n')

p.text('Ambulance : ')
p.text(plat)
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