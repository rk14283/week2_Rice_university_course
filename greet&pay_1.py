"""A function that gives away money to friends"""
def great(friend, money): 
    print "Hi!"
    money = money - 20
    return money 


money = 15

money = great(True, money)
print  "Money:", money 
print ""

money = great(True, money) 
print "Money:", money 
print ""
