from declension.maldecl.DeclensionGenerator import DeclensionGenerator

class ANStem(DeclensionGenerator):
    def genAccusative(self, noun):
        # Replace trailing chillu with -ne
        return noun.replace(u"\u0d6f", u"\u0d28\u0d46")

    def genGenitive(self, noun):
        # Append -rre
        return noun + u"\u0d31\u0d4d\u0d31\u0d46"

    def genDative(self, noun):
        # Replace chillu with -nnuh
        return noun.replace(u"\u0d6f", u"\u0d28\u0d4d\u0d28\u0d4d")

    def genLocative(self, noun):
        # Replace chillu with -nil
        return noun.replace(u"\u0d6f", u"\u0d28\u0d3f\u0d7d")

    def genInstrumental(self, noun):
        # Replace chillu with -naal
        return noun.replace(u"\u0d6f", u"\u0d28\u0d3e\u0d7d")

    def genSociative(self, noun):
        return noun.replace(u"\u0d6f", u"\u0d28\u0d3e\u0d7d")