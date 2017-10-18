import ipgetter, subprocess, time, os

# changing IP by HMA! pro by running windows batch file
def change_ip():
    os.system('connect.bat')
    os.system('changeip.bat')
    time.sleep(40)
