import csv
import re

contact_name = []
contact_number = []
contact_email = []

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
    contact_number.append(phoneNumber)
    contact_email.append(email)
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
                        if new_number in contact_number: 
                            print('Duplicate entry')
                            print("---------------------------------")
                            return
                        if not re.match(r'^\d{11}$', new_number):
                            print('number is not correct')
                            print("---------------------------------")
                            return
                        else:
                            contact_number.remove(contact['Number'])
                            contact['Number'] = new_number
                            contact_number.append(new_number)
                            print('Changes were made')
                            print("---------------------------------")
                            return
            
            elif option == 'email':
                for contact in contacts:
                    if contact['Name'] == edit_name:
                        new_email = input('Enter new email: ')
                        if new_email in contact_email: 
                            print('Duplicate entry')
                            print("---------------------------------")
                            return
                        if not re.match(r'[^@]+@[^@]+\.[^@]+', new_email):
                            print('email is not correct')
                            print("---------------------------------")
                            return
                        else:
                            contact_email.remove(contact['Email'])
                            contact['Email'] = new_email
                            contact_email.append(new_email)
                            print('Changes were made')
                            print("---------------------------------")
                            return
                        
def del_contact(name,contacts):
    if name not in contact_name:
        print('name does not exist')
    else:
        for contact in contacts:
            if contact['Name'] == name:
                contact_number.remove(contact['Number'])
                contact_email.remove(contact['Email'])
                contacts.remove(contact)
                contact_name.remove(name)
                break

                 
def contact_info(contacts):
    if len(contacts) != 0:
        header = contacts[0].keys()
        row = "{:<15}"*len(header)
        print(row.format(*header))
        print("-------------------------------------------------------")
        for contact in contacts:
            print(row.format(*contact.values()))
        print("-------------------------------------------------------")
    else:
        print("There is no contact")
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
        edit_contact(contacts)
        phonepanel()

    if choice == '3':
        del_name = input('Enter name to delete: ')
        del_contact(del_name,contacts)
        phonepanel()

    if choice == '4':
        contact_info(contacts)
        phonepanel()
    



print(contacts)



    

    




       



