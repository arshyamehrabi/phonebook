import csv
import re

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
        for contact in contacts:
            if contact['Name'] == name or contact['Number'] == phoneNumber: 
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
    print('Contact added')
    print("---------------------------------")


def edit_contact(contacts):
    edit_name = input('Enter name to edit: ')
    for contact in contacts:
        if contact['Name'] == edit_name:
            option = input('Which option do you want to edit (name/number/email): ')
            if option not in ['name','number','email']:
                print('entry is wrong')
                print("---------------------------------")
                return
            else:
                if option == 'name':
                    new_name = input('Enter new name: ')
                    for cont in contacts:
                        if cont['Name'] == new_name:
                            print('Duplicate entry')
                            print("---------------------------------")
                            return
                    if not re.match(r'^[a-zA-Z\s]+$', new_name):
                        print('name is not correct')
                        print("---------------------------------")
                        return
                    else:
                        contact['Name'] = new_name
                        print('Changes were made')
                        print("---------------------------------")
                        return
                
                elif option == 'number':
                    new_number = input('Enter new number: ')
                    for cont2 in contacts:
                        if cont2['Number'] == new_number: 
                            print('Duplicate entry')
                            print("---------------------------------")
                            return
                    if not re.match(r'^\d{11}$', new_number):
                        print('number is not correct')
                        print("---------------------------------")
                        return
                    else:
                        contact['Number'] = new_number
                        print('Changes were made')
                        print("---------------------------------")
                        return
                
                elif option == 'email':
                    new_email = input('Enter new email: ')
                    for cont3 in contacts:
                        if cont3['Email'] == new_email:
                            print('Duplicate entry')
                            print("---------------------------------")
                            return
                    if not re.match(r'[^@]+@[^@]+\.[^@]+', new_email):
                        print('email is not correct')
                        print("---------------------------------")
                        return
                    else:
                        contact['Email'] = new_email
                        print('Changes were made')
                        print("---------------------------------")
                        return
    print('entry does not exist')
    print("---------------------------------")
    return 

                        
def del_contact(name,contacts):
    for contact in contacts:
        if contact['Name'] == name:
            contacts.remove(contact)
        else:
            print('name does not exist')
            
                 
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


def sort_contact(contacts):
    sort_contacts = sorted(contacts, key=lambda contact: contact['Name'])
    print('contacts were sorted')
    print("---------------------------------")
    return sort_contacts


def storage(contacts):
    file = open("contact.csv", "w", newline="")
    writer = csv.DictWriter(file, ['Name','Number','Email'])
    writer.writeheader()
    writer.writerows(contacts)
    file.close()
             
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

    elif choice == '2':
        edit_contact(contacts)
        phonepanel()

    elif choice == '3':
        del_name = input('Enter name to delete: ')
        del_contact(del_name,contacts)
        phonepanel()

    elif choice == '4':
        contact_info(contacts)
        phonepanel()
    
    elif choice == '5':
        if len(contacts) != 0:
            contacts = sort_contact(contacts)
        else:
            print('there are not any contact')
            print("---------------------------------")
        phonepanel()

    else:
        storage(contacts)
        break




    

    




       



