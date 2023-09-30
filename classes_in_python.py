
# define a class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print ('Woof!')    

# Main

# instantiate an object from the class
my_dog = Dog('Spot', 'Shepard')       
print (my_dog.name)
print (my_dog.breed) 
my_dog.bark()
