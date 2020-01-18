# TW1 - AutoCombat
_An easy to use script to ease combat in "The Witcher" PC game._

## Pre-requisites
1. This script will only work on **Windows** machines.
2. Require you to have **Python 3** installed on your PC or laptop.
3. Require you to install all the **required modules** (Run `pip install -r requirements.txt`)
4. Also you will obviously need **The Witcher** PC game (The first one.)
5. This script only works in the **Over the shoulder** camera mode.
6. Before using it for the first time, you need to follow the steps explained in the **How to set it up** section.

## How to use it
To use it, just run `main.py` (Double click it) and **The Witcher** PC game.

Once you have them running, pressing the <kbd>⇥</kbd> key will cycle across the available modes:
* Sleep mode:
   * Initial mode, the script is waiting and not doing anything.
* Combat mode:
   * Just by looking to an enemy, the script will engage in combat and do all the combos for you.
   * **Remember:** Choose the correct weapon/style for each enemy.
* Loot mode:
   * Just by looking to a lootable, the script will go to it and picl all the items it contains.

## How to set it up
### Introduction:
Using this script is very easy, but requires some set-up and config in order to properly work on your side.

### Step 1: Gather all the required images.
Every screen is different, that's why the first step is to gather several screenshots taken in the PC or laptop where you are going to be playing.

To do it, run `main_screenshot.py` and start **The Witcher** PC game.

While `main_screenshot.py` is running, every time you press the <kbd>⇥</kbd> key, a new screenshot will be saved to the folder `main/resources/calibration`.

You will need screenshots of the following situations (4 to 6 for each situation):

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

**NOTE:** Remember to delete all the old images of that folders and take extra care of putting all the images in the correct folder.

Once you have done it, just run `main_calibration.py` and follow the on-screen instructions.
