vowels:list[str] = ['a','e','i','o','u']

myname:str = "Mateo"

def replaceCharacters(chars:list[str],name:str,replace:str) -> str:
    n = name
    for ch in chars:
        n = n.replace(ch,replace)
    return n
    
print("The name {} is {} characters long.".format(myname,len(myname)))

print(
    "The name {} starts with the '{}' character."
    .format(myname,myname[0])
)

print(
    "the characters from {} to {} of the name {} are: {}"
    .format(2,len(myname),myname,myname[2:len(myname)+1]) #second param is exclusive.
)

print(
    "If the vowels in your name were to be replaced by '{}', you name would be: {}"
    .format('X',replaceCharacters(vowels, myname, 'X'))
)