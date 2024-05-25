# LanguageCreationTools
Some tools which can help one to create one's own language, featuring different aspects of language.

The [program config](./languagecreationtools/program_config.yaml) defines how the program would create a new
suggested language, i.e. which resources it draws from (full text or set of rules, for instance),
and which algorithms it uses to come up with new words.

The [language config](./languagecreationtools/specific_language/language_config.yaml), on the other hand, defines
the specific language itself. It comprises the input (syllables, full text, ...) for the generators
and algorithms.

## To-Dos

## Open Questions

- treating ejectives as consonant + glottal stop + vocal?