# Standard library imports
import os

# Third party imports
import cv2 as cv
import numpy as np
from PIL import Image


class FeatureExtractor:
    """Encapsulates the feature extraction process"""

    def __init__(self, path_to_resources, corners):
        """Constructor"""
        self._path_to_resources = path_to_resources
        _, _, self._files = next(os.walk(path_to_resources))
        self._corners = corners

    def _get_cropped_image(self, file_name):
        img = cv.imread(
            self._path_to_resources + '/' + file_name,
            cv.IMREAD_COLOR
        )
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        return img[self._corners[0][1]:self._corners[1][1], self._corners[0][0]:self._corners[1][0]]

    def get_feature_images(self):
        # Initialize using the reference image
        reference_img = self._get_cropped_image(self._files[0])
        common_px = np.ones_like(reference_img) == 1

        # Iterate over all the files
        for file in self._files[1:]:
            # Get the new image and common values
            new_img = self._get_cropped_image(file)
            new_common_px = np.isclose(reference_img, new_img, rtol=0, atol=2)

            # Update old values
            common_px = np.logical_and(common_px, new_common_px)
            reference_img = new_img

        # Get the px common to al channels
        all_px_equal = np.logical_and(np.logical_and(common_px[:, :, 0], common_px[:, :, 1]), common_px[:, :, 2])
        all_px_equal = np.array([all_px_equal, all_px_equal, all_px_equal]).swapaxes(0, 2).swapaxes(0, 1)

        # Generate the mask
        array_mask = np.where(all_px_equal, 255, 0)
        img_mask = Image.fromarray(np.uint8(array_mask), 'RGB')

        # Generate the template
        array_template = np.where(all_px_equal, reference_img, 0)
        img_template = Image.fromarray(np.uint8(array_template), 'RGB')

        return img_template, img_mask
