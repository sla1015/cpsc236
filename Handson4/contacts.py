# -*- coding: utf-8 -*-
"""
Contacts Functions
"""


def listContacts(contactsList):
    num = 1
    for c in contactsList:
        print(num, contactsList[num - 1][0], sep = '. ')
        num += 1
    
def view(contactsList):
    x = int(input("Number: "))
    while x > len(contactsList):
        x = int(input("Invalid number. Try again: "))
    print("Name:", contactsList[x-1][0])
    print("Email:", contactsList[x-1][1])
    print("Phone:", contactsList[x-1][2])

def add(contactsList):
    contact = []
    name = input("Name: ")
    email = input("Email: ")
    number = input("Number: ")
    contact.append(name)
    contact.append(email)
    contact.append(number)
    contactsList.append(contact)
    print(contactsList[-1][0], 'has been added.')

def delete(contactsList):
    x = int(input("Number: "))
    while x > len(contactsList):
        x = int(input("Invalid number. Try again: "))
    print(contactsList[x-1][0], "has been deleted.")
    del contactsList[x-1]
    
    

def displayMenu():
    print("COMMAND MENU")
    print("list - Display all contacts\nview - View a contact",
        "\nadd - Add a contact\ndel - delete a contact\nexit - Exit program")
    
def getCommand(contactsList):
    command = input("\nCommand: ")
    while command != 'exit':
        if command == 'list':
            listContacts(contactsList)
        elif command == 'view':
            view(contactsList)
        elif command == 'add':
            add(contactsList)
        elif command == 'del': 
            delete(contactsList)
        else:
            print("Invalid command. Try again.")
        command = input("\nCommand: ")
    print("Bye!")

def main():
    displayMenu()
    
    getCommand()

if __name__ == "__main__":
    main()