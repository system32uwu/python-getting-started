from datetime import date

class Person:
    #declare props / attributes
    name:str = ''
    surname:str = ''
    age:int = 0
    height:float = float(0)
    weight:float = float(0)

    # example of a constructor 
    def __init__(self,name:str,surname:str,age:int,height:float,weight:float):
        self.name = name
        self.surname = surname 
        self.age = age
        self.height = height
        self.weight = weight
    
    def describePerson(self) -> str:
        if len(self.name) < 1:
            return "Please input data in order to describe this object."
        
        # you can write a multiline string / comment using """
        descriptionMessage = """
        Hello fellow human, I'm an instance of the class {}.
        My full name is {} {}.
        I'm {} years old.
        I'm {}cm tall.
        I weigh {}kg.""".replace(8*" ","") # You'll understand what this does if you remove .replace(...), in short terms it removes the 8 trailing whitespaces of each line in that string.

        return descriptionMessage.format(
            type(self).__name__,
            self.name,self.surname,
            self.age,
            self.height,
            self.weight
            )

    def bark(self) -> str:
        return "I'm not your dog, be a good human and go pet him."

    def getOlder(self) -> str:
        yearBorn:int = date.today().year - self.age

        if self.age + 1 > 100:
            return "RIP {} {}, {} - {}".format(self.name,self.surname, yearBorn, date.today().year)
        else:
            self.age += 1
            return "I'm {} years old".format(self.age)

    def learnPython(self) -> str:
        return "That's what you should be doing human, I can understand this language perfectly thanks to its interpreter, now stop fooling around and head to https://docs.python.org/3/ to keep learning!"
            
me = Person("Mateo","Carriquí",18,175.4,53.2)

print(me.describePerson())

print(me.getOlder())

print(me.bark())

print(me.learnPython())