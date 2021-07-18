#logical operators (and,or,not) = used to check if two or more conditional statement

temp = int(input("What is the temperature outside?: "))

#logical operators of 'and' is both must be the correct 
if temp >= 0 and temp <= 30:
    print("the temperature is good today!")
    print("go outside!")
    #logical operators of 'or' need either one of correct 
    elif temp < 0 or temp >30:
        print("the temperature is bad today!")
        print("stay inside!")

#logical operators of 'not' is reverse of true 
#if not(temp >= 0 and temp <= 30):
#        print("the temperature is bad today!")
#        print("stay inside!")
#    elif not(temp < 0 or temp >30):  
#        print("the temperature is good today!")
#        print("go outside!") 