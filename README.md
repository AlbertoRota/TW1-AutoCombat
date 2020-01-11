# TW1 - AutoCombat
_An easy to use script to ease combat in "The Witcher" PC game._

## How to use it:
### Introduction:
Using this script is very easy, but requires some set-up and config in order to properly work on your side.

This script will only work on **Windows** machines, and require you to have **Python** installed on your PC or laptop.

Also you will obviously need **The Witcher** PC game (The first one.)

### Step 1: Gather all the required images.
Every screen is different, that's why the first step is to gather several screenshots taken in the PC or laptop where you are going to be playing.

To do it, run `main_screenshot.py` and start **The Witcher** PC game.

While `main_screenshot.py` is running, every time you press the <kbd>⇥</kbd> key, a new screenshot will be saved to the folder `main/resources/calibration`.

You will need screenshots of the following situations:

* Start attack with the steel sword
    * See examples in `main/resources/calibration/startCombat`
* Combo attack with the steel sword
    * See examples in `main/resources/calibration/combatCombo`
* Start attack with the silver sword
    * See examples in `main/resources/calibration/startCombatSilver`
* Combo attack with the silver sword
    * See examples in `main/resources/calibration/combatComboSilver`
* Gather resource
    * See examples in `main/resources/calibration/gather`
* Looting menu
    * See examples in `main/resources/calibration/loot`

Once you have all the images, you can stop `main_screenshot.py` either by closing it or pressing the right <kbd>⇧</kbd> key.

### Step 2: Process all the required images.
Replace the contents of the following folders with the images you have obtained in the previous step:

* `main/resources/calibration/startCombat` -> Start attack with the steel sword
* `main/resources/calibration/combatCombo` -> Combo attack with the steel sword
* `main/resources/calibration/startCombatSilver` -> Start attack with the silver sword
* `main/resources/calibration/combatComboSilver` -> Combo attack with the silver sword
* `main/resources/calibration/gather` -> Gather resource
* `main/resources/calibration/loot` -> Looting menu

**NOTE:** Remember to delete all the old images of that folders and take extra care of putting all the images in the correcto folder.

Once you have done it, just run `main_calibration.py` and follow the on-screen instructions.
