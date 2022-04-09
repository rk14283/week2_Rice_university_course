
# I got question 6 wrong,which was related to function and question 8 wrong, which was related to area of polygon

def do_stuff():
    print "Hello world"
    print "Goodbye cruel world!"
    return "Is it over yet?"
    

print do_stuff()

print "==="
print 

def do_stuff():
    print "Hello world"
    return "Is it over yet?"
    print "Goodbye cruel world!"

print do_stuff()

#this is important because if print is before return then 
#you will get your output
n = 123

print (n % 100 - n % 10) / 10

print (n // 10) % 10


print (n % 10) / 10

print "===" 
import math 
import random

#print random.randint(0, 10)

#print random.randrange(0, 10)

def compute_q_6(x):
    x = ((-5*x**2) + (69*x**2) - (47)) 
    return x

print compute_q_6(0) 
print compute_q_6(1)
print compute_q_6(2)
print compute_q_6(3)

print "==="

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    fv = present_value* ((1+ rate_per_period)**periods)
    fv_round = round(fv,4)
    return fv_round 


    

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

print future_value(500, .04, 10, 10)

print "==="

def area_polygon(number_of_sides,side_length):
    area= (number_of_sides * (side_length **2))/(4*math.tan(math.pi/n))
    area_round = round(area,4)
    return area_round


print area_polygon(7,3)

print "==="

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))



def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance/dist_to_origin
    print point_x * scale, point_y * scale, 4

project_to_distance(2, 7,4)

print round (3.84609579056, 4)

