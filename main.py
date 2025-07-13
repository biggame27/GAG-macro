import pydirectinput
import time
from pynput import mouse, keyboard
import datetime
import requests
import json
import re

# must make sure thate the seed shop is scrolled all the up
# look at table, scroll out

# --- pydirectinput Configuration ---
# You can adjust these if needed, but the defaults are generally fine.
pydirectinput.PAUSE = 0.05  # A small default pause after each action
cnt = 0 # for wrench

print("Script is running...")
print("-> Press the MIDDLE mouse button to focus, type, and scroll.")
print("-> Press the ESC key to exit the script.")
def buy(times = 1):
    buy_sequence1 = ['enter', 's', 'enter', 'w', 'enter']
    buy_sequence3 = ['enter', 's', 'enter', 'enter', 'enter', 'w', 'enter']
    if times == 1:
        for i in buy_sequence1:
            pydirectinput.press(i)
            time.sleep(0.1)
    else:
        for i in buy_sequence3:
            pydirectinput.press(i)
            time.sleep(0.1)

def garden():
    """
    The full sequence using pydirectinput: focus cursor, type keys, and then scroll up.
    """
    # --- Part 1: Focus Cursor ---
    target_position = (980, 500)
    print(f"Moving cursor to {target_position} and clicking...")
    
    # Move the cursor and click to focus
    pydirectinput.moveTo(target_position[0], target_position[1])
    pydirectinput.click()

    # A brief pause to ensure the click is processed
    time.sleep(0.1)
    pydirectinput.press('\\')
    for i in range(12):
        pydirectinput.press('a')
    pydirectinput.press('w')

    # --- Part 2: Typing ---
    # Note: pydirectinput handles special keys by their string name.
    type_sequence = ['d', 'd', 's', 'enter', 'e']
    
    for key in type_sequence:
        pydirectinput.press(key)
        # A small sleep is still good practice for reliability in some applications
        time.sleep(0.1)

    # --- Part 3: Scrolling ---
    time.sleep(3)
    for i in range(23):
        if i >= 13:
            buy()
        if i != 22:
            pydirectinput.press('s')
        time.sleep(0.1)
    
    for i in range(22):
        pydirectinput.press('w')
    pydirectinput.press('enter')
    pydirectinput.press('\\')
    
    
    # x out of seeds
    # for _ in range(21):
    #     pydirectinput.press('w')
    #     time.sleep(0.1)
    # pydirectinput.press('enter')
    # pydirectinput.click()

def safe_click(x, y, button='left'):
    """
    A more robust click function that "wakes up" the cursor first.
    """
    print(f"Moving to ({x}, {y})...")
    pydirectinput.moveTo(x, y)
    time.sleep(0.1) # A small pause after moving
    
    print("Performing a relative move to 'wake up' the cursor...")
    # Move 1 pixel right and then back. This is a quick "jitter".
    pydirectinput.moveRel(1, 0) 
    time.sleep(0.05)
    pydirectinput.moveRel(-1, 0)

    print(f"Clicking at the current position.")
    pydirectinput.click(button=button)

def gear():
    """
    The gear sequence using pydirectinput.
    """
    # make sure to look at top of table, be 9 scroll wheels away from first person
    pydirectinput.press('2')
    safe_click(1200, 500)
    time.sleep(2)
    
    pydirectinput.press('e')
    
    time.sleep(3)
    safe_click(1200, 580)
    time.sleep(3)

    menu_sequence = ['\\', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'd']
    stuff_to_buy = [2,3,4,5, 7,8]
    for i in menu_sequence:
        pydirectinput.press(i)
        time.sleep(0.1)
    for i in range(13):
        if i in stuff_to_buy:
            if i > 2:
                buy()
                buy()
            if (cnt % 5 == 0 or i != 2):
                buy()
        if i != 12:
            pydirectinput.press('s')
            time.sleep(0.1)
    for i in range(13):
        pydirectinput.press('w')
        time.sleep(0.1)
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('\\')

def purchase():
    pydirectinput.press('e')
    pydirectinput.press('\\')
    for i in range(12):
        pydirectinput.press('a')
    pydirectinput.press('w')
    for i in range(4):
        pydirectinput.press('d')
    pydirectinput.press('s')
    pydirectinput.press('enter')
    pydirectinput.press('\\')

def egg():
    """
    The egg sequence using pydirectinput.
    """
    pydirectinput.keyDown('d')
    time.sleep(0.5)
    pydirectinput.keyUp('d')
    
    pydirectinput.press('e')
    
    time.sleep(3)
    safe_click(1200, 500)
    time.sleep(3)

    menu_sequence = ['\\', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'd']
    stuff_to_buy = [2,3,4,5, 7,8]
    for i in menu_sequence:
        pydirectinput.press(i)
        time.sleep(0.1)

    for i in range(6):
      if i >= 4:
          buy(3)
      if i != 5:
        pydirectinput.press('s')
        pydirectinput.press('s')
    for i in range(6):
        pydirectinput.press('w')
        pydirectinput.press('w')
    pydirectinput.press('s')
    pydirectinput.press('d')
    pydirectinput.press('enter')
    pydirectinput.press('\\')

def on_click(x, y, button, pressed):
    """
    This function is called for each mouse event.
    It triggers the action on a middle mouse button press.
    """
    global cnt
    if button == mouse.Button.middle and pressed:
        print("Middle mouse button clicked! Running full sequence...")
        now = datetime.datetime.now().minute
        while True:
            now = datetime.datetime.now().minute
            if now % 5 == 0:
                garden()
                gear()
                cnt += 1
                if (now == 30 or now == 31 or now == 0 or now == 1):
                    egg()
            time.sleep(30)

def on_press(key):
    """
    This function is called for each keyboard event.
    It checks if the Escape key was pressed to stop the listeners.
    """
    if key == keyboard.Key.esc:
        print("Escape key pressed. Exiting script.")
        # Stop both listeners
        mouse_listener.stop()
        return False  # Stop the keyboard listener

# --- Listeners Setup (using pynput) ---
# Listeners are started to wait for the trigger inputs.
mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

# Start the listeners
mouse_listener.start()
keyboard_listener.start()

# Wait for the listeners to be stopped (by pressing ESC)
mouse_listener.join()
keyboard_listener.join()