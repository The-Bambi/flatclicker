from time import sleep
from datetime import datetime

import pyautogui as pag

def jiggle_with_click():
    pag.click(clicks=2)
    pag.move(3,3)
    pag.click(clicks=2)

def jiggle_with_scroll():
    pag.scroll(10)
    sleep(1)
    pag.scroll(3)
    sleep(2)
    pag.scroll(-8)
    pag.move(3,3)

def test():
    print("TOO LONG INACTIVE!")

def mouse_moved(prev_x, prev_y):
    x, y = pag.position()
    if prev_x != x or prev_y != y:
        return True
    else:
        return False

def main():

    last_mouse_move = datetime.now()
    countdown = 10

    try:
        while True:
            now_x, now_y = pag.position()
            sleep(1)
            if not mouse_moved(now_x, now_y):
                countdown -= 1
                if countdown < 0:
                    # test()
                    jiggle_with_scroll()
                    countdown = 10
            else:
                countdown = 10
                print("ok mouse moved")
                last_mouse_move = datetime.now()

    except KeyboardInterrupt:
        print("stop!")


if __name__=="__main__":
    main()
