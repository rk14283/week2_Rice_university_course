"""A function that gives away money to friends"""
def greet(friend, money): 
    if friend and (money>20):
        print "Hi!"
        money = money - 20
    else:
        print "Hello"
    return money 


money = 15

money = greet(True, money)
print  "Money:", money 
print ""

money = greet(False, money)
print "Money:", money 
print ""

money = greet(True, money) 
print "Money:", money 
print ""
