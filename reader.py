# Reader for iPrint
# Canyon Gargon and Michael Blaisdell
# Version 1.0 3-27-2018
# Import the modules
import requests
import keyboard
import socket
import re
import smtplib

keyboard.send('enter')

cardnumclean = re.compile('^[0-9]+$')

cardnum = ""

# printer IP address
printerip = "10.0.6.221"

# set needed variables for email
smtpServer = "smtp-relay.gmail.com"
subject = "iPrint release agent"
mfrom = "no-reply@francis.edu"
mto = "mblaisdell@francis.edu"


# Get the IP of the raspberry pi
print(socket.getfqdn())
agentip = ((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0])

# contruct the email body with IP addresses
message = "The printer/copier release agent for " + printerip + " running on " + agentip + "  is ready." 

# form the email message
BODY = str.join("\r\n",(
	"From: %s" % mfrom,
	"To: %s" % mto,
	"Subject: %s" % subject,
	"",
	message))

# send the email
server = smtplib.SMTP(smtpServer)
server.sendmail(mfrom, [mto], BODY)
server.quit()

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
