# Reader for iPrint
# Canyon Gargon and Michael Blaisdell

# Import the modules
import requests

cardnum =""
printerip = "10.0.6.221"

while cardnum != "q":
    print()
    print ("-" * 30)
    print ("iPrint Walk-Up printer release console")
    print ("-" * 30)
    # get input from keypad or HID prox reader
    cardnum = input('Swipe card: ')

    # Get the feed
    r = requests.get("https://print.francis.edu/iprint/users/jobs?csn=" + cardnum)
    # check for 200 so get is good
    print (r.status_code)
    print (r)
    print (r.text)

    if r.text == "[]":
       print ("Nothing to print")
       input("Press Enter to continue...")
    else:
       # release the print job to the printer
       s = requests.get("https://print.francis.edu/iprint/users/release?csn=" + cardnum + "&devip=" + printerip)
       print (s.text)
       print (s.status_code)
       print (s)
       
       #test comment
 
       
