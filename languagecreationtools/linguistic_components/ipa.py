from dataclasses import dataclass

class IPALetter(dict):
    ALLOWED_KEYS = ["name", "symbol", "unicode"]

    def __init__(self, name=None, symbol=None, unicode=None, properties: list=None):
        self.__name = name
        self.__symbol = symbol
        self.__unicode = unicode
        self._properties = {}
        self._set_properties(properties)
        dict.__setitem__(self, "name", self.__name)
        dict.__setitem__(self, "unicode", self.__unicode)
        dict.__setitem__(self, "symbol", self.__symbol)

    def __setitem__(self, key, val):
        if key not in self.ALLOWED_KEYS:
           raise KeyError("key: '" + str(key) + "' not in allowed keys: '" + str(self.ALLOWED_KEYS) + "'")
        dict.__setitem__(self, key, val)

    def _set_properties(self, properties):
        """
        Sets the respective properties to the value "val" where this is either True or False.
        :param properties: dict of properties, where the values are IPAProperty with corresponding
        truth value
        :return: None
        """
        if properties:
            for prop in properties:
                self._properties[prop] = IPAProperty(prop, True)

    def __repr__(self):
        dict_repr = dict.__repr__(self)
        prop_repr = self._properties
        actual_props = {prop: prop_repr[prop].enabled for prop in prop_repr if prop_repr[prop].enabled}
        return (dict_repr + "\nProperties: " + str(actual_props) + "\n")


    def get_properties(self):
        return self._properties

@dataclass(frozen=False)
class IPAProperty:
    def __init__(self, name: str, enabled: bool):
        self.__name = name
        self.__enabled = enabled

    @property
    def name(self):
        return self.__name

    @property
    def enabled(self):
        return self.__enabled

    def __repr__(self):
        return str(self.__enabled)


class IPAVowel(IPALetter):
    VOWEL_PROPERTIES = [
        "long",
        "front",
        "central",
        "back",
        "close",
        "close_mid",
        "open_mid",
        "open",
        "rounded",
        "near_close"
    ]

    def __init__(self, name=None, symbol=None, unicode=None, properties: list=None):
        super().__init__(name, symbol, unicode, properties)

    def _set_properties(self, properties):
        for prop in self.VOWEL_PROPERTIES:
            self._properties[prop] = IPAProperty(prop, False)
        super()._set_properties(properties)


class IPAConsonant(IPALetter):
    CONSONANT_PROPERTIES = [
        "plosive",
        "nasal",
        "trill",
        "flap",
        "fricative",
        "lateral_fricative",
        "approximant",
        "lateral_approximant",
        "voiced",
        "bilabial",
        "labiodental",
        "dental",
        "alveolar",
        "postalveolar",
        "retroflex",
        "palatal",
        "velar",
        "uvular",
        "pharyngeal",
        "glottal"
    ]

    def __init__(self, name=None, symbol=None, unicode=None, properties: list=None):
        super().__init__(name, symbol, unicode, properties)

    def _set_properties(self, properties):
        for prop in self.CONSONANT_PROPERTIES:
            self._properties[prop] = IPAProperty(prop, False)
        super()._set_properties(properties)


# ------------------------------------
from languagecreationtools.linguistic_components.ipa_alphabet import IPALetterInventory

class IPA:
    """
    This class represents the IPA (International Phonetic Alphabet). It is *not* meant to be complete, but rather,
    it will contain those elements which I, specifically, need, and possibly some more. IPA can be found under res
    folder, and in https://en.wikipedia.org/wiki/Phonetic_symbols_in_Unicode, there is a map from IPA symbols to
    unicode characters.
    """

    def __init__(self):
        self.current_letter = None
        self.letter_inventory = IPALetterInventory

    def to_unicode(self):
        """
        Returns the currently held letter as unicode character.
        :return:
        """
        pass

    def to_symbol(self):
        """
        Returns the currently held letter as symbol.
        :return:
        """
        pass

    def to_name(self):
        """
        Returns the name of the currently held letter.
        :return:
        """
        pass

    def __call__(self):
        pass