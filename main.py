# Standard library imports
import time
from statistics import mean
from time import sleep
from itertools import cycle
import json

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

    if key == keyboard.Key.shift_r:
        end_program = True  # Flip global flag
        return False  # Stop listener
    elif key == keyboard.Key.tab:
        key_pressed = True  # Flip global flag


def elapsed(ref, timeout):
    return time.perf_counter() - ref > timeout


def main():
    # Variable declaration and initialization
    global end_program, key_pressed
    mode_cycle = cycle(['sleepMode', 'combatMode', 'lootMode'])
    current_mode = next(mode_cycle)
    with open('main/resources/templates/config.json') as f:
        cfg = json.load(f)
        loot_poi = cfg['lootPoi']
        loot_click = (mean([loot_poi[0][0], loot_poi[1][0]]), mean([loot_poi[0][1], loot_poi[1][1]]))
    last_gather = time.perf_counter()
    last_loot = time.perf_counter()

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
            img = w_mgr.get_combat_area()
            if im.is_combat_combo(img) or im.is_start_combat(img):
                pyautogui.click(pyautogui.position())
                sleep(1)
        elif current_mode == 'lootMode':
            # Gather mode
            if elapsed(last_gather, 0.5) and im.is_gather(w_mgr.get_gather_area()):
                pyautogui.click(pyautogui.position())
                last_gather = time.perf_counter()
            elif elapsed(last_loot, 0.5) and im.is_loot(w_mgr.get_loot_area()):
                pyautogui.click(loot_click)
                last_loot = time.perf_counter()
        elif current_mode == 'sleepMode':
            # Sleep mode
            sleep(0.1)

    # Play "Shutting down" sound
    s_mgr.play_shut_down_audio()


if __name__ == '__main__':
    main()
