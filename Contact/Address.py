import Person

class Address:
    
    def __init__(self):
        pass
    
    def save(self, name, phone_number, address):
        self.person_list = []
        p = Person.Person(name,phone_number,address)
        self.person_list.append(p)
        
    def findAll(self):
        return self.person_list
    
    def remove(self, name):
        for i, person in enumerate(self.person_list):
            if person.name == name:
                del self.person_list[i]
                
    def test(self):
        print("test!!")
    