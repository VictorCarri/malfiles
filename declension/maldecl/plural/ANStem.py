from declension.maldecl.DeclensionGenerator import DeclensionGenerator

class ANStem(DeclensionGenerator):
    def genNominative(self, noun):
        return noun.replace(u"\u0d6f", u"\u0d7c")

    def genAccusative(self, noun):
        # Replace trailing chillu with -re
        return noun.replace(u"\u0d6f", u"\u0d30\u0d46")

    def genGenitive(self, noun):
        # Append -rude
        return noun.replace(u"\u0d6f", u"\u0d30\u0d41\u0d1f\u0d46")

    def genDative(self, noun):
        # Replace chillu with -rkkuh
        return noun.replace(u"\u0d6f", u"\u0d7c\u0d15\u0d4d\u0d15\u0d4d")

    def genLocative(self, noun):
        # Replace chillu with -ril
        return noun.replace(u"\u0d6f", u"\u0d30\u0d3f\u0d7d")

    def genInstrumental(self, noun):
        # Replace chillu with -raal
        return noun.replace(u"\u0d6f", u"\u0d30\u0d3e\u0d7d")