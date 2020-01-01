# Local application imports
from main.code.calibration.poiExtractor import PoiExtractor
from main.code.calibration.featureExtractor import FeatureExtractor


def main():
    paths_and_names = [
        ('main/resources/calibration/combatCombo', 'combatCombo'),
        ('main/resources/calibration/startCombat', 'startCombat'),
        ('main/resources/calibration/gather', 'gather')
    ]

    for path, name in paths_and_names:
        # Extract the corners of the POI with user help.
        corners = PoiExtractor(path).get_poi_corners()
        print('Coords for "{0}" are: ({1})'.format(name, corners))

        # Generate the "Template" and "Mask" files.
        img_template, img_mask = FeatureExtractor(path, corners).get_feature_images()

        # Save files to the correct folder
        img_template.save('main/resources/templates/' + name + '_template.png')
        img_mask.save('main/resources/templates/' + name + '_mask.png')


if __name__ == '__main__':
    main()
