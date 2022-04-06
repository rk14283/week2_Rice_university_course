def favorites(instructor):
    """Returns the favorite thing of a given instructor."""
    
    
    if instructor == "Joe":
        return "games"
    elif instructor == "Scott":
        return "ties"
    elif instructor == "John":
        return "outdoors"
    else:
        print "favorites saw invalid instructor: " , instructor

print favorites("John")
print favorites("Jeannie")

#the first output was none, so make sure each of your ifs has an else case


