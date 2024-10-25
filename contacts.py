import json

class Contacts:
    def __init__(self, filename = 'contacts.json'):
        self.filename = filename
        self.data = {}
    
    def add_contact(self, id, first_name, last_name):
        if (id in self.data):
            return 'error'
        id:[first_name , last_name]
        #sort
        #write contents
        return([first_name, last_name])

    def modify_contacts(self, id, first_name, last_name):
        if (id == 'dne'):
            return 'error'
        self.data.append(id:[first_name, last_name])

    def delete_contact(self, id)
        if (id =='dne'):
            return 0