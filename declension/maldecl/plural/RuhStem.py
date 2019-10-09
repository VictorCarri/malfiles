from declension.maldecl.DeclensionGenerator import DeclensionGenerator

class RuhStem(DeclensionGenerator):
    def genNominative(self, noun):
        return noun + "\u0d15\u0d7e"

    def genAccusative(self, noun):
        return noun + "\u0d15\u0d33\u0d46"

    def genGenitive(self, noun):
        return noun + "\u0d15\u0d33\u0d41\u0d1f\u0d46"

    def genDative(self, noun):
        return noun + "\u0d15\u0d7e\u0d15\u0d4d\u0d15\u0d4d"

    def genLocative(self, noun):
        return noun + "\u0d15\u0d33\u0d3f\u0d7d"

    def genSociative(self, noun):
        return noun + "\u0d15\u0d33\u0d4b\u0d1f\u0d4d"

    def genInstrumental(self, noun):
        return noun + "\u0d15\u0d33\u0d3e\u0d7d"