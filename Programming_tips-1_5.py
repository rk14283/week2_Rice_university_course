import math 

def area_triangle_sss(side1, side2, side3):
    """Returns the area of a triangle given the lenghts
    of its three sides
    """
    #Heron's formula 
    semi_perim = (side1 + side2+ side3) / 2.0
    return math.sqrt(semi_perim * 
                    (semi_perim- side1) *
                    (semi_perim- side2) *
                    (semi_perim- side3))



"""doc string is below a function header, 
it allows the string to over over multiple lines 
 it must have input output and how they relate
 a documentation string tells you what it does 
 but not how it does it"""


#no output 
