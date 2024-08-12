import csv
import re

contact_name = []
contact_numner = []
contact_gmail = []

def phonepanel():
    print("1- Add Contact")
    print("2- Edit Contact")
    print("3- Delete Contatct")
    print("4- Contacts")
    print("5- Sort Contacts")
    print("6- Storage")
    print("---------------------------------")
    global choice
    choice = input("Enter your choice: ")
    if choice not in ["1","2","3","4","5","6"]:
        print('not valid')
        phonepanel()
    return choice


def add_contact(name,phoneNumber,email,contacts):
    print(contact_name)
    if len(contacts) != 0:
        if name in contact_name: 
            print('Duplicate entry')
            print("---------------------------------")
            return
    
    if not re.match(r'^[a-zA-Z\s]+$', name):
        print('name is not correct')
        print("---------------------------------")
        return
    if not re.match(r'^\d{11}$', phoneNumber):
        print('number is not correct')
        print("---------------------------------")
        return
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        print('email is not correct')
        print("---------------------------------")
        return
    contacts.append({'Name': name, 'Number': phoneNumber, 'Email': email})
    contact_name.append(name)
    contact_numner.append(phoneNumber)
    contact_gmail.append(email)
    print('Contact added')
    print("---------------------------------")


def edit_contact(contacts):
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
                        if new_name in contact_name: 
                            print('Duplicate entry')
                            print("---------------------------------")
                            return
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
                        pass


file = open('contact.csv',newline='')
data = csv.DictReader(file)
contacts = list(data)
phonepanel()
while True:
    if choice == '1':
        print('Enter the information')
        name = input('Enter name: ')
        phoneNumber = input('Enter phoneNumber: ')
        email = input('Enter email: ')
        add_contact(name,phoneNumber,email,contacts)
        phonepanel()

    if choice == '2':
            edit_contact(contacts)
            phonepanel()

    if choice == '6':
        break



print(contacts)



    

    




       



