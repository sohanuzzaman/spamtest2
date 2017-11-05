import subprocess, time, os, platform, ipgetter
from random import randrange
from get_mailids import update_sheet

# determin the frequency of reconnecting internet every 5 -10 times
reconnect_now = randrange(5, 10)

def check_ip():
    myip = ipgetter.myip()
    return myip

# #Change IP function for linux
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


def connect_linux(vpn_server):
    # # Connecting GSM by WVDIAL
    # subprocess.call("nohup wvdial connect &", shell=True)

    # #seeting up pppd(Dial up internet) priority over wifi and ethernet
    # subprocess.call("route del default", shell=True)
    # subprocess.call("route add default gw 10.64.64.64", shell=True)


    # connecting openvpn
    command = "openvpn --daemon --config ovpn/{}".format(vpn_server)
    subprocess.call(command, shell=True)


    # waiting 100 secoends to make sure it is connected
    time.sleep(50)
    update_sheet()


def disconnect_linux():
    subprocess.call("killall openvpn", shell=True)
    # subprocess.call("nohup killall wvdial &", shell=True)
    time.sleep(10)


def connect_win():
    os.system("connect.bat")
    time.sleep(8)


def disconnect_win():
    os.system("disconnect.bat")
    time.sleep(3)


def connect(vpn_server):
    print("Connecting to new internet...")
    if platform.system() == 'Linux':
        print("Linux system ditected")
        connect_linux(vpn_server)
    elif platform.system() == "Windows":
        print("Windows system ditected")
        connect_win()
    else:
        pass
    myip = check_ip()
    print("New assigned IP Address is {}".format(myip))


def disconnect():
    print("Disconnecting vpn.. internet...")
    if platform.system() == 'Linux':
        disconnect_linux()
    elif platform.system() == "Windows":
        disconnect_win()
    else:
        pass


def reconnect(vpn_server):
    if not vpn_server == "same":
        disconnect()
        connect(vpn_server)
    else:
        pass