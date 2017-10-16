import ipgetter, subprocess, time

original_ip = '52.14.48.000'
current_ip = ipgetter.myip()

def check_ip():
    new_current_ip = ipgetter.myip()
    if not new_current_ip == original_ip and new_current_ip == original_ip:
        result = True
    else:
        result = False
    return result

def change_ip():
    subprocess.call('"c:\Program Files (x86)\HMA! Pro VPN\bin\HMA! Pro VPN.exe" -connect', shell=True)
    subprocess.call('"c:\Program Files (x86)\HMA! Pro VPN\bin\HMA! Pro VPN.exe" -changeip', shell=True)
    time.sleep(5)
    while check_ip() = False:
        time.sleep(7)
        check_ip()