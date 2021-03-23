# --- IMPORTS
from datetime import date

# --- DECLARATIONS
today: date = date.today()

# --- FUNCTIONS

"""This function greets you :D"""


def greet(name: str) -> str:
    message: str = "Hello {}."
    return message.format(name)


print(
    greet("Mateo") + "\nToday's date is: {}"
    .format(today)
    .replace("-", "/")
)
