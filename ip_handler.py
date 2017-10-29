import subprocess, time, os, platform, ipgetter


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


def connect_linux():
    subprocess.call("nohup wvdial connect &", shell=True)


def disconnect_linux():
    subprocess.call("nohup killall wvdial &", shell=True)


def connect_win():
    os.system("connect.bat")
    time.sleep(8)


def disconnect_win():
    os.system("disconnect.bat")
    time.sleep(3)


def connect():
    print("Connecting GP internet...")
    if platform.system() == 'Linux':
        print("Linux system ditected")
        connect_linux()
    elif platform.system() == "Windows":
        print("Windows system ditected")
        connect_win()
    else:
        pass
    myip = check_ip()
    print("New assigned IP Address is {}".format(myip))


def disconnect():
    print("Disconnecting GP internet...")
    if platform.system() == 'Linux':
        disconnect_linux()
    elif platform.system() == "Windows":
        disconnect_win()
    else:
        pass


def reconnect():
    disconnect()
    connect()