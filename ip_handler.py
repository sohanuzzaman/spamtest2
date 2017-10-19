import subprocess, time, os
import ipgetter
#import platform

def check_ip():
    myip = ipgetter.myip()
    return myip

#Change IP function for linux
def change_ip(vpn_server):
    print("initializing changing IP address...")
    #Disconnect previous connection
    subprocess.call("sudo killall openvpn", shell=True)
    print("disconnecting previous server...")
    time.sleep(10) # <<<< wait a bit more to make sure that the openvpn has been properly disconnected
    print("connecting to new server...")
    vpn = str(vpn_server)
    command = "sudo openvpn --daemon --config ./UDP/{}".format(vpn)
    subprocess.call(command, shell=True)
    print("waiting to be sure connecting openvpn...")
    time.sleep(45) # <<<< wait for connection to be established
    myip = check_ip()
    print(myip)
    return myip


change_ip("USA.Alabama.Montgomery.UDP.ovpn")
# changing IP by HMA! pro by running windows batch file
# def change_ip(vpn_server):
#     if platform.system() == 'Linux':
#         change_ip_linux(vpn_server)
#     elif platform.system() == "win32":
#         os.system('connect.bat')
#         os.system('changeip.bat')
#         time.sleep(40)
#     else:
#         pass
#     myip = check_ip()
#     return myip