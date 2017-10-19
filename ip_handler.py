import ipgetter, subprocess, time, os
import platform


#Change IP function for linux
def change_ip_linux(server):
    subprocess.call("killall openvpn", shell=True)
    command = "openvpn --daemon --config ./UDP/{}".format(server)
    subprocess.call(command, shell=True)



# changing IP by HMA! pro by running windows batch file
def change_ip(server):
    if platform.system() == 'Linux':
        change_ip_linux(server)
    elif platform.system() == "win32":
        os.system('connect.bat')
        os.system('changeip.bat')
        time.sleep(40)
    else:
        pass
