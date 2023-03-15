from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key as keyboard_key
import numpy as np
import matplotlib.pyplot as plt


m_data = []
k_data = []
valid = True


def on_move(x, y):
    pass


def on_click(x, y, button, pressed):
    global m_data

    if pressed:
        m_data.append([x, y, button])
        print(f"clicky: x = {x}, y = {y}")


def on_scroll(x, y, dx, dy):
    print(f"scrolling along {x}, {y} and {dx}, {dy}")


def on_press(key):
    pass


def on_release(key):
    global k_data
    global valid
    print(f"key <{key}>")
    try:
        if key == keyboard_key.f2:
            print(f"F2 pressed {key}")
            k_data.append(key)

            valid = False
            return False
    except:
        print("Exception")

    return False


def get_coords(data):
    x = []
    y = []
    for d in data:
        x.append(int(d[0]))
        y.append(int(d[1]))
    return x, y, len(data)


def plotting(x, y):

    plt.figure()
    plt.plot(x, y, "*")
    plt.show()


def main():
    global m_data
    global k_data
    global valid

    print("Counting mouse Clicks")
    print("Press F2 to exit")

    while valid:
        with KeyboardListener(on_press=on_press, on_release=on_release) as k_listen:
            mouse_listener = MouseListener(
                on_move=on_move, on_click=on_click, on_scroll=on_scroll)
            mouse_listener.start()
            k_listen.join()

        if not valid:
            k_listen.stop()
            mouse_listener.stop()

    x, y, totals = get_coords(m_data)

    print(f"Total number of clicks: {totals}")
    print(x)
    print(y)

    plotting(x, y)


if __name__ == '__main__':
    main()
