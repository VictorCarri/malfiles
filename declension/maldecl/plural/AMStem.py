from declension.maldecl.SingularDeclensionGenerator import SingularDeclensionGenerator

class AMStem(SingularDeclensionGenerator):
    def genNominative(self, noun):
        return noun.replace(u"\u0d02", u"\u0d19\u0d4d\u0d19\u0d7e")

    def genAccusative(self, noun):
        # Replace trailing am with -ngngaLe
        return noun.replace(u"\u0d02", u"\u0d19\u0d4d\u0d19\u0d33\u0d46")

    def genGenitive(self, noun):
        # Replace trailing -am with -ngngaLuTe
        return noun.replace(u"\u0d02", u"\u0d19\u0d4d\u0d19\u0d33\u0d41\u0d1f\u0d46")

    def genDative(self, noun):
        # Replace trailing -am with -ngngaLkkuh
        return noun.replace(u"\u0d02", u"\u0d19\u0d4d\u0d19\u0d7e\u0d15\u0d4d\u0d15")

    def genLocative(self, noun):
        # Replace trailing -am with -ngngaLil
        return noun.replace(u"\u0d02", u"\u0d19\u0d4d\u0d19\u0d33\u0d3f\u0d7d")

    def genInstrumental(self, noun):
        # Replace trailing -am with -ngngaLaal
        return noun.replace(u"\u0d02", u"\u0d19\u0d4d\u0d19\u0d33\u0d3e\u0d7d")

    def genSociative(self, noun):
        return noun.replace(u"\u0d02", u"\u0d19\u0d4d\u0d19\u0d33\u0d4b\u0d1f\u0d4d")