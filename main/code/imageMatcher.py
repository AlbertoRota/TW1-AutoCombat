# Third party imports
import cv2 as cv


class ImageMatcher:
    """Encapsulates the image recognition process"""

    def __init__(self, path_to_resources="main/resources/templates"):
        """Constructor"""
        # Read the "gather" template and its mask
        self._gather_template = cv.imread(path_to_resources + '/gather_template.png', cv.IMREAD_COLOR)
        self._gather_mask = cv.imread(path_to_resources + '/gather_mask.png', cv.IMREAD_COLOR)

        # Read the "loot" template and its mask
        self._loot_template = cv.imread(path_to_resources + '/loot_template.png', cv.IMREAD_COLOR)
        self._loot_mask = cv.imread(path_to_resources + '/loot_mask.png', cv.IMREAD_COLOR)

        # Read the "combatCombo" template and its mask
        self._cc_template = cv.imread(path_to_resources + '/combatCombo_template.png', cv.IMREAD_COLOR)
        self._cc_mask = cv.imread(path_to_resources + '/combatCombo_mask.png', cv.IMREAD_COLOR)

        # Read the "combatComboSilver" template and its mask
        self._ccs_template = cv.imread(path_to_resources + '/combatComboSilver_template.png', cv.IMREAD_COLOR)
        self._ccs_mask = cv.imread(path_to_resources + '/combatComboSilver_mask.png', cv.IMREAD_COLOR)

        # Read the "startCombat" template and its mask
        self._sc_template = cv.imread(path_to_resources + '/startCombat_template.png', cv.IMREAD_COLOR)
        self._sc_mask = cv.imread(path_to_resources + '/startCombat_mask.png', cv.IMREAD_COLOR)

        # Read the "startCombatSilver" template and its mask
        self._scs_template = cv.imread(path_to_resources + '/startCombatSilver_template.png', cv.IMREAD_COLOR)
        self._scs_mask = cv.imread(path_to_resources + '/startCombatSilver_mask.png', cv.IMREAD_COLOR)

    def is_gather(self, image, threshold=0.1):
        """Returns True if the image contains the "Gather" icon, False otherwise."""
        return cv.matchTemplate(
            image,
            self._gather_template,
            cv.TM_SQDIFF,
            mask=self._gather_mask
        ).min() < threshold

    def is_loot(self, image, threshold=0.1):
        """Returns True if the image contains the "Loot" icon, False otherwise."""
        return cv.matchTemplate(
            image,
            self._loot_template,
            cv.TM_SQDIFF,
            mask=self._loot_mask
        ).min() < threshold

    def is_combat(self, image):
        """Returns True if the image contains any of the "Combat" icons, False otherwise."""
        return self._is_start_combat(image) \
               or self._is_start_combat_silver(image) \
               or self._is_combat_combo(image) \
               or self._is_combat_combo_silver(image)

    def _is_combat_combo(self, image, threshold=4):
        """Returns True if the image contains the "Combat combo" icon, False otherwise."""
        return cv.matchTemplate(
            image=image,
            templ=self._cc_template,
            method=cv.TM_SQDIFF,
            mask=self._cc_mask
        ).min() < threshold

    def _is_combat_combo_silver(self, image, threshold=4):
        """Returns True if the image contains the "Combat combo silver" icon, False otherwise."""
        return cv.matchTemplate(
            image=image,
            templ=self._ccs_template,
            method=cv.TM_SQDIFF,
            mask=self._ccs_mask
        ).min() < threshold

    def _is_start_combat(self, image, threshold=0.1):
        """Returns True if the image contains the "Start combat" icon, False otherwise."""
        return cv.matchTemplate(
            image,
            self._sc_template,
            cv.TM_SQDIFF,
            mask=self._sc_mask
        ).min() < threshold

    def _is_start_combat_silver(self, image, threshold=0.1):
        """Returns True if the image contains the "Start combat silver" icon, False otherwise."""
        return cv.matchTemplate(
            image,
            self._scs_template,
            cv.TM_SQDIFF,
            mask=self._scs_mask
        ).min() < threshold
