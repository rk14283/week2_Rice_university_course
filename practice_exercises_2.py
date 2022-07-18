# Register three buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 


# Handlers for buttons
def set_red():
    global color
    color = "red"
    
def set_blue():
    global color
    color = "blue"
    
def print_color():
    print color

# Create frame
frame = simplegui.create_frame("Set and print colors", 200, 200)
frame.add_button("print_color", set_red)
frame.add_button("red", set_red)
frame.add_button("blue", set_blue)


# Start the frame animation
frame.start()


###################################################
# Test

set_red()
print_color()
set_blue()
print_color()
set_red()
set_blue()
print_color()

###################################################
# Expected output from test

#red
#blue
#blue



# GUI with buttons to manipulate global variable count

###################################################
# Student should enter their code below


import simplegui

# Define event handlers for four buttons
#Don't forget docstrings 

#count = 0, this would make it global as well 
def reset():
    """Reset global count to zero."""
    global count 
    count = 0 
    return count

def increment():
     """Increment global count."""
    global count 
    count += 1
    return count 

def decrement():
    """Decrement global count."""
    global count 
    count -= 1
    return count

def print_count():
    """Print global count."""
    global count 
    print count 
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Returns count", 200, 200)
frame.add_button("reset to 0",reset)
frame.add_button("increment by 1",increment)
frame.add_button("decrement by 1",decrement)
frame.add_button("prints count",print_count)


# Start the frame animation
frame.start()

    
###################################################
# Test

# Note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Expected output from test

#1
#2
#-2

# Echo an input field

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Handlers for input field
def get_input(txt):
    print txt
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Echo input", 200, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_input("First test input")
get_input("Second test input")
get_input("Third test input")

###################################################
# Expected output from test

#First test input
#Second test input
#Third test input


# Convert input text into Pig Latin

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Pig Latin helper function
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.

# Handler for input field


def get_input(word):
     """Prints the (simplified) Pig Latin version of the word to console."""
    first_letter = word[0]
    rest_of_word = word[1 : ]
    if first_letter in ['a', 'e', 'i', 'o', 'u']:
        print word + "way" 
    else: 
        print rest_of_word + first_letter+ "ay"
    
    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)


# Start the frame animation
frame.start()



###################################################
# Test

get_input("pig")
get_input("owl")
get_input("tree")

###################################################
# Expected output from test

#igpay
#owlway
#reetay



# Convert input text into Pig Latin

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Pig Latin helper function
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.
    if (first_letter == "a" or first_letter == "e" or first_letter == "i" or
        first_letter == "o" or first_letter == "u"):
        return word + "way"
    else:
        return rest_of_word + first_letter + "ay"


# Handler for input field
def get_input(txt):
    print pig_latin(txt)
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)
frame.add_input("Translate to Pig Latin (hit enter)", get_input, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_input("pig")
get_input("owl")
get_input("tree")

###################################################
# Expected output from test

#igpay
#owlway
#reetay


# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Insert your solution for RPSLS here
def name_to_number(name):
   #"""Takes input as name of five characters in the game and returns number between 0 to 4"""
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2 
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return "Error! wrong input."

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    """Takes input between 0 to 4 and returns one of five characters in the game: rock, paper, scissors, lizard, Spock"""
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'     
    else:
        return "Error! wrong input."
    
    
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below

    
    # print a blank line to separate consecutive games
    print 

    # print out the message for the player's choice
    print "Player chooses" + " " + player_choice 

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    #print comp_number 

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    
    print "Computer chooses" + " " +comp_choice
    

    # compute difference of comp_number and player_number modulo five
    score_differece =  ((comp_number) - (player_number)) %5 
    
    absolute_difference =  abs(score_differece)

    # use if/elif/else to determine winner, print winner message
    if      absolute_difference == 1 or      absolute_difference == 2:
        print "Compter wins!"
    elif      absolute_difference == 3 or      absolute_difference  == 4:
        print "Player wins!"
    elif   absolute_difference== 0:
        print "Player and computer tie!"
    else:
        print "there was a wrong input, no one wins"
        


     
    
# handler for input field
def get_guess(guess):
    
    # validate input
    if not (guess == "rock" or guess == "Spock" or guess == "paper" or
            guess == "lizard" or guess == "scissors"):
        print
        print 'Error: Bad input "' + guess + '" to rpsls'
        return
    else:
        rpsls(guess)
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#


