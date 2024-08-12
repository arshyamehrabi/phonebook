from phoneBook import phone
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
    print("6- Storage and Retrieval")
    print("---------------------------------")
    choice = input("Enter your choice: ")
    if choice not in ["1","2","3","4","5","6"]:
        print('not valid')
        phonepanel()
    return choice


print(contacts)






