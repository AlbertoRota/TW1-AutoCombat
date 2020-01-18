# Standard library imports
import os
import time

# Third party imports
from pynput import keyboard
from PIL import ImageGrab

# Global variables
end_program = False


def on_press(key):
    """Pressing "Right Sift" will stop the program, "Tab" will take an snapshot."""
    global end_program
    if key == keyboard.Key.shift_r:
        end_program = True
        return False
    elif key == keyboard.Key.tab:
        take_screenshot()


def take_screenshot():
    """Takes a full-screen snapshot and saves it."""
    img_name = os.getcwd() + '/main/resources/calibration/full_snap_' + str(int(time.time())) + '.png'
    ImageGrab.grab().save(img_name, 'PNG')
    print('New screenshot taken: ' + img_name)


def main():
    """Program entry point."""
    global end_program
    keyboard.Listener(on_press=on_press).start()
    while not end_program:
        pass


if __name__ == '__main__':
    main()