# Standard library imports
import winsound
from time import sleep

# Third party imports
import pyautogui

# Local application imports
from main.code.windowMgr import WindowMgr
from main.code.imageMatcher import ImageMatcher
from pynput import keyboard

# Global variables
end_program = False
key_pressed = False
mode = 2


def on_press(key):
    global end_program, key_pressed

    if key == keyboard.Key.esc:
        end_program = True  # Flip global flag
        return False  # Stop listener
    elif key == keyboard.Key.tab:
        key_pressed = True  # Flip global flag


def main():
    global end_program, key_pressed, mode

    # Initialize keyboard listener on a separate thread
    keyboard.Listener(on_press=on_press).start()

    # Initialize all the internal modules.
    w_mgr = WindowMgr("The Witcher.*")
    im = ImageMatcher(path_to_resources='main/resources/templates')

    # Main loop
    mode_audios = [
        'main/resources/sounds/combatMode.wav',
        'main/resources/sounds/lootMode.wav',
        'main/resources/sounds/sleepMode.wav'
    ]
    winsound.PlaySound('main/resources/sounds/bootUp.wav', winsound.SND_FILENAME)
    while not end_program:
        # Change mode if needed
        if key_pressed:
            mode = 0 if mode == 2 else mode + 1
            winsound.PlaySound(mode_audios[mode], winsound.SND_FILENAME | winsound.SND_ASYNC)
            key_pressed = False

        # Main decision tree
        if mode == 0:
            # Combat mode
            img = w_mgr.get_mouse_area()
            if im.is_combat_combo(img) or im.is_start_combat(img):
                pyautogui.click(pyautogui.position())
                sleep(1)
        elif mode == 1:
            # Gather mode
            img = w_mgr.get_mouse_area()
            if im.is_gather(img):
                pyautogui.click(pyautogui.position())
                sleep(1)
        elif mode == 2:
            # Sleep mode
            sleep(0.5)

    # Play "Shutting down" sound
    winsound.PlaySound('main/resources/sounds/shutDown.wav', winsound.SND_FILENAME)


if __name__ == '__main__':
    main()
