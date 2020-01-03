# Standard library imports
import json

# Local application imports
from main.code.calibration.poiExtractor import PoiExtractor
from main.code.calibration.featureExtractor import FeatureExtractor


def main():
    cfg = {}

    process_combat(cfg)
    process_gather(cfg)
    process_loot(cfg)

    with open('main/resources/templates/config.json', 'w+') as out:
        json.dump(cfg, out, indent=2)


def process_combat(cfg):
    # Process the "combatCombo" and "startCombat" together.
    sc_poi = PoiExtractor('main/resources/calibration/startCombat').get_poi_corners()
    cc_poi = PoiExtractor('main/resources/calibration/combatCombo').get_poi_corners()
    combat_poi = (
        (min(sc_poi[0][0], cc_poi[0][0]), min(sc_poi[0][1], cc_poi[0][1])),
        (max(sc_poi[1][0], cc_poi[1][0]), max(sc_poi[1][1], cc_poi[1][1])),
    )
    cfg['combatPoi'] = combat_poi
    # Generate the "Template" and "Mask" files for "startCombat".
    sc_img_template, sc_img_mask = FeatureExtractor(
        'main/resources/calibration/startCombat', combat_poi
    ).get_feature_images()
    sc_img_template.save('main/resources/templates/startCombat_template.png')
    sc_img_mask.save('main/resources/templates/startCombat_mask.png')
    # Generate the "Template" and "Mask" files for "combatCombo".
    cc_img_template, cc_img_mask = FeatureExtractor(
        'main/resources/calibration/combatCombo', combat_poi
    ).get_feature_images()
    cc_img_template.save('main/resources/templates/combatCombo_template.png')
    cc_img_mask.save('main/resources/templates/combatCombo_mask.png')


def process_gather(cfg):
    # Process the "gather".
    gather_poi = PoiExtractor('main/resources/calibration/gather').get_poi_corners()
    cfg['gatherPoi'] = gather_poi
    # Generate the "Template" and "Mask" files for "gather".
    sc_img_template, sc_img_mask = FeatureExtractor(
        'main/resources/calibration/gather', gather_poi
    ).get_feature_images()
    sc_img_template.save('main/resources/templates/gather_template.png')
    sc_img_mask.save('main/resources/templates/gather_mask.png')


def process_loot(cfg):
    # Process the "loot".
    gather_poi = PoiExtractor('main/resources/calibration/loot').get_poi_corners()
    cfg['lootPoi'] = gather_poi
    # Generate the "Template" and "Mask" files for "loot".
    sc_img_template, sc_img_mask = FeatureExtractor(
        'main/resources/calibration/loot', gather_poi
    ).get_feature_images()
    sc_img_template.save('main/resources/templates/loot_template.png')
    sc_img_mask.save('main/resources/templates/loot_mask.png')


if __name__ == '__main__':
    main()
