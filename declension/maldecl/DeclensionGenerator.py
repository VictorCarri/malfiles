class DeclensionGenerator:
    def genNominative(self, noun):
        return noun

    def genAccusative(self, noun):
        return "Unknown accusative"

    def genGenitive(self, noun):
        return "Unknown genitive"

    def genDative(self, noun):
        return "Unknown dative"

    def genLocative(self, noun):
        return "Unknown locative"

    def genSociative(self, noun):
        return "Unknown sociative"

    def genInstrumental(self, noun):
        return "Unknown instrumental"

    def decline(self, noun):
        toReturn = {
            "Nominative": self.genNominative(noun),
            "Accusative": self.genAccusative(noun),
            "Genitive": self.genGenitive(noun),
            "Dative": self.genDative(noun),
            "Locative": self.genLocative(noun),
            "Sociative": self.genSociative(noun),
            "Instrumental": self.genInstrumental(noun)
        }
        #print("decline: noun = {1}, genNominative returned {0}\n\tClass name = {3}.{2}".format(toReturn["Nominative"], noun, self.__class__.__name__, self.__class__.__module__))
        return toReturn