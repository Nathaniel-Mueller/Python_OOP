from cell_phone import CellPhone

phone1 = CellPhone("Android")

def ringerOn():
    ringer = ""
    if phone1.is_on_vibrate == True:
        ringer = "off"
    elif phone1.is_on_vibrate == False:
        ringer = "on"
    return ringer
# Contact 1: Mom, Contact 2: Dad, Contact 3: Papa John's Pizza

print("")
print (phone1.contacts)
print ("")
phone1.recieveText(phone1.contacts[1], "Sample text from contact 1: Mom")
print ("")
phone1.recieveText(phone1.contacts[2], "Sample text from contact 2: Dad")
print ("")
print (phone1.messages)
print ("")
phone1.sendText(phone1.contacts[3], "Hello, I'd like to order a large pepperoni pizza please!")
print ("")
phone1.toggleVibrate()
print ("")
print (f"This phone's ringer is {ringerOn()}.")