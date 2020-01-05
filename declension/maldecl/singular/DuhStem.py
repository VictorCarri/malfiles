from declension.maldecl.DeclensionGenerator import DeclensionGenerator

class DuhStem(DeclensionGenerator):
    def genAccusative(self, noun):
        return noun.replace(u"\u0d1f\u0d4d", u"\u0d1f\u0d4d\u0d1f\u0d3f\u0d28\u0d46")

    def genGenitive(self, noun):
        return noun.replace(u"\u0d1f\u0d4d", u"\u0d1f\u0d4d\u0d1f\u0d3f\u0d28\u0d4d\u0d31\u0d4d\u0d31\u0d46")

    def genDative(self, noun):
        return noun.replace(u"\u0d1f\u0d4d", u"\u0d1f\u0d4d\u0d1f\u0d3f\u0d28\u0d4d\u0d28\u0d4d")

    def genLocative(self, noun):
        return noun.replace(u"\u0d1f\u0d4d", u"\u0d1f\u0d4d\u0d1f\u0d3f\u0d7d")

    def genSociative(self, noun):
        return noun.replace(u"\u0d1f\u0d4d", u"\u0d1f\u0d4d\u0d1f\u0d3f\u0d28\u0d4b\u0d1f\u0d4d")

    def genInstrumental(self, noun):
        return noun.replace(u"\u0d1f\u0d4d", u"\u0d1f\u0d4d\u0d1f\u0d3f\u0d28\u0d3e\u0d7d")