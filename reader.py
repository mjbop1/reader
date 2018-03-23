# Reader for iPrint
# Canyon Gargon and Michael Blaisdell
# Version 1.0
# Import the modules
import requests
import keyboard
import socket
import re

keyboard.send('enter,enter')

cardnumclean = re.compile('^[0-9]+$')

cardnum = ""

# printer IP address
printerip = "10.0.6.221"

print(socket.getfqdn())
print((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0])

while cardnum != "0000":
    print()
    print ("-" * 30)
    print ("iPrint Walk-Up printer release console")
    print ("-" * 30)
    # get input from keypad or HID prox reader
    cardnum = input()
    print (cardnum)
    # Get the feed
    r = requests.get("https://print.francis.edu/iprint/users/jobs?csn=" + cardnum)
    # check for 200 so get is good
    print (r.status_code)
    print (r)
    print (r.text)

    if r.text == "[]":
       print ("Nothing to print")
       #input("Press Enter to continue...")
    else:
       # release the print job to the printer
       s = requests.get("https://print.francis.edu/iprint/users/release?csn=" + cardnum + "&devip=" + printerip)
       print (s.text)
       print (s.status_code)
       print (s)

       #test comment
