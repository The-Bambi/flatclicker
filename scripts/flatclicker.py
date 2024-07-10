from datetime import datetime, sleep

import pyautogui as pg


def jiggle_with_click():
    pg.click(clicks=2)
    pg.move(3,3)
    pg.click(clicks=2)

def jiggle_with_scroll():
    pg.scroll(10)
    sleep(1)
    pg.scroll(3)
    sleep(2)
    pg.scroll(-8)
    pg.move(3,3)

def test():
    print("TOO LONG INACTIVE!")

def mouse_moved(prev_x, prev_y):
    x, y = pg.position()
    if prev_x != x or prev_y != y:
        return True
    else:
        return False

def flatclicker():

    last_mouse_move = datetime.now()
    countdown = 10

    try:
        while True:
            now_x, now_y = pg.position()
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
