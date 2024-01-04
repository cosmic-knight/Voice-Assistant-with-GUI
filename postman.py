import socket,os,threading
import pyqrcode,webbrowser

def share(path):
    os.chdir(path)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    address=ip_address+":8000"
    url = pyqrcode.create(address)
    url.png("myqr.png", scale=8)
    webbrowser.open("myqr.png")
    a="python -m http.server"
    try:
        os.system('cmd /c '+a)
    except:
        print()

def start(path):
    try:    
        tim=threading.Thread(target=share, args=[path])
        tim.start()
    except:
        print()