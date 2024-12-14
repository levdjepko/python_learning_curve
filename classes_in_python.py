#  Definition of a Class
class Dog:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color
    def bark(self):
        print ('Woof!')    

#  instantiate an object from the class
my_dog = Dog('Spot', 'Shepard', 'Brown')       
print(my_dog.name)
print(my_dog.breed) 
print(my_dog.color)
my_dog.bark()
