import pygame
import thorpy as tp
from datetime import time

pygame.init()

CLICK_POSITION = None
CLICK_INTERVAL_SECONDS = 180

screen = pygame.display.set_mode((700, 450))
tp.init(screen, tp.theme_round2) #bind screen to gui elements and set theme

# position control:
# set position button - if pressed - wait for next click, on next click overwrite CLICK_POSITION 
# and pop-up alert "position set" some height over the position
# clear position - CLICK_POSITION = None
# text field that shows coords of the position, or None
choose_position = tp.Button("Set")
clear_position = tp.Button("Clear")
position_group = tp.Group([tp.Text("Position control"), choose_position, clear_position, tp.Text(str(CLICK_POSITION) if CLICK_POSITION else "On mouse")], mode="v")

click_interval = tp.SliderWithText("Click interval [seconds]", 1, 600, CLICK_INTERVAL_SECONDS, 300, mode='v')
click_interval_group = tp.Group([click_interval], mode='h')


clicking_control = tp.SwitchButtonWithText("Clicking control", ("On", "Off"), value=False)
click_type = tp.DropDownListButton(['Left Click', 'Double Click', 'Triple Click', 'Scroll', ])
click_control_group = tp.Group([clicking_control, click_type], mode='v')

metagroup = tp.Group([position_group, click_interval_group, click_control_group], mode='h')

def before_gui(): #add here the things to do each frame before blitting gui elements
        screen.fill((35,)*3)
tp.call_before_gui(before_gui) #tells thorpy to call before_gui() before drawing gui.

#For the sake of brevity, the main loop is replaced here by a shorter but blackbox-like method

player = metagroup.get_updater().launch()
pygame.quit()
