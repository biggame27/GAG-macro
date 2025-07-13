import pydirectinput
import time
from pynput import mouse, keyboard
pydirectinput.PAUSE = 0.05

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

def buy(times = 1):
    buy_sequence1 = ['enter', 's', 's', 'enter', 'w', 'enter']
    buy_sequence3 = ['enter', 's', 's', 'enter', 'enter', 'enter', 'w', 'enter']
    if times == 1:
        for i in buy_sequence1:
            pydirectinput.press(i)
            time.sleep(0.1)
    else:
        for i in buy_sequence3:
            pydirectinput.press(i)
            time.sleep(0.1)

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

    menu_sequence = ['\\', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'd']
    stuff_to_buy = [2,3,4,5, 7,8]
    time.sleep(0.5)
    for i in menu_sequence:
        pydirectinput.press(i)

    for i in range(6):
      if i >= 4:
          buy(3)
      if i != 5:
        pydirectinput.press('s')
        pydirectinput.press('s')
    time.sleep(0.1)
    for i in range(6):
        pydirectinput.press('w')
        pydirectinput.press('w')
    pydirectinput.press('s')
    pydirectinput.press('d')
    pydirectinput.press('enter')
    pydirectinput.press('\\')
time.sleep(5)
# pydirectinput.keyDown('d')
# time.sleep(0.5)
# pydirectinput.keyUp('d')

# safe_click(1200,500)

egg()
