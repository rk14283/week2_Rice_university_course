# interactive application to convert a float into dollars and cents 
import simplegui 

# define global value 

value = 3.12 #draws 3.12 in the string


# Handle single quantity
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result
        
# convert xx.yy to xx dollars and yy cents
def convert(val):
    # Split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
    
    
#this taking input and drawing canvas would look good on an actual web app
    
# define draw handler 
def draw(canvas):
    #to fit your text you need to adjust value in the list 
    canvas.draw_text(convert(value), [60, 110], 24, "White")

# define an input field handler 
def input_handler(text):
    global value 
    value = float(text)

# create a frame
frame = simplegui.create_frame("Converter", 300, 200) 


# register the event handlers
frame.set_draw_handler(draw) 
frame.add_input("Enter value", input_handler, 100)


# start the frame 
frame.start() 

