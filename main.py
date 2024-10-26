from contacts import Contacts

contacts = Contacts()

filename = 'contacts.json'

while True:
    inp1 = input('''
      *** TUFFY TITAN CONTACT MAIN MENU

1. Add contact
2. Modify contact
3. Delete contact
4. Print contact list
5. Set contact filename
6. Exit the program

Enter menu choice: ''')
    if (inp1 == '1') :
        Phone = input('Enter phone number: ')
        First_name = input('Enter first name: ')
        Last_name = input('Enter last name: ')
        add = contacts.add_contact(id=Phone, first_name=First_name, last_name=Last_name)
        if (add == 'error'):
            print('Phone number already exists.\n')
        else:
            print(f'Added: {First_name} {Last_name}.\n')
    if (inp1 == '2') :
        Phone = input('Enter phone number: ')
        First_name = input('Enter first name: ')
        Last_name = input('Enter last name: ')
        modify = contacts.modify_contact(id=Phone, first_name=First_name, last_name=Last_name)
        if modify == 'error':
            print('Phone number does not exist.\n')
        else:
            print(f'Modified: {First_name} {Last_name}.')
    if (inp1 == '3'):
        Phone = input('Enter phone number: ')
        delete = contacts.delete_contact(id=Phone)
        if delete == 'error':
            print('Invalid phone number.')
        else:
            print(f'Deleted: {delete[Phone][0]} {delete[Phone][1]}.')

    if (inp1 == '4') :
        print('''
==================== CONTACT LIST ====================
Last Name             First Name            Phone
====================  ====================  ==========''')
        for id, (first_name, last_name) in contacts.data.items():
            print(f"{last_name:22} {first_name:20} {id}")
    
    if (inp1 == '5') :
        filename = input('Enter File Name: ')
    if (inp1 == '6') :
        break