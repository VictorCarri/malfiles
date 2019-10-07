from declension.maldecl import DeclensionGenerator

class VowelStem(DeclensionGenerator):
    def __init__(self):
        pass

    def genAccusative(self, noun):
        return noun + "\u0d2f\u0d46"

    def genGenitive(self, noun):
        return noun + "\u0d2f\u0d41\u0d1f\u0d46"

    def genDative(self, noun):
        return noun + "\u0d15\u0d4d\u0d15\u0d4d"

    def genLocative(self, noun):
        return noun + "\u0d2f\u0d3f\u0d7d"

    def genSociative(self, noun):
        return noun + "\u0d2f\u0d4b\u0d41\u0d4d"

    def genInstrumental(self, noun):
        return noun + "\u0d2f\u0d3e\u0d7d"

    def genSociative(self, noun):
        return noun + "\u0d2f\u0d4b\u0d1f\u0d4d"