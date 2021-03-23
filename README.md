# Creating a python project

NOTE: use Virtual environments only if you plan on using external modules, like Django or Flask, which require you to run ``pip install``. If you are not going to use external modules, you can just create a project with the following structure (the same one I used for this project):

```
getting-started-python
│ README.md  
└─── src
			│ someFile.py
			│ anotherFile.py
```
You want to use the "README.md" file to write down a project overview, and the required procedure for someone else to be able to run and use your project.  
______________________

If you want to add external modules to your project, you can do it with [pip](https://pip.pypa.io/en/stable/installing/ "pip").

You can run ``pip install [package_name]`` to add a package to your project.

To set up a virtual environment I followed [this guide](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)

# Python variables

varX:[type] is not type declaration but rather type hinting, there's no type declaration in Python, may want to check Cython if you prefer that.

### numeric types

[int,float,complex]

### sequence types

[list,tuple,range]

### mapping types:

[dict]

### set types:

[set,frozenset]

### boolean types:

[bool]

### Binary types:

[bytes,bytearray,memoryview]

### Text types:

[str]

## Variable with type hinting examples

```python
anInteger:int = 1

aFloat:float = 44.29

alsoAFloat:float = float(44.29)

aString:str = "Hello, World!"
```

A variable can of course be declared without type hinting, however in my personal opinion it's way better to do so, it improves readability and it makes the code look more elegant.

# Arithmetic operators

| Operator | Operation       | Example|
|----------|-----------------|--------|
| +        | Addition        | x+y    |
| -        | Substraction    | x-y    |
| *        | Multiplication  | x*y    |
| /        | Division        | x/y    |
| %        | Modulus         | x%y    |
| **       | Exponentiation  | x**y   |
| //       | Floor division  | x//y   |

# Logical operators

| Operator | Operation                                | Example        |
|----------|------------------------------------------|----------------|
| and      | Checks if both conditions are true      | x < 1 and y > 2 |
| or       | Checks if at least one condition is true | x < 1 or y > 2 |
| not      | Checks if something is false           | not(x > 2 and y) |

# Comparison operators

| Operator | Operation             | Example        |
|----------|-----------------------|----------------|
| ==       | Equal                 | x == y         |
| !=       | Not equal             | x != y         |
| >        | Greater than          | x > y          |
| <        | Less than             | x < y          |
| >=       | Greater than or equal | x >= y         |
| <=       | Less than or equal    | x <= y         |

# Assignment operators

| Operator | Example  | Same As        |
|----------|----------|----------------|
| =	       | x = 5    | x = 5          |
| +=	   | x += 3   | x = x + 3	   |
| -=	   | x -= 3   | x = x - 3	   |
| *=	   | x *= 3   |	x = x * 3	   |	
| /=	   | x /= 3   |	x = x / 3	   |	
| %=	   | x %= 3   |	x = x % 3	   |	
| //=	   | x //= 3  |	x = x // 3	   |	
| **=      | x **= 3  |	x = x ** 3	   |	
| &=	   | x &= 3   | x = x & 3	   |	
| |=	   | x |= 3   | x = x | 3	   |	
| ^=	   | x ^= 3   | x = x ^ 3	   |	
| >>=	   | x >>= 3  | x = x >> 3	   |	
| <<=	   | x <<= 3  |	x = x << 3	   |

# Classes in Python

In case you don't know about Object Oriented Programming, you can check this source to know more about it.

TL;DR:
You can imagine a class as a prototype, that's intended to have certain properties, for example the prototype "Person", could have the following ones:

    Name
    Surname
    Age
    Weight
    Height

But computers don't know what a person is, so you need to define it, with its properties (see the full example in [src/oop.py](http://github.com/system32uwu/getting-started-python/blob/main/src/oop.py "src/oop.py")).

```python
    class Person:
        name:str = ''
        surname:str = ''
        age:int = 0
        height:float = float(0)
        weight:float = float(0)

    def __init__(self,name:str,surname:str,age:int,height:float,weight:float):
        self.name = name
        self.surname = surname 
        self.age = age
        self.height = height
        self.weight = weight
```

Now, what's ```__init__```? Just what you think it is, the constructor of the class, that's the function that gets called whenever you make an instance of a class, like the following:

```python
me = Person("Mateo","Carriquí",18,175.4,53.2)
```

And of course you can now access its properties, and methods:

```python
print(me.name)
print(me.describePerson())
```