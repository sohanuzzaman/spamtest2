import subprocess, time, os
import ipgetter
#import platform

def check_ip():
    myip = ipgetter.myip()
    return myip

def disconnect_windows():
    os.system("disconnect.bat")
def connect_windows():
    os.system("connect.bat")

def disconnect_linux():
    pass

def connect_linux():
    pass

def disconnect():
    if platform.system() == 'Linux':
        disconnect_linux()
    else:
        disconnect_windows()
    time.sleep(4)

def connect():
    if platform.system() == 'Linux':
        connect_linux()
    else:
        connect_windows()
    time.sleep(9)
    ip = check_ip()
    print ("The new ip address is {}".format(ip))




#Change IP function for linux
# def change_ip(vpn_server):
#     print("initializing changing IP address...")
#     #Disconnect previous connection
#     subprocess.call("sudo killall openvpn", shell=True)
#     print("disconnecting previous server...")
#     time.sleep(7) # <<<< wait a bit more to make sure that the openvpn has been properly disconnected
#     print("connecting to new server...")
#     command = "sudo openvpn ./UDP/{}".format(vpn_server)
#     subprocess.call(command, shell=True)
#     print("waiting to be sure connecting openvpn...")
#     time.sleep(30) # <<<< wait for connection to be established
#     myip = check_ip()
#     print(myip)
#     return myip


#change_ip("USA.Alabama.Montgomery.UDP.ovpn")
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