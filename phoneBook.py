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
    print('Contact added')
    print("---------------------------------")


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
            phone.edit_contact(contacts)
            phonepanel()

    if choice == '6':
        break



print(contacts)



    

    




       



