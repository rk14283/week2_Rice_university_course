# first example of drawing on the canvas

import simplegui

# define draw handler 
def draw(canvas):
    #the value 100, 100 is the position where the string was drawn
    canvas.draw_text("Hello", [100,100], 24, "White")
    #now we see a circle at lower left hand portion of the scree
    canvas.draw_circle([100,100], 2, 2, "Red")
    


# create frame 
frame = simplegui.create_frame("Test",300,200)

# register draw handler 
frame.set_draw_handler(draw)

# start frame 
frame.start()
