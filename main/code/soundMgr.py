# Standard library imports
import winsound


class SoundMgr:
    """Encapsulates calls to the winsound for sound management"""

    def __init__(self, path_to_resources="main/resources/sounds"):
        """Constructor"""
        self._path_to_resources = path_to_resources
        self._boot_up_audio = path_to_resources + '/bootUp.wav'
        self._mode_audios = {
            'combatMode': path_to_resources + '/combatMode.wav',
            'lootMode': path_to_resources + '/lootMode.wav',
            'sleepMode': path_to_resources + '/sleepMode.wav'
        }
        self._shut_down_audio = path_to_resources + '/shutDown.wav'

    def play_boot_up_audio(self):
        """plays the boot up audio"""
        winsound.PlaySound(self._boot_up_audio, winsound.SND_FILENAME)

    def play_mode_audio(self, mode):
        """plays the mode audio"""
        winsound.PlaySound(self._mode_audios[mode], winsound.SND_FILENAME | winsound.SND_ASYNC)

    def play_shut_down_audio(self):
        """plays the shut down audio"""
        winsound.PlaySound(self._shut_down_audio, winsound.SND_FILENAME)
