# convert xx.yy to xx dollars and yy cents
def convert(val):
    dollars = int(val)
    cents = int(100 * (val - dollars))
    return str(dollars) + " dollars and " + str(cents) + " cents"

#common error 

# Tests
print convert(11.23)
print convert(11.20) #this prints 11 dollars and 19 cents
print convert(1.12) # here it is 1 dollars instead of dollar 
print convert(12.01)  
print convert(1.01)
print convert(0.01)
print convert(1.00)
print convert(0)
print convert(-1.40)
print convert(12.55555)

# test your program with multiple inputs 
