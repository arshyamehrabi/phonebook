import re
import csv

class Phone:

    def __init__(self,name,phoneNumber,email):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email

    
    def add_contact(self,contacts):
        if len(contacts) != 0:
            for contact in contacts:
                if contact['Number'] == self.phoneNumber or contact['Email'] == self.email:
                    print('Duplicate entry')
                    print("---------------------------------")
                    return
        
        if not re.match(r'^[a-zA-Z\s]+$', self.name):
            print('name is not correct')
            print("---------------------------------")
            return
        if not re.match(r'^\d{11}$', self.phoneNumber):
            print('number is not correct')
            print("---------------------------------")
            return
        if not re.match(r'[^@]+@[^@]+\.[^@]+', self.email):
            print('email is not correct')
            print("---------------------------------")
            return
        contacts.append({'Name': self.name, 'Number': self.phoneNumber, 'Email': self.email})
        print('Contact added')
        print("---------------------------------")

    

    




       



