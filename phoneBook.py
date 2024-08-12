import re
import csv

class Phone:

    global contact_name
    contact_name = []
    global contact_numner
    contact_numner = []

    def __init__(self,name,phoneNumber,email):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email

    
    def add_contact(self,contacts):
        
        print(contact_name)
        if len(contacts) != 0:
            if self.name in contact_name: 
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
        contact_name.append(self.name)
        print('Contact added')
        print("---------------------------------")
    

    def edit_contact(self,contacts):
        edit_name = input('Enter name to edit: ')
        if edit_name not in contact_name:
            print('entry does not exist')
            print("---------------------------------")
            return
        else:
            option = input('Which option do you want to edit (name/number/email): ')
            if option not in ['name','number','email']:
                print('entry is wrong')
                print("---------------------------------")
                return
            else:
                if option == 'name':
                    for contact in contacts:
                        if contact['Name'] == edit_name:
                            new_name = input('Enter new name: ')
                            if not re.match(r'^[a-zA-Z\s]+$', new_name):
                                print('name is not correct')
                                print("---------------------------------")
                                return
                            else:
                                contact['Name'] = new_name
                                contact_name.remove(edit_name)
                                contact_name.append(new_name)
                                print('Changes were made')
                                print("---------------------------------")
                                return
                
                elif option == 'number':
                    for contact in contacts:
                        if contact['Name'] == edit_name:
                            new_number = input('Enter new number: ')






            



    

    




       



