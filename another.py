class person:

    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def display_info(self):
        return self.name , self.address , self.age
    
person1=person("Abhishek","Janakpur",24)
print(person1.display_info())