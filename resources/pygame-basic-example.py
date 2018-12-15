import pygame       # import pygame module
pygame.init()       # initialize all of pygame's submodules
screen = pygame.display.set_mode((400, 400))    # create a surface called 'screen' and give it a size of 400x400
running = True      # used to control while loop

while running:      # main loop of program. will repeat until the window is closed
    """Below this line is a for loop for handling the event queue.
    The event queue takes every event (user interaction) that happens in the pygame window and
    makes it available in order. the variable 'e' will be each event in order.
    Anything that involves handling events should generally happen in here"""
    
    for e in pygame.event.get():    # get each event in the event queue... 
        print(e)                    # ...and print that event
        if e.type == pygame.QUIT:   # ...and if that event is QUIT...
            running = False         # ...set running to False so the main loop ends
    
    """It's probably worth noting that we're still in the main loop here, but have left the for loop  
    for the event queue. This will run on repeat, but won't repeat for each event."""
    screen.fill((0,0,0))            # fill the display with black 
    pygame.draw.circle(screen, (200, 40, 255), pygame.mouse.get_pos(), 20)      # draw a circle on the display, in purple, at the mouse location, with a radius of 2-
    pygame.display.flip()           # update the display