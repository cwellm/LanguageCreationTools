import random

from languagecreationtools.config.config_parser import LanguageConfigParser


def __str_to_list(input_str):
    """
    Generates a list from a string of the form '["a", "b", ...]'
    :param input_str: input string
    :return: list of the form ["a", "b", ...]
    """
    str_without_braces = input_str[1:-1]
    str_list = str_without_braces.split(",")
    for i in range(len(str_list)):
        str_list[i] = str_list[i].replace("\"", "").strip()

    return str_list


def __generate_syllable(syllable_option_list):
    syllable = []
    for item in syllable_option_list:
        option_no = random.randrange(len(item))
        chosen = item[option_no]
        if (chosen):
            syllable.append(item[option_no])
    return syllable


def prepare_syllable_structure_input(no_words) -> dict:
    """
    Generates the input syllable structures which are parsed from the syllable structure options.
    First, it determines what are the possibilities at all (e.g. (C)V could be [CV, V]), then it determines the
    word length between min. and max. syllable number per word, taking randomly one of the above syllable structure
    possibilities for each new syllable. If there are special letters given, e.g. an optional structure like
    V([a,b]), then V and V[a,b] are given as options input.
    :param no_words: number of words for which syllable structures should be generated
    :return: dict of list of lists of syllable structures (dict: word no. i, outer list: all syllables of word;
    inner list: syllable structure of one syllable)
    """
    config_parser = LanguageConfigParser()
    general_syllable_options = config_parser.syllable_structure().get("general")

    syllable_option_list = []
    bracket_open_pos = -1
    parentheses_open_pos = -1
    for i, letter in enumerate(general_syllable_options):
        if letter == "(":
            parentheses_open_pos = i
            if not general_syllable_options[i+1] == "[":
                syllable_option_list.append([general_syllable_options[i+1], ""])
        elif letter == "[":
            bracket_open_pos = i
        elif letter == "]":
            if not i == (len(general_syllable_options) - 1):
                listized_str = __str_to_list(general_syllable_options[bracket_open_pos:(i+1)])
                if not general_syllable_options[i+1] == ")":
                    syllable_option_list.append(listized_str)
                else:
                    listized_str.append("")
                    syllable_option_list.append(listized_str)
            else:
                listized_str = __str_to_list(general_syllable_options[bracket_open_pos:(i + 1)])
                syllable_option_list.append(listized_str)
            bracket_open_pos = -1
        elif letter == ")":
            parentheses_open_pos = -1
        else:
            if parentheses_open_pos < 0 and bracket_open_pos < 0:
                syllable_option_list.append([general_syllable_options[i]])

    # --- now, generate actual syllable structure for new words ---
    max_word_length = config_parser.max_word_length()
    min_word_length = config_parser.min_word_length()
    all_words = {}
    for word_i in range(no_words):
        # first, determine word length
        word_length = random.randrange(min_word_length, max_word_length+1)
        syllable_structure = []

        # Now, use algorithm for each syllable
        for _ in range(word_length):
            syllable_structure.append(__generate_syllable(syllable_option_list))

        all_words[word_i] = syllable_structure

    return all_words
