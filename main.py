# Standard library imports
from time import sleep
from itertools import cycle

# Third party imports
import pyautogui

# Local application imports
from main.code.windowMgr import WindowMgr
from main.code.soundMgr import SoundMgr
from main.code.imageMatcher import ImageMatcher
from pynput import keyboard

# Global variables
end_program = False
key_pressed = False


def on_press(key):
    global end_program, key_pressed

    if key == keyboard.Key.esc:
        end_program = True  # Flip global flag
        return False  # Stop listener
    elif key == keyboard.Key.tab:
        key_pressed = True  # Flip global flag


def main():
    global end_program, key_pressed
    mode_cycle = cycle(['sleepMode', 'combatMode', 'lootMode'])
    current_mode = next(mode_cycle)

    # Initialize keyboard listener on a separate thread
    keyboard.Listener(on_press=on_press).start()

    # Initialize all the internal modules.
    w_mgr = WindowMgr()
    s_mgr = SoundMgr()
    im = ImageMatcher()

    # Main loop
    s_mgr.play_boot_up_audio()
    while not end_program:
        # Change mode if needed
        if key_pressed:
            current_mode = next(mode_cycle)
            s_mgr.play_mode_audio(current_mode)
            key_pressed = False

        # Main decision tree
        if current_mode == 'combatMode':
            # Combat mode
            img = w_mgr.get_mouse_area()
            if im.is_combat_combo(img) or im.is_start_combat(img):
                pyautogui.click(pyautogui.position())
                sleep(1)
        elif current_mode == 'lootMode':
            # Gather mode
            img = w_mgr.get_mouse_area()
            if im.is_gather(img):
                pyautogui.click(pyautogui.position())
                sleep(1)
        elif current_mode == 'sleepMode':
            # Sleep mode
            sleep(0.1)

    # Play "Shutting down" sound
    s_mgr.play_shut_down_audio()


if __name__ == '__main__':
    main()
