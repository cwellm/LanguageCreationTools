from languagecreationtools.linguistic_components.ipa import IPAVowel, IPAConsonant

IPALetterInventory = [
    # ---------------------------------------
    # Plosives
    # ---------------------------------------
    IPAConsonant("bilabial_plosive_unvoiced", "p", "\u0070", [
        "plosive",
        "bilabial"
    ]),
    IPAConsonant("bilabial_plosive_voiced", "b", "\u0062", [
        "plosive",
        "bilabial",
        "voiced"
    ]),
    # ----------------------------------
    IPAConsonant("dental_plosive_unvoiced", "t°", "\u0074" + "\u032A", [
        "plosive",
        "dental"
    ]),
    IPAConsonant("dental_plosive_voiced", "d°", "\u0064" + "\u032A", [
        "plosive",
        "dental",
        "voiced"
    ]),
    # ----------------------------------
    IPAConsonant("alveolar_plosive_unvoiced", "t", "\u0074", [
        "plosive",
        "alveolar",
        "dental",
        "postalveolar"
    ]),
    IPAConsonant("alveolar_plosive_voiced", "d", "\u0064", [
        "plosive",
        "alveolar",
        "voiced",
        "dental",
        "postalveolar"
    ]),
    # ----------------------------------
    IPAConsonant("retroflex_plosive_unvoiced", "t*", "\u0288", [
        "plosive",
        "retroflex"
    ]),
    IPAConsonant("retroflex_plosive_voiced", "d*", "\u0256", [
        "plosive",
        "retroflex",
        "voiced"
    ]),
    # ----------------------------------
    IPAConsonant("palatal_plosive_unvoiced", "c", "\u0063", [
        "plosive",
        "palatal"
    ]),
    IPAConsonant("palatal_plosive_voiced", "c.", "\u025F", [
        "plosive",
        "palatal",
        "voiced"
    ]),
    # ----------------------------------
    IPAConsonant("velar_plosive_unvoiced", "k", "\u006B", [
        "plosive",
        "velar"
    ]),
    IPAConsonant("velar_plosive_voiced", "g", "\u0261", [
        "plosive",
        "velar",
        "voiced"
    ]),
    # ----------------------------------
    IPAConsonant("uvular_plosive_unvoiced", "q", "\u0071", [
        "plosive",
        "uvular"
    ]),
    IPAConsonant("uvular_plosive_voiced", "q.", "\u0262", [
        "plosive",
        "uvular",
        "voiced"
    ]),
    # ----------------------------------
    IPAConsonant("glottal_plosive_unvoiced", "'", "\u0294", [
        "plosive",
        "glottal"
    ]),
    # ---------------------------------------
    # Implosive
    # ---------------------------------------
    IPAConsonant("bilabial_implosive", "p°", "\u0253" + "\u0325", [
        "implosive",
        "bilabial"
    ]),
    IPAConsonant("bilabial_implosive_voiced", "b°", "\u0253", [
        "implosive",
        "alveolar",
        "voiced"
    ]),
    # ----------------------------------
    IPAConsonant("alveolar_implosive_voiced", "d+", "\u0257", [
        "implosive",
        "alveolar",
        "voiced"
    ]),
    # ----------------------------------
    IPAConsonant("velar_implosive_voiced", "g+", "\u0260", [
        "implosive",
        "velar",
        "voiced"
    ]),
    # ---------------------------------------
    # Nasal
    # ---------------------------------------
    IPAConsonant("bilabial_nasal_voiced", "m", "\u006D", [
        "nasal",
        "bilabial",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("labiodental_nasal_voiced", "m*", "\u0271", [
        "nasal",
        "labiodental",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("alveolar_nasal_voiced", "n", "\u006E", [
        "nasal",
        "dental",
        "voiced",
        "alveolar",
        "postalveolar"
    ]),
    # ---------------------------------------
    IPAConsonant("palatal_nasal_voiced", "n*", "\u0272", [
        "nasal",
        "palatal",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("velar_nasal_voiced", "n+", "\u014B", [
        "nasal",
        "velar",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("uvular_nasal_voiced", "n~", "\u0274", [
        "nasal",
        "uvular",
        "voiced"
    ]),
    # ---------------------------------------
    # Trills
    # ---------------------------------------
    IPAConsonant("bilabial_trill_voiced", "B", "\u0299", [
        "trill",
        "bilabial",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("alveolar_trill_voiced", "r", "\u0072", [
        "trill",
        "alveolar",
        "voiced",
        "dental",
        "postalveolar"
    ]),
    # ---------------------------------------
    IPAConsonant("uvular_trill_voiced", "R", "\u0280", [
        "trill",
        "uvular",
        "voiced"
    ]),
    # ---------------------------------------
    # Taps
    # ---------------------------------------
    IPAConsonant("alveolar_tap_voiced", "r+", "\u027E", [
        "tap",
        "alveolar",
        "voiced",
        "dental",
        "postalveolar"
    ]),
    # ---------------------------------------
    IPAConsonant("retroflex_tap_voiced", "r*", "\u027D", [
        "tap",
        "retroflex",
        "voiced"
    ]),
    # ---------------------------------------
    # Fricatives
    # ---------------------------------------
    IPAConsonant("labiodental_fricative_unvoiced", "f", "\u0066", [
        "fricative",
        "labiodental"
    ]),
    IPAConsonant("labiodental_fricative_voiced", "v", "\u0076", [
        "fricative",
        "labiodental",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("dental_fricative_unvoiced", "D", "\u03B8", [
        "fricative",
        "dental"
    ]),
    IPAConsonant("dental_fricative_voiced", "D.", "\u00F0", [
        "fricative",
        "dental",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("alveolar_fricative_unvoiced", "s", "\u0073", [
        "fricative",
        "alveolar"
    ]),
    IPAConsonant("alveolar_fricative_voiced", "z", "\u007A", [
        "fricative",
        "alveolar",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("postalveolar_fricative_unvoiced", "S", "\u0283", [
        "fricative",
        "postalveolar"
    ]),
    IPAConsonant("postalveolar_fricative_voiced", "S.", "\u0292", [
        "fricative",
        "postalveolar",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("retroflex_fricative_unvoiced", "S+", "\u0282", [
        "fricative",
        "retroflex"
    ]),
    IPAConsonant("retroflex_fricative_voiced", "S+.", "\u0290", [
        "fricative",
        "retroflex",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("palatal_fricative_unvoiced", "C", "\u00E7", [
        "fricative",
        "palatal"
    ]),
    IPAConsonant("palatal_fricative_voiced", "C.", "\u029D", [
        "fricative",
        "palatal",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("velar_fricative_unvoiced", "x", "\u0078", [
        "fricative",
        "velar"
    ]),
    IPAConsonant("velar_fricative_voiced", "x.", "\u0263", [
        "fricative",
        "velar",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("uvular_fricative_unvoiced", "X", "\u03C7", [
        "fricative",
        "uvular"
    ]),
    IPAConsonant("uvular_fricative_voiced", "X.", "\u0281", [
        "fricative",
        "uvular",
        "voiced"
    ]),
    # ---------------------------------------
    # Lateral Fricatives
    # ---------------------------------------
    IPAConsonant("alveolar_lateral_fricative_unvoiced", "l*", "\u026C", [
        "lateral_fricative",
        "alveolar",
        "dental",
        "postalveolar"
    ]),
    IPAConsonant("alveolar_lateral_fricative_voiced", "l*.", "\u026E", [
        "lateral_fricative",
        "alveolar",
        "dental",
        "postalveolar",
        "voiced"
    ]),
    # ---------------------------------------
    # Approximants
    # ---------------------------------------
    IPAConsonant("alveolar_approximant_voiced", "r-", "\u0279", [
        "approximant",
        "alveolar",
        "dental",
        "postalveolar",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("retroflex_approximant_voiced", "r--", "\u027B", [
        "approximant",
        "retroflex",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("palatal_approximant_voiced", "j", "\u006A", [
        "approximant",
        "palatal",
        "voiced"
    ]),
    # ---------------------------------------
    IPAConsonant("velar_approximant_voiced", "j*", "\u0270", [
        "approximant",
        "velar",
        "voiced"
    ]),
    # ---------------------------------------
    # Lateral Approximants
    # ---------------------------------------
    IPAConsonant("alveolar_lateral_approximant_unvoiced", "l", "\u0234", [
        "lateral_approximant",
        "alveolar",
        "dental",
        "postalveolar"
    ]),
]