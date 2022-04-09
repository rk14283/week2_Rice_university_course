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
