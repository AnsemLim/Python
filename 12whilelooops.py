# while loop = a statement that will execute it's block of code.
#               as long as it's condition remains true

# infinite loop 
# while 1==1:
#    print("Help: I a'm stuck in a loop!")

name = "" # /name = None

while len(name) == 0: # /while not name:
    name = input("Enter your name: ")

print("Hello " +name)