def area_triangle(base, height):
    return 0.5 * base * height 

b = 5 #we also removed "" from here
h = 2 + 2 #this caused second type error, and we had to remove double quotes 

#here we passed in only b, but we required b and h 
print "Area of triangle with base", b, "and height", h, "is",area_triangle(b,h), "." 

