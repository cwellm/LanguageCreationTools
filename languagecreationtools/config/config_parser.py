import pathlib
import yaml

LANGUAGE_CONFIG = str(pathlib.Path(__file__).parent.parent / "specific_language" / "language_config.yaml")


class LanguageConfigParser:

    def __init__(self):
        self.yaml_obj = self.__load_yaml_as_obj()

    def syllable_structure(self):
        return self.yaml_obj.get("syllable_structure")

    def max_word_length(self):
        return int(self.yaml_obj.get("parameters").get("max_word_length"))

    def min_word_length(self):
        return int(self.yaml_obj.get("parameters").get("min_word_length"))

    def __load_yaml_as_obj(self):
        with open(LANGUAGE_CONFIG, "r") as file:
            yaml_obj = yaml.safe_load(file)
        return yaml_obj
