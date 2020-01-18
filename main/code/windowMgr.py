# Standard library imports
import json

# Third party imports
import numpy as np
import cv2
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

    def __init__(self):
        """Constructor"""
        with open('main/resources/templates/config.json') as f:
            cfg = json.load(f)
            self._combat_poi = [y for x in cfg['combatPoi'] for y in x]
            self._gather_poi = [y for x in cfg['gatherPoi'] for y in x]
            self._loot_poi = [y for x in cfg['lootPoi'] for y in x]

    def get_combat_area(self):
        """return the "Combat POI" area as a Numpy array"""
        return _img_2_np(ImageGrab.grab(self._combat_poi))

    def get_gather_area(self):
        """return the "Gather POI" area as a Numpy array"""
        return _img_2_np(ImageGrab.grab(self._gather_poi))

    def get_loot_area(self):
        """return the "Loot POI" area as a Numpy array"""
        return _img_2_np(ImageGrab.grab(self._loot_poi))
