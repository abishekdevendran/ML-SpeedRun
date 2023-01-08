import os
import pygame as pg
pg.init()
# set the screen size
screen = pg.display.set_mode((500, 500))
# set the screen title
pg.display.set_caption("EigenPaint")
# set the screen background color
screen.fill((255, 255, 255))
# set the variable to keep the program running
running = True
# add UI button to save the screen on new surface
save_button = pg.Rect(0, 0, 100, 50)
pg.draw.rect(screen, (0, 0, 0), save_button)
# Add text to the save button
font = pg.font.SysFont("Arial", 20)
text = font.render("Save", True, (255, 255, 255))
screen.blit(text, (save_button.x + 30, save_button.y + 10))
# set the screen to be visible
pg.display.flip()
# set the variable to check if the mouse is drawing
drawing = False
# main loop
while running:
    # loop through the event queue
    for event in pg.event.get():
        # check for closing the window
        if event.type == pg.QUIT:
            running = False
            pg.quit()
        # check for mouse button down
        if event.type == pg.MOUSEBUTTONDOWN:
            # check for left mouse button
            if event.button == 1:
                # get the mouse position
                pos = pg.mouse.get_pos()
                # if the mouse is in the save button
                if save_button.collidepoint(pos):
                    # save the screen as a png in same folder as the program
                    pg.image.save(screen, os.path.join(
                        os.path.dirname(__file__), "paint.png"))
                else:
                    drawing = True
                    # draw a circle at the mouse position
                    pg.draw.circle(screen, (255, 0, 0), pos, 5)
                    # update the screen
                    pg.display.flip()
        # check for mouse button up
        elif event.type == pg.MOUSEBUTTONUP:
            drawing = False
        # check for mouse motion
        elif event.type == pg.MOUSEMOTION:
            # check for left mouse button
            if pg.mouse.get_pressed()[0] and drawing:
                # get the mouse position
                pos = pg.mouse.get_pos()
                # draw a circle at the mouse position
                pg.draw.circle(screen, (255, 0, 0), pos, 5)
                # update the screen
                pg.display.flip()
