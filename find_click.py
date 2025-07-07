# You may need to install pynput first: pip install pynput
from pynput import mouse, keyboard

print("Starting coordinate finder...")
print("Click anywhere on the screen to get its coordinates.")
print("Press the ESC key to stop the script.")

def on_click(x, y, button, pressed):
    """
    This function is called whenever a mouse click event occurs.
    """
    # We only want to print the coordinates when the button is pressed down, not released.
    if pressed:
        # The formatting helps align the coordinates in the console
        print(f"Mouse clicked at: X={x:<5} Y={y:<5}")

def on_press(key):
    """
    This function is called whenever a key is pressed.
    It checks for the Escape key to stop the program.
    """
    if key == keyboard.Key.esc:
        print("\nESC key pressed. Exiting...")
        # Stop the mouse listener, which will allow the script to end.
        mouse_listener.stop()
        # Stop the keyboard listener by returning False
        return False

# Setup the listener objects
mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

# Start listening for events in background threads
mouse_listener.start()
keyboard_listener.start()

# Keep the main script running until the listeners are stopped
# The script will end when mouse_listener.stop() is called
mouse_listener.join()
keyboard_listener.join()

print("Script stopped. Have a great day!")
