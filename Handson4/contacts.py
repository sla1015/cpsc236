# -*- coding: utf-8 -*-
"""
Contacts Functions
"""
contactsList = [['Pansy Greenhill', 'pansy@greenhill.com', '555-347-2367'], 
                ['Cora Baggins', 'cora@bagend.com', '555-456-2967']]

def listContacts():
    num = 1
    for c in contactsList:
        print(num, contactsList[num - 1][0], sep = '. ')
        num += 1
    
def view():
    x = int(input("Number: "))
    while x > len(contactsList):
        x = int(input("Invalid number. Try again: "))
    print("Name:", contactsList[x-1][0])
    print("Email:", contactsList[x-1][1])
    print("Phone:", contactsList[x-1][2])

def add():
    contact = []
    name = input("Name: ")
    email = input("Email: ")
    number = input("Number: ")
    contact.append(name)
    contact.append(email)
    contact.append(number)
    contactsList.append(contact)
    print(contactsList[-1][0], 'has been added.')

def delete():
    x = int(input("Number: "))
    while x > len(contactsList):
        x = int(input("Invalid number. Try again: "))
    print(contactsList[x-1][0], "has been deleted.")
    del contactsList[x-1]
    
    

def displayMenu():
    print("COMMAND MENU")
    print("list - Display all contacts\nview - View a contact",
        "\nadd - Add a contact\ndel - delete a contact\nexit - Exit program")
    
def getCommand():
    command = input("\nCommand: ")
    while command != 'exit':
        if command == 'list':
            listContacts()
        elif command == 'view':
            view()
        elif command == 'add':
            add()
        elif command == 'del': 
            delete()
        else:
            print("Invalid command. Try again.")
        command = input("\nCommand: ")
    print("Bye!")

def main():
    displayMenu()
    
    getCommand()

if __name__ == "__main__":
    main()