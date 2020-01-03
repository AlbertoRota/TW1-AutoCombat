# Standard library imports
import re
import json

# Third party imports
import numpy as np
import cv2
import win32gui
import win32con
from PIL import ImageGrab


def _img_2_np(image):
    # Convert it to NumPy
    image_np = np.array(
        image.getdata(),
        dtype='uint8'
    ).reshape((
        image.size[1],
        image.size[0],
        3
    ))

    # Convert it to "RGB"
    return cv2.cvtColor(
        image_np,
        cv2.COLOR_BGR2RGB
    )


class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__(self, window_title="The Witcher.*"):
        """Constructor"""
        self._handle = None
        self._window_title = window_title

        # Tricked the code
        # self.find_window_wildcard(self._window_title)
        with open('main/resources/templates/config.json') as f:
            cfg = json.load(f)
            self._combat_poi = [y for x in cfg['combatPoi'] for y in x]
            self._gather_poi = [y for x in cfg['gatherPoi'] for y in x]
            self._loot_poi = [y for x in cfg['lootPoi'] for y in x]

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

        """put the window in the foreground"""
        win32gui.BringWindowToTop(self._handle)
        win32gui.ShowWindow(self._handle, win32con.SW_MAXIMIZE)

    def get_combat_area(self):
        """return the "Combat POI" area as a Numpy array"""
        return _img_2_np(ImageGrab.grab(self._combat_poi))

    def get_gather_area(self):
        """return the "Gather POI" area as a Numpy array"""
        return _img_2_np(ImageGrab.grab(self._gather_poi))

    def get_loot_area(self):
        """return the "Loot POI" area as a Numpy array"""
        return _img_2_np(ImageGrab.grab(self._loot_poi))
