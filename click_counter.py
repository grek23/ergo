from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key as keyboard_key
import numpy as np
import matplotlib.pyplot as plt

clicks = 0
distance = 0
prev_x = 0
prev_y = 0
data = []


def distance(x, y):
    global clicks

    if clicks == 0:
        return 0
    return int(np.sqrt((x - prev_x)**2 + (y - prev_y)**2))


def on_move(x, y):
    pass


def on_click(x, y, button, pressed):
    if pressed:
        global clicks
        global distance
        global prev_x
        global prev_y
        global data

        clicks += 1
        Dist = distance(x, y)
        data.append([x, y, Dist])
        prev_x = x
        prev_y = y
        print(f"Clicks = {clicks}, distance = {Dist}")


def on_scroll(x, y, dx, dy):
    print(f"scrolling along {x}, {y} and {dx}, {dy}")


def on_press(key):
    pass


def on_release(key):
    global clicks
    global data

    try:
        if (key.char == 'a') or (key == keyboard_key.f2):
            print("", end='')
    except:
        if key == keyboard_key.f2:
            print("Killing on exception F2")
            mouse_listener.stop()
            keyboard_listener.stop()
            mouse_listener.stop()
            print(f"data = {data}")
            X = []
            Y = []
            for i in data:
                X.append(i[0])
            for j in data:
                Y.append(j[1]*-1)
            print(f"x = {X}")
            print(f"Y = {Y}")
            plt.figure()
            plt.plot(X, Y, '*')
            plt.show()
        pass


with KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
    mouse_listener = MouseListener(
        on_move=on_move, on_click=on_click, on_scroll=on_scroll)
    mouse_listener.start()
    keyboard_listener.join()
