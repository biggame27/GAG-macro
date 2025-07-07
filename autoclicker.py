import time
import threading
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode, Key

# --- Configuration ---
# Set the time delay (in seconds) between each click.
CLICK_INTERVAL = 10

# Set to True to click at the current mouse position.
# Set to False to click at the fixed coordinates specified below.
CLICK_AT_CURRENT_POSITION = False 

# The fixed coordinates for the click if CLICK_AT_CURRENT_POSITION is False.
CLICK_X, CLICK_Y = 1180, 600
#GARDEN_X, GARDEN_Y = 1000, 100

# Assign the key to start and stop the auto-clicker.
# Use KeyCode.from_char('s') for regular keys or Key.f8 for special keys.
START_STOP_KEY = KeyCode.from_char('p')

# Assign the key to terminate the script completely.
EXIT_KEY = Key.esc
# ---------------------


# --- Script Logic ---
# Global variables to control the state of the clicker and the threads.
clicking = False
mouse = MouseController()

def clicker():
    """
    This function contains the main clicking loop.
    It runs in a separate thread and will continuously click the left
    mouse button as long as the 'clicking' variable is set to True.
    It respects the location configuration (current vs. fixed position).
    """
    while True:
        if clicking:
            # If not clicking at the current position, move the mouse first.
            # if not CLICK_AT_CURRENT_POSITION:
            #     mouse.position = (CLICK_X, CLICK_Y)
            time.sleep(1)
            mouse.click(Button.left, 1)
        # The sleep time is essential to prevent the script from consuming
        # too much CPU and to control the click speed.
        time.sleep(CLICK_INTERVAL)

def on_press(key):
    """
    This function is a callback that runs whenever a key is pressed.
    It checks if the pressed key matches our designated start/stop or exit keys.
    """
    # We use a global variable to be able to modify it from this function.
    global clicking

    # Check if the pressed key is the start/stop key.
    if key == START_STOP_KEY:
        clicking = not clicking
        if clicking:
            print("Auto-clicker started.")
        else:
            print("Auto-clicker stopped.")

    # Check if the pressed key is the exit key.
    if key == EXIT_KEY:
        print("Exiting script.")
        # Stop the clicker loop.
        clicking = False
        # Stop the keyboard listener.
        return False

# --- Main execution block ---
# if __name__ == "__main__":
#     # This block runs when the script is executed directly.
    
#     print("--- Python Auto-Clicker ---")
#     print("Instructions:")
#     try:
#         # Try to get the character of the start/stop key for display.
#         start_key_char = f"'{START_STOP_KEY.char}'"
#     except AttributeError:
#         # If it's a special key (like F8), display its name.
#         start_key_char = f"'{str(START_STOP_KEY).split('.')[-1]}'"

#     print(f" > Press {start_key_char} to start or stop clicking.")
#     print(f" > Press '{str(EXIT_KEY).split('.')[-1].capitalize()}' to exit the script completely.")
#     print("---------------------------")
#     if CLICK_AT_CURRENT_POSITION:
#         print("Mode: Clicking at current mouse position.")
#     else:
#         print(f"Mode: Clicking at fixed position ({CLICK_X}, {CLICK_Y}).")
#     print("---------------------------")
    
#     # Set up and start the clicking thread.
#     # The 'daemon=True' argument makes the thread exit when the main script exits.
#     click_thread = threading.Thread(target=clicker, daemon=True)
#     click_thread.start()

#     # Set up and start the keyboard listener.
#     # The 'with' statement ensures that the listener is properly released.
#     with Listener(on_press=on_press) as listener:
#         # The join() method will block the main thread until the listener is stopped.
#         listener.join()
