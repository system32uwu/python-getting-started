# ---IMPORTS
from datetime import date #yyyy-mm-dd format

# ---FUNCTIONS
def check(value, compare) -> str:
    xIsValue:str = "{} is equal to {}."
    # ternary operator (inline conditional statements)
    message:str = xIsValue.format(value, compare)
    return message if value == compare else message.replace("is", "is not") 

def getAge(dateBorn:date) -> int:
    today = date.today()
    return today.year - dateBorn.year - ((today.month, dateBorn.day) < (dateBorn.month,dateBorn.day))

def canDrink(age:int) -> bool:
    return True if age >= 18 else False

# ---DECLARATIONS
x:int = 1
y:int = 1

# a clear way to declare a float variable
usdValueInUyu:float = float(44.29)
# usdValueInUyu = 44.29 would also work but I prefer knowing the type beforehand 

born:date = date(2002,10,24)

age:int = getAge(born)

canDrinkMessage:str = "You are over 18, so you can drink."

# ---EXAMPLES
print(check(x, y))

print(
        "The value of a dollar in uruguayan pesos is equal to: {} UYU"
        .format(usdValueInUyu)
)

print(
    "If you were born in: {}, then your age is: {}"
    .format(born,age)
)

print(canDrinkMessage) if canDrink(age) else print(
    canDrinkMessage
    .replace("over","below")
    .replace("can","can't")
    )