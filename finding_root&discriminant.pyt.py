"""found this online""" 


# Compute the smaller root of a quadratic equation.

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.
import math 

def disciminant(a,b,c):
    """program to find discriminant"""
    d = (b**2.0) - (4.0*a*c)
    return d

print disciminant(1,7,10) #since result is positive there are two solutios 


def findroots(a,b,c):
    """This function finds roots of numbers"""
    dis_form = b*b -4*a*c 
    sqrt_val = math.sqrt(abs(dis_form))
    
    if dis_form>0:
        print("real and different roots")
        print (-b + sqrt_val)/(2*a)
        print(-b - sqrt_val)/ (2*a)
        
    elif dis_form ==0:
        print("real and same roots")
        print(-b/2*a)
        
    else:
        print "Complex Roots"
        print (-b/(2*a)), "+i", sqrt_val
        print (-b/(2*a)), "-i", sqrt_val
    
    
    
    
a = int(input('Enter a:'))
b = int(input ('Enter b:'))
c = int (input ('Enter c:'))   
    
    #if a is 0, then incorrect equation 
    
if a ==0:
    print("Input correct quadritic equation")
else:
    findroots(a,b,c)
    
    
    

    
 
  



findroots(7,5,2)
    



