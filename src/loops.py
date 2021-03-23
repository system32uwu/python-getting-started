numbers:int = 10
count:int = numbers

message:str = "Hello, World!"

for char in message:
    print(char)

for i in range(len(message)):
    print("Index: {} - Value: {}".format(i,message[i]))

#you can also start from X (4), and specify a step (3)
for i in range(4,len(message),3):
    print("Index: {} - Value: {}".format(i,message[i]))

while count >= 0:
    print("I'm counting from {} to {}. Currently at: {}".format(numbers,0,count))
    count -= 1

while True:
    print("This guy can come handy, use at your own risk though. I'm breaking out now!")
    break