import ipgetter, subprocess, time, os
from sys import platform

# changing IP by HMA! pro by running windows batch file
def change_ip():
    if platform == "win32":
        os.system('connect.bat')
        os.system('changeip.bat')
        time.sleep(40)
    else:
        pass
