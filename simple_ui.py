# Simple pygame program


# Import and initialize the pygame library

import pygame
import os

pygame.init()


# Set up the drawing window

screen = pygame.display.set_mode([500, 500])
koi = pygame.image.load(os.path.join("/Users/kaedonhamm/Pictures/koi_minimal_background.png"))


# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False


    # Fill the background with white

    screen.fill((0, 0, 0))


    # Draw a solid blue circle in the center
                            #   color        x     y  ,  diameter
    pygame.draw.circle(screen, (255, 0, 0), (250, 100), 10)
    


    # Flip the display

    pygame.display.flip()


# Done! Time to quit.

pygame.quit()
