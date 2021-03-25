def myFunction():
    print("Hello, World!")

myFunction()

def aFunctionWithParameters(name:str):
    print("Hello, {}.".format(name))

aFunctionWithParameters("Mateo")

def aFunctionThatReturnsSomething(name:str) -> str:
    return "Hello {}".format(name)

print(aFunctionThatReturnsSomething("Mateo"))
