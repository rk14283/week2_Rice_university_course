### String Processing 

# String literals 

s1 = "Rixner's funny" 
s2 = 'Warren wears nice ties!'
s3 = 't-shirts!'
#print s1, s2
#print s3 

# combining strings 
a = ' and '
s4 = "Warren" + ' and ' + "Rixner" + ' are nuts!'
print s4 


# characters and slices 
#print s1[-1], getting the last character, remember this 
print s1[-2]
print len(s1) 

#you will get an error when you go beyond 14, simiarly you will get an index error if you type -14

# getting a slice 
print s1[0:8]

#s2[6:] going all the way till the end 
print s1[0:6] + s2[6:]

# begining up to the 13th index 
# they are clever 
print s2[:13] + s1[9:] + s3


# converting strings 
s5 = str(375) 
#slice of 375
print s5[1:]
i1 = int(s5[1:])
print i1 + 38 




