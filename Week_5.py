#Question 1
#definnig a class on different methods of food preservation based on food type
#parent class
class Preservation():
    def __init__(self, PMethod, Foodtype, sideEffects):
        #attributes (facts about food preservation)
        self.PMethod = PMethod 
        self.Foodtype = Foodtype
        self.__sideEffects = sideEffects #encapsulation
        
    #methods (Various ways of preserving foods )
    def FPreserve(self):
        print(f"{self.Foodtype} can be best preserved by {self.PMethod}")

    #method 2 (How long the food will last due to preservation)
    def sLife(self):
        print(f"{self.PMethod} is guaranteed to extend the shelf life of {self.Foodtype} for at least 3 months")
    
    
    #accessing encapsulated object
    def get_side_effects(self):
            return self.__sideEffects

    # modifying encapsulated object safely
    def set_side_effects(self, new_effect):
        self.__sideEffects = new_effect

    
# Subclass 1 (override sLife)
class Refrigeration(Preservation):
    def sLife(self):
        print(f"{self.Foodtype} preserved by refrigeration lasts 1-3 weeks, depending on temperature")


# Subclass 2
class Smoking(Preservation):
    def sLife(self):
        print(f"{self.Foodtype} preserved by smoking can last several months but may introduce nitrates")

    
#Creating object
f1 = Refrigeration('Refrigeration', 'Fruits', 'Chilling Injury')
f2 = Preservation('Vacuum storage', 'Grains', 'Requires high capital')
f3 = Preservation('Dry Storage', 'Grains', 'Risk of mold')
f4 = Smoking('Curing and Smoking', 'Fish and Poultry', 'Introduces nitrates')

#using methods
f1.FPreserve()
f2.FPreserve()
f3.sLife()
f4.sLife


# accessing private attribute through encapsulation
print(f"The side effect of {f1.PMethod} for {f1.Foodtype} is: {f1.get_side_effects()}")

# modifying side effect safely
f2.set_side_effects("Needs expensive equipment")
print(f"Updated side effect of {f2.PMethod}: {f2.get_side_effects()}")


#Question 2
#parent class(blueprint)
class Animal():
    def action(self):
        print('Animal makes a sound') #base methond

#subclass one
class Cat(Animal): #inherits from parent class
    def action(self): # overrides parent with its own method
        print('Cat Meows')

class Dog(Animal):
    def action(self):
        print('Dog barks')


animals = [Dog(), Cat(), Animal()] #One list holding the different types of objects.
for a in animals:                  #Iterate through each object…
    a.action()                     #call the same method name, action().


        