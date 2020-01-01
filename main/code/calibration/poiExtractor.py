# Standard library imports
import os
import random
from math import ceil, floor

# Third party imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class PoiExtractor:
    """Encapsulates the POI extraction/selection process"""

    def __init__(self, path_to_resources):
        """Constructor"""
        self._path_to_resources = path_to_resources
        _, _, self._files = next(os.walk(path_to_resources))
        self._corners = None

    def _change_title(self, title):
        """Changes the title of the displayed image."""
        print(title)
        plt.title(title, fontsize=16)
        plt.draw()

    def get_poi_corners(self):
        """Interactively defines the corners of a POI"""
        # Init plot.
        plt.clf()
        plt.imshow(mpimg.imread(self._path_to_resources + "/" + random.choice(self._files)))
        self._change_title('You will define the area of interest, click to begin')
        plt.waitforbuttonpress()

        # Loop until user is satisfied
        while True:
            # Get the two corners
            self._change_title('Select top-left and bottom-right corners with mouse')
            corners = np.asarray(plt.ginput(2, timeout=-1))
            corners = (
                (floor(corners[0][0]), floor(corners[0][1])),
                (ceil(corners[1][0]), ceil(corners[1][1]))
            )

            # Show a preview of the selection
            ph = plt.fill(
                (corners[0][0], corners[0][0], corners[1][0], corners[1][0]),
                (corners[0][1], corners[1][1], corners[1][1], corners[0][1]),
                'r', lw=2
            )

            # Ask for confirmation
            self._change_title('Happy? Key click for yes, mouse click for no')
            if plt.waitforbuttonpress():
                self._corners = corners
                return self._corners
            else:
                # Get rid of fill
                for p in ph:
                    p.remove()
