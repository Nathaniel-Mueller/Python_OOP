from hashlib import new


class CellPhone:

    def __init__(self, cellModel):
        self.cell_phone_model = cellModel
        self.phone_number = 9182763452
        self.contacts = {
        1 : "Mom",
        2 : "Dad",
        3 : "Papa John's Pizza"
        }
        self.messages = []
        self.is_on_vibrate = False
    
    def toggleVibrate (self):
        
        if self.is_on_vibrate == True:
            self.is_on_vibrate = False
            print ("This phone is no longer on vibrate.")
        elif self.is_on_vibrate == False:
            self.is_on_vibrate = True
            print("This phone is now on vibrate.")
    
    def recieveText(self, contact, newText):
        
        print(f"You recieved a new text from {contact}: {newText}")
        self.messages.append(newText)

    def sendText(self, contact, newText):
        
        print(f"Sending message to {contact}: {newText}")