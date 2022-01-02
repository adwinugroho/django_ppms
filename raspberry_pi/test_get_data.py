import bluetooth
import time
import datetime
import os.path

# sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
# sock.close()
lines = []
isExist = os.path.exists('/home/pi/Documents/PPMS/py3/django_ppms/raspberry_pi/file_login.txt')
if isExist == True:
    with open('/home/pi/Documents/PPMS/py3/django_ppms/raspberry_pi/file_login.txt', 'r') as fl:
        lines = fl.readlines()

print('Check login file: ', lines)
if len(lines) >= 2:
    print('Check br address from login file: ', lines[0])    
    print('Check port from login file: ', lines[1])

    intPort = int(lines[1])
    bd_addr = lines[0]
    port = intPort
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((bd_addr, port))
    jam_file = str(datetime.datetime.now().strftime('%Y%m%d_%H%M'))
    print('Connected to ', bd_addr)

    #define variabel
    suhu = '0'
    spo = '0'
    resp = '0'
    hr = '0'
    cek = True

    with open('/home/pi/Documents/PPMS/py3/django_ppms/raspberry_pi/data_from_pi.txt', 'w') as f:
        while cek is True:
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