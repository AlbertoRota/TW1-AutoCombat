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


def _save_images(name, poi):
    img_template, img_mask = FeatureExtractor(
        'main/resources/calibration/' + name, poi
    ).get_feature_images()
    img_template.save('main/resources/templates/' + name + '_template.png')
    img_mask.save('main/resources/templates/' + name + '_mask.png')


def process_combat(cfg):
    # Process the "combatCombo", "startCombat", "combatComboSilver" and "startCombatSilver" together.
    sc_poi = PoiExtractor('main/resources/calibration/startCombat').get_poi_corners()
    cc_poi = PoiExtractor('main/resources/calibration/combatCombo').get_poi_corners()
    scs_poi = PoiExtractor('main/resources/calibration/startCombatSilver').get_poi_corners()
    ccs_poi = PoiExtractor('main/resources/calibration/combatComboSilver').get_poi_corners()
    cfg['combatPoi'] = PoiExtractor.merge_pois((sc_poi, cc_poi, scs_poi, ccs_poi))

    # Generate the "Template" and "Mask" files.
    _save_images('startCombat', cfg['combatPoi'])
    _save_images('combatCombo', cfg['combatPoi'])
    _save_images('startCombatSilver', cfg['combatPoi'])
    _save_images('combatComboSilver', cfg['combatPoi'])


def process_gather(cfg):
    # Process the "gather".
    cfg['gatherPoi'] = PoiExtractor('main/resources/calibration/gather').get_poi_corners()
    _save_images('gather', cfg['gatherPoi'])


def process_loot(cfg):
    # Process the "loot".
    cfg['lootPoi'] = PoiExtractor('main/resources/calibration/loot').get_poi_corners()
    _save_images('loot', cfg['lootPoi'])


if __name__ == '__main__':
    main()
