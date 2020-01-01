# Standard library imports
import unittest
import sys
import os

# Third party imports
import cv2

# Local application imports (Adding the root of the project to the path)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from main.code.imageMatcher import ImageMatcher


class TestImageMatcher(unittest.TestCase):

    def setUp(self):
        self._im = ImageMatcher(path_to_resources='../../main/resources/templates')

    def test_is_gather_returns_true_if_match(self):
        path = '../resources/gather/positives'
        _, _, files = next(os.walk(path))
        for file in files:
            self.assertTrue(self._im.is_gather(cv2.imread(path + '/' + file, cv2.IMREAD_COLOR)))

    def test_is_gather_returns_false_if_no_match(self):
        path = '../resources/gather/negatives'
        _, _, files = next(os.walk(path))
        for file in files:
            self.assertFalse(self._im.is_gather(cv2.imread(path + '/' + file, cv2.IMREAD_COLOR)))

    def test_is_combat_combo_returns_true_if_match(self):
        path = '../resources/combatCombo/positives'
        _, _, files = next(os.walk(path))
        for file in files:
            self.assertTrue(self._im.is_combat_combo(cv2.imread(path + '/' + file, cv2.IMREAD_COLOR)))

    def test_is_combat_combo_returns_false_if_not_match(self):
        path = '../resources/combatCombo/negatives'
        _, _, files = next(os.walk(path))
        for file in files:
            self.assertFalse(self._im.is_combat_combo(cv2.imread(path + '/' + file, cv2.IMREAD_COLOR)))

    def test_is_start_combat_returns_true_if_match(self):
        path = '../resources/startCombat/positives'
        _, _, files = next(os.walk(path))
        for file in files:
            self.assertTrue(self._im.is_start_combat(cv2.imread(path + '/' + file, cv2.IMREAD_COLOR)))

    def test_is_start_combat_returns_false_if_no_match(self):
        path = '../resources/startCombat/negatives'
        _, _, files = next(os.walk(path))
        for file in files:
            self.assertFalse(self._im.is_start_combat(cv2.imread(path + '/' + file, cv2.IMREAD_COLOR)))
