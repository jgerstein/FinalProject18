import pyglet                               # import pyglet

window = pyglet.window.Window()             # create a window. can specify a size, but defaults are reasonable
# label = pyglet.text.Label("Hello world")  # create a label (text) and assign it to label. This version uses defaults other than providing a string for text
label = pyglet.text.Label("Hello world",    # create a label with lots of configuration options
                            font_size=48,
                            color=(255,0,255,255),
                            x=window.width//2,
                            y=window.height//2,
                            anchor_x='center',
                            anchor_y='center',
                            font_name=['Comic Sans MS', 'Bauhaus 93', 'System'])

"""The syntax here is something most of you haven't seen before.

@window.event is something called a 'decorator'. Essentially, it modifies 
a function. For your purposes, what you would need to know about it is that 
for each type of event you'd use (there's a list of them), you'd define a 
function for that event and use @window.event to indicate that it's an
event affecting your window.

The code below will cause the window to be cleared and the text to be
redrawn each time the window is redrawn"""

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()    # runs the application