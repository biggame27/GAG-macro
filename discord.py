import requests 
import json
import re

import pydirectinput
import time
from pynput import mouse, keyboard
import datetime

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

# # looking for keywords: bee, sun, rare, legendary, mythical, paradise, bug
# def retrieve_messages(channelID):
#   keywords = ['bee', 'sun', 'rare', 'legendary', 'mythical', 'paradise', 'bug']
#   headers = {'authorization': 'NDUxOTI1NTQyMDAzMDE1Njgx.G4WHaH.ZvQ-cy3UxmMbSAe-G747oAH26kbjz9HfxDfQtc'}
#   # https://discord.com/api/v9/channels/1374191514518814734/messages?limit=50
#   r = requests.get(f'https://discord.com/api/v9/channels/{channelID}/messages?limit=50', headers=headers)
#   jsonn = json.loads(r.text)
#   # for value in jsonn:
#   #   print(value['embeds'][0]['fields'][0]['value'], '\n')
#   text = jsonn[0]['embeds'][0]['fields'][0]['value']
#   lower_text = text.lower()
#   return any(keyword in lower_text for keyword in keywords)

def retrieve_messages(channelID):
  keywords = ['bee', 'sun', 'rare', 'legendary', 'mythical', 'paradise', 'bug']
  headers = {'authorization': 'NDUxOTI1NTQyMDAzMDE1Njgx.G4WHaH.ZvQ-cy3UxmMbSAe-G747oAH26kbjz9HfxDfQtc'}
  # https://discord.com/api/v9/channels/1374191514518814734/messages?limit=50
  r = requests.get(f'https://discord.com/api/v9/channels/{channelID}/messages?limit=50', headers=headers)
  jsonn = json.loads(r.text)
  # for value in jsonn:
  #   print(value['embeds'][0]['fields'][0]['value'], '\n')
  # text = jsonn[0]['embeds'][0]['fields'][0]['value']
  # lower_text = text.lower()
  # return any(keyword in lower_text for keyword in keywords)
  text = ""
  for value in jsonn:
     if ('Vulcan' in value['author']['username']):
      text = value['embeds'][0]['fields'][0]['value']
      break
  lower_text = text.lower()
  return any(keyword in lower_text for keyword in keywords)

# print(retrieve_messages('1377312737180389408'))
print(retrieve_messages('1373218102313091072'))
# pydirectinput.PAUSE = 0.05

# def buy_egg():
#     pydirectinput.press('\\')
#     for i in range(12):
#         pydirectinput.press('a')
#     pydirectinput.press('w')
#     for i in range(4):
#         pydirectinput.press('d')
#     pydirectinput.press('s')
#     pydirectinput.press('enter')
    

# def on_click(x, y, button, pressed):
#     """
#     This function is called for each mouse event.
#     It triggers the action on a middle mouse button press.
#     """
#     if button == mouse.Button.middle and pressed:
#         buy_egg()
#         safe_click(920, 670)
#         safe_click()
#         pydirectinput.keyDown('d')
#         time.sleep(0.8)
#         pydirectinput.keyUp('d')
#         # hold e
#         time.sleep(1)

#         pydirectinput.keyDown('d')
#         time.sleep(0.2)
#         pydirectinput.keyUp('d')
#         #hold e
#         time.sleep(1)

#         pydirectinput.keyDown('d')
#         time.sleep(0.2)
#         pydirectinput.keyUp('d')
#         #hold e
#         time.sleep(1)

# def on_press(key):
#     """
#     This function is called for each keyboard event.
#     It checks if the Escape key was pressed to stop the listeners.
#     """
#     if key == keyboard.Key.esc:
#         print("Escape key pressed. Exiting script.")
#         # Stop both listeners
#         mouse_listener.stop()
#         return False  # Stop the keyboard listener

# # --- Listeners Setup (using pynput) ---
# # Listeners are started to wait for the trigger inputs.
# mouse_listener = mouse.Listener(on_click=on_click)
# keyboard_listener = keyboard.Listener(on_press=on_press)

# # Start the listeners
# mouse_listener.start()
# keyboard_listener.start()

# # Wait for the listeners to be stopped (by pressing ESC)
# mouse_listener.join()
# keyboard_listener.join()