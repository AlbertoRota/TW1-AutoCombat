# Standard library imports
import os
import time

# Third party imports
import cv2


class DebugUtils:
    """Encapsulates the debug utils"""

    def __init__(self, debug=False):
        """Constructor"""
        self._debug = debug

    def debug_show_image(self, image):
        if self._debug:
            cv2.imshow("Image", image)
            cv2.waitKey(0)

    def debug_save_image(self, image, name='image'):
        if self._debug:
            cv2.imwrite(
                os.getcwd() + '\\' + name + '_' + str(int(time.time())) + '.png',
                image
            )
