from logging import Logger
import os
import glob

from TTS.api import TTS


class SpeechGenerator:

    def __init__(self, logger: Logger, output_dir="./redditext-frontend/public"):
        self.__logger = logger
        self.__output_dir = output_dir
        self.__tts = TTS(
            model_name="tts_models/multilingual/multi-dataset/your_tts",
            progress_bar=False,
            gpu=False
        )

    def generate_speech(self, text):

        self.__delete_wavs()

        new_text = text[0:5].replace(' ', '_').replace('.', '').lower()
        file = f'{self.__output_dir}/{new_text}.wav'

        self.__tts.tts_to_file(
            text,
            speaker_wav="./redditext/audio/nick_longer.wav",
            language="en",
            file_path=file
        )

        return new_text

    def __delete_wavs(self):
        try:
            wav_files = glob.glob(os.path.join(self.__output_dir, "*.wav"))
            for wav_file in wav_files:
                os.remove(wav_file)
                self.__logger.info(f"{wav_file} was successfully deleted.")

        except OSError as e:
            self.__logger.error(f"Error: WAV files in {self.__output_dir} could not be deleted - {e}")

