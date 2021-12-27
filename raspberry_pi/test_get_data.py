import bluetooth
import time
import datetime

# address & port will be inputs by staff
bd_addr = "34:81:F4:6B:F1:01"
port = 6
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
jam_file = str(datetime.datetime.now().strftime('%Y%m%d_%H%M'))
print('Connected to ', bd_addr)

#define variabel
suhu = '0'
spo = '0'
resp = '0'
hr = '0'

