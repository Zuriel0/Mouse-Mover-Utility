import time
import pyautogui
import random
import ctypes
import keyboard
from pynput.keyboard import Listener, KeyCode


INACTIVITY_TIME = 100

prev_x, prev_y = pyautogui.position()


pressed_key = None


def on_press(key):
    global pressed_key
    pressed_key = key

def on_release(key):
    global pressed_key
    pressed_key = None


with Listener(on_press=on_press, on_release=on_release) as listener:

    while True:
        time.sleep(INACTIVITY_TIME)

        curr_x, curr_y = pyautogui.position()
        
        if pressed_key:
            continue
        
        if curr_x == prev_x and curr_y == prev_y:
            x = random.randint(0, pyautogui.size().width)
            y = random.randint(0, pyautogui.size().height)
    
            pyautogui.moveTo(x, y)
    
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
        
        prev_x, prev_y = curr_x, curr_y

        if keyboard.is_pressed('ctrl+shift+q'):
            break

