
"""
n = 0

def increment():
    global n 
    n = n + 1

increment()
increment()
increment()


print n 

"""

"""
n = 0 
def assign(x):
    global n 
    n = x
    
assign(2)
assign(15)
assign(7)

print n 

#why do we get 0 instead of 7
#because in our functions above we never make n global 
#we weren't using n, befre assigning to it 

"""

"""

n = 0 
def decrement():
    global n 
    n = n-1 
x = decrement()



print "x = ", x
print "n = ", n

#we get x= None, what is that?
#we are not returning anything in decrement, and when that happens we get None 
#So if you want to get rid of none you must return something 

"""


#we run this program, it increments numbers, but we do not know what is going on 
#To solve the problem we use print statements 

#It is very useful to use print statements while using the printout the values and labels the values so you know what you are printing out 

"""
import simplegui 

x =0 

def f(n):
    print "f : n, x = ", n, x 
    print "f: result = ", n**x 
    return n**x 

def button_handler():
    global x 
    print "bh : x = ", x
    x += 1
    print "bh : x = ", x
    
def input_handler(text):
    print "ih : text = ", text 
    print f(float(text)) 

frame = simplegui.create_frame("Example", 200, 200)
frame.add_button("Increment", button_handler)
frame.add_input("Number:", input_handler,100)

frame.start() 


"""

#Now the issue of code style 

def f(a,b):
    """Returns True exacty when a is False and b is True"""
    return not a and b 


print f(True, True)
print f(True, False)
print f(False, True)
print f(False, False)

#instead of a == False, instead of b == True: and we get the same input 
"""
# now we remove the conditional and get the same output 
        return True 
    else:
        return False 
"""

print "==="


def f(a,b):
    """Returns True exacty when a is False and b is True"""
    return not (a and b) 


print f(True, True)
print f(True, False)
print f(False, True)
print f(False, False)



