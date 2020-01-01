# Standard library imports
import re
from time import sleep

# Third party imports
import numpy as np
import cv2
import win32gui
import win32con
from PIL import ImageGrab

# Constants
# ------------------
mouseWidth = 20
mouseHeight = 20
hOffset = 0


class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__(self, window_title="The Witcher.*"):
        """Constructor"""
        self._handle = None
        self._mouse_area = None
        self._window_title = window_title

        # Tricked the code
        # self.find_window_wildcard(self._window_title)
        # self._mouse_area = (624.0, 344.0, 656.0, 376.0)
        self._mouse_area = (630.0, 351.0, 650.0, 370.0)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

        self.set_foreground()

        dimensions = win32gui.GetWindowRect(self._handle)
        dimensions_width = dimensions[2] - dimensions[0]
        dimensions_height = dimensions[3] - dimensions[1] + hOffset

        self._mouse_area = (
            dimensions[0] + dimensions_width / 2 - mouseWidth / 2,
            dimensions[1] + dimensions_height / 2 - mouseHeight / 2,
            dimensions[0] + dimensions_width / 2 + mouseWidth / 2,
            dimensions[1] + dimensions_height / 2 + mouseHeight / 2
        )

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.BringWindowToTop(self._handle)
        win32gui.ShowWindow(self._handle, win32con.SW_MAXIMIZE)
        sleep(7) # Give time to the window

    def get_mouse_area(self):
        """return the mouse area as a Numpy array"""
        # Capture the target area
        image = ImageGrab.grab(self._mouse_area)

        # Convert it to NumPy
        image_np = np.array(
            image.getdata(),
            dtype='uint8'
        ).reshape((
            image.size[1],
            image.size[0],
            3
        ))

        # Convert it to "Gray scale"
        return cv2.cvtColor(
            image_np,
            cv2.COLOR_BGR2RGB
        )
