import json

class Contacts:
    def __init__(self, filename = 'contacts.json'):
        self.filename = filename
        self.data = {}
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except:
            pass
    
    def add_contact(self, id, first_name, last_name):
        if (id in self.data):
            return 'error'
        self.data[id] = [first_name , last_name]
        #sort
        self.data = dict(sorted(self.data.items(), key= lambda item: (item[1][1].lower(), item[1][0].lower())))
        #write contents
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
        return{id:[first_name,last_name]}

    def modify_contact(self, id, first_name, last_name):
        if id not in self.data:
            return 'error'
        self.data[id] = [first_name,last_name]
        self.data = dict(sorted(self.data.items(), key= lambda item: (item[1][1].lower(), item[1][0].lower())))
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
        return{id:[first_name,last_name]}

    def delete_contact(self, id):
        if (id not in self.data):
            return 'error'
        delete = {id:self.data.pop(id)}
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
            return delete

        