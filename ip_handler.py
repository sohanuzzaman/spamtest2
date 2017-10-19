import ipgetter, subprocess, time, os
import platform


#Change IP function for linux
def change_ip_linux(server):
    #Disconnect previous connection
    subprocess.call("killall openvpn", shell=True)
    time.sleep(10) # <<<< wait a bit more to make sure that the openvpn has been properly disconnected
    command = "openvpn --daemon --config ./UDP/{}".format(server)
    subprocess.call(command, shell=True)
    time.sleep(45) # <<<< wait for connection to be established



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


change_ip("USA.Alabama.Montgomery.UDP.ovpn")