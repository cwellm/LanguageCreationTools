from languagecreationtools.config.config_parser import LanguageConfigParser
from languagecreationtools.processing.preprocessing import prepare_syllable_structure_input

if __name__ == "__main__":
    a = prepare_syllable_structure_input(10)
    print(a)