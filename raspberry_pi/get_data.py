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

with open('/home/pi/Documents/PPMS/'+jam_file+'.txt', 'a') as f:
    while True:
        a = sock.recv(1024)
        jam = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        c = '' 
        for i in range(len(a)):
            c = c + ' ' + str(a[i])
        f.writelines('\n')
        f.writelines(jam + ' ' +str(len(a)) +' ' + c)
        
        #grab data
        index = len(a)
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
        
sock.close()
f.close()