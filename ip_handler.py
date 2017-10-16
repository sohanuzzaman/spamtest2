import ipgetter, subprocess, time, os

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
    os.system('connect.bat')
    os.system('changeip.bat')
    time.sleep(5)
    ip_changed = check_ip()
    while ip_changed == False:
        time.sleep(7)
        ip_changed = check_ip()