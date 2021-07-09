def functionTest(num, division):
    if num % division == 0: #If the number is a multiple of the value of division
        #it returns true, else False is returned
        return True
    else:
        return False

for i in range(1,101):
    value = ""
    
    #No need to check for a multiple of 3 and 5 as it will pass both tests and be concatenated as one string as "FizzBuzz"
    
    if functionTest(i,3) == True:
        value += "Fizz"
    
    if functionTest(i,5) == True:
        value += "Buzz"
    
    if value == "": #Rather than checking if it is not a multiple, checking the string is an easier way to do the same thing
        value = i
    
    print(value)
