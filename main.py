# Standard library imports
from time import sleep

# Third party imports
import pyautogui

# Local application imports
from main.code.windowMgr import WindowMgr
from main.code.imageMatcher import ImageMatcher
from main.code.debugUtils import DebugUtils


def main():
    # Initialize all modules.
    w = WindowMgr("The Witcher.*")
    im = ImageMatcher(path_to_resources='main/resources/templates')
    d = DebugUtils(True)

    # Main loop
    while True:
        # Get a fresh image
        img = w.get_mouse_area()

        # Main decision tree
        if im.is_combat_combo(img):
            pyautogui.click(pyautogui.position())
            sleep(1)
        elif im.is_start_combat(img):
            pyautogui.click(pyautogui.position())
            sleep(1)


if __name__ == '__main__':
    main()
