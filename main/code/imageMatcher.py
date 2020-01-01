# Third party imports
import cv2 as cv


class ImageMatcher:
    """Encapsulates the image recognition process"""

    def __init__(self, path_to_resources="main/resources/templates"):
        """Constructor"""
        # Read the "gather" template and its mask
        self._gather_template = cv.imread(path_to_resources + '/gather_template.png', cv.IMREAD_COLOR)
        self._gather_mask = cv.imread(path_to_resources + '/gather_mask.png', cv.IMREAD_COLOR)

        # Read the "combatCombo" template and its mask
        self._combat_combo_template = cv.imread(path_to_resources + '/combatCombo_template.png', cv.IMREAD_COLOR)
        self._combat_combo_mask = cv.imread(path_to_resources + '/combatCombo_mask.png', cv.IMREAD_COLOR)

        # Read the "startCombat" template and its mask
        self._start_combat_template = cv.imread(path_to_resources + '/startCombat_template.png', cv.IMREAD_COLOR)
        self._start_combat_mask = cv.imread(path_to_resources + '/startCombat_mask.png', cv.IMREAD_COLOR)

    def is_gather(self, image, threshold=0.1):
        """Returns True if the image contains the "Gather" icon, False otherwise."""
        return cv.matchTemplate(
            image,
            self._gather_template,
            cv.TM_SQDIFF,
            mask=self._gather_mask
        ).min() < threshold

    def is_combat_combo(self, image, threshold=4):
        """Returns True if the image contains the "Combat combo" icon, False otherwise."""
        return cv.matchTemplate(
            image=image,
            templ=self._combat_combo_template,
            method=cv.TM_SQDIFF,
            mask=self._combat_combo_mask
        ).min() < threshold

    def is_start_combat(self, image, threshold=0.1):
        """Returns True if the image contains the "Start combo" icon, False otherwise."""
        return cv.matchTemplate(
            image,
            self._start_combat_template,
            cv.TM_SQDIFF,
            mask=self._start_combat_mask
        ).min() < threshold
