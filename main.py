from phoneBook import Phone
import csv




file = open('contact.csv',newline='')
data = csv.DictReader(file)
contacts = list(data)


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


phonepanel()
while True:
    if choice == '1':
        print('Enter the information')
        name = input('Enter name: ')
        phoneNumber = input('Enter phoneNumber: ')
        email = input('Enter email: ')
        phone = Phone(name,phoneNumber,email)
        phone.add_contact(contacts)
        phonepanel()

    if choice == '2':
            phone.edit_contact(contacts)



print(contacts)