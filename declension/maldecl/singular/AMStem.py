from declension.maldecl.DeclensionGenerator import DeclensionGenerator

class AMStem(DeclensionGenerator):
    def genAccusative(self, noun):
        # Replace trailing am with -ttine
        return noun.replace(u"\u0d02", u"\u0d24\u0d4d\u0d24\u0d3f\u0d28\u0d46")

    def genGenitive(self, noun):
        # Replace trailing -am with -ttinte
        return noun.replace(u"\u0d02", u"\u0d24\u0d4d\u0d24\u0d3f\u0d7b\u0d31\u0d4d\u0d31\u0d46")

    def genDative(self, noun):
        # Replace trailing -am with -ttinnuh
        return noun.replace(u"\u0d02", u"\u0d24\u0d4d\u0d24\u0d3f\u0d28\u0d4d\u0d28\u0d4d")

    def genLocative(self, noun):
        # Replace trailing -am with -ttil
        return noun.replace(u"\u0d02", u"\u0d24\u0d4d\u0d24\u0d3f\u0d7d")

    def genInstrumental(self, noun):
        # Replace trailing -am with -ttinaal
        return noun.replace(u"\u0d02", u"\u0d24\u0d4d\u0d24\u0d3f\u0d28\u0d3e\u0d7d")

    def genSociative(self, noun):
        return noun.replace(u"\u0d02", u"\u0d24\u0d4d\u0d24\u0d3f\u0d28\u0d4b\u0d1f\u0d4d")
