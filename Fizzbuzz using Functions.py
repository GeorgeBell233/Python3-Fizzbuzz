def functionTest(num, division):
    if num % division == 0: #If the number is a multiple of the value of division
        #it returns true, else False is returned
        return True
    else:
        return False

for i in range(1,101):
    value = ""
    
    if functionTest(i,3) == True:
        value += "Fizz"
    
    if functionTest(i,5) == True:
        value += "Buzz"
    
    if value == "":
        value=i
    
    print(value)
