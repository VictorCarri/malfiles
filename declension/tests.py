from django.test import TestCase

from declension.maldecl.decline import decline


class AMStemTests(TestCase):
    def setUp(self):
        self.noun = "\u0d05\u0d24\u0d40\u0d24\u0d02" # atiiTam

    def testSingularNominative(self):
        declensions = decline(self.noun)
        self.assertEqual(declensions["Singular"]["Nominative"], self.noun, "The generated nominative singular should be the same as the given noun.")

    def testSingularAccusative(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d24\u0d40\u0d24\u0d24\u0d4d\u0d24\u0d3f\u0d28\u0d46"
        self.assertEqual(declensions["Singular"]["Accusative"], expectedVal, "The generated accusative singular should be {0}, but {1} was returned.".format(expectedVal, declensions["Singular"]["Accusative"]))

    def testSingularGenitive(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d24\u0d40\u0d24\u0d24\u0d4d\u0d24\u0d3f\u0d7b\u0d31\u0d4d\u0d31\u0d46"
        self.assertEqual(declensions["Singular"]["Genitive"], expectedVal, "The generated genitive singular should be {0}, but {1} was returned.".format(expectedVal, declensions["Singular"]["Genitive"]))

    def testSingularDative(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d24\u0d40\u0d24\u0d24\u0d4d\u0d24\u0d3f\u0d28\u0d4d\u0d28\u0d4d" # atiitattin_n_uh
        self.assertEqual(declensions["Singular"]["Dative"], expectedVal, "The generated dative singular should be {0}, but {1} was returned.".format(expectedVal, declensions["Singular"]["Dative"]))

    def testSingularLocative(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d24\u0d40\u0d24\u0d24\u0d4d\u0d24\u0d3f\u0d7d" # atiitattil
        self.assertEqual(declensions["Singular"]["Locative"], expectedVal, "The generated locative singular should be {0}, but {1} was returned.".format(expectedVal, declensions["Singular"]["Locative"]))

    def testSingularSociative(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d24\u0d40\u0d24\u0d24\u0d4d\u0d24\u0d3f\u0d28\u0d4b\u0d1f\u0d4d" # atiitattinooDuh
        self.assertEqual(declensions["Singular"]["Sociative"], expectedVal, "The generated sociative singular should be {0}, but {1} was returned.".format(expectedVal, declensions["Singular"]["Sociative"]))

    def testSingularInstrumental(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d24\u0d40\u0d24\u0d24\u0d4d\u0d24\u0d3f\u0d28\u0d3e\u0d7d" # atiitattinaal
        self.assertEqual(declensions["Singular"]["Instrumental"], expectedVal, "The generated instrumental singular should be {0}, but {1} was returned.".format(expectedVal, declensions["Singular"]["Instrumental"]))

    def testPluralNominative(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d24\u0d40\u0d24\u0d19\u0d4d\u0d19\u0d7e" # /at̪iːt̪aŋːaɭ/
        self.assertEqual(declensions["Plural"]["Nominative"], expectedVal, "Expected {0} as nominative plural, but received {1}".format(expectedVal, declensions["Plural"]["Nominative"]))

    def testPluralAccusative(self):
        declensions = decline(self.noun)
        exVal = "\u0d05\u0d24\u0d40\u0d24\u0d19\u0d4d\u0d19\u0d33\u0d46" # /at̪iːt̪aŋːaɭe/
        self.assertEqual(declensions["Plural"]["Accusative"], exVal, "Expected {0} as accusative plural, but received {1}".format(exVal, declensions["Plural"]["Accusative"]))

    def testPluralGenitive(self):
        declensions = decline(self.noun)
        exVal = "\u0d05\u0d24\u0d40\u0d24\u0d19\u0d4d\u0d19\u0d33\u0d41\u0d1f\u0d46" # /at̪iːt̪aŋːaɭuʈe/
        self.assertEqual(declensions["Plural"]["Genitive"], exVal, "Expected {0} as genitive plural, but received {1}".format(exVal, declensions["Plural"]["Genitive"]))

    def testPluralDative(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d24\u0d40\u0d24\u0d19\u0d4d\u0d19\u0d7e\u0d15\u0d4d\u0d15\u0d4d" # /at̪iːt̪aŋːaɭkːə/
        self.assertEqual(declensions["Plural"]["Dative"], expectedVal, "Expected {0} as dative plural, but received {1}".format(expectedVal, declensions["Plural"]["Dative"]))

    def testPluralLocative(self):
        declensions = decline(self.noun)
        exVal = "\u0d05\u0d24\u0d40\u0d24\u0d19\u0d4d\u0d19\u0d33\u0d3f\u0d7d" # /at̪iːt̪aŋːaɭil/
        self.assertEqual(declensions["Plural"]["Locative"], exVal, "Expected {0} as locative plural, but received {1}".format(exVal, declensions["Plural"]["Locative"]))

    def testPluralSociative(self):
        declensions = decline(self.noun)
        exVal = "\u0d05\u0d24\u0d40\u0d24\u0d19\u0d4d\u0d19\u0d33\u0d4b\u0d1f\u0d4d" # /at̪iːt̪aŋːaɭoːʈə/
        self.assertEqual(declensions["Plural"]["Sociative"], exVal, "Expected {0} as sociative plural, but received {1}".format(exVal, declensions["Plural"]["Sociative"]))

    def testPluralInstrumental(self):
        declensions = decline(self.noun)
        exVal = "\u0d05\u0d24\u0d40\u0d24\u0d19\u0d4d\u0d19\u0d33\u0d3e\u0d7d" # /at̪iːt̪aŋːaɭaːl/
        self.assertEqual(declensions["Plural"]["Instrumental"], exVal, "Expected {0} as instrumental plural, but received {1}".format(exVal, declensions["Plural"]["Instrumental"]))

class ANStemTests(TestCase):
    def setUp(self):
        self.noun = "\u0d05\u0d35\u0d7b" # avan

    def testSingularNominative(self):
        declensions = decline(self.noun)
        self.assertEqual(declensions["Singular"]["Nominative"], self.noun, "The an-stem noun should be the same as its nominative form.")

    def testSingularAccusative(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d35\u0d28\u0d46" # /aʋan̪e/
        self.assertEqual(declensions["Singular"]["Accusative"], expectedVal, "Expected {0} as the singular accusative form, but received {1} instead".format(expectedVal, declensions["Singular"]["Accusative"]))

    def testSingularGenitive(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d35\u0d7b\u0d31\u0d4d\u0d31\u0d46" # /aʋante/
        self.assertEqual(declensions["Singular"]["Genitive"], expectedVal, "Expected {0} as the singular genitive form, but received {1} instead".format(expectedVal, declensions["Singular"]["Genitive"]))

    def testSingularDative(self):
        declensions = decline(self.noun)
        expectedVal = u"\u0d05\u0d35\u0d28\u0d4d\u0d28\u0d4d"  # /aʋanːə/
        self.assertEqual(declensions["Singular"]["Dative"], expectedVal, u"Expected {0} as the singular dative form, but received {1} instead".format(expectedVal, declensions["Singular"]["Dative"]))

    def testSingularLocative(self):
        declensions = decline(self.noun)
        expectedVal = u"\u0d05\u0d35\u0d28\u0d3f\u0d7d" # /aʋan̪il/
        self.assertEqual(declensions["Singular"]["Locative"], expectedVal, u"Expected {0} as the singular locative form, but received {1} instead".format(expectedVal, declensions["Singular"]["Locative"]))

    def testSingularSociative(self):
        declensions = decline(self.noun)
        expectedVal = u"\u0d05\u0d35\u0d28\u0d4b\u0d1f\u0d4d" # /aʋan̪oːʈə/
        self.assertEqual(declensions["Singular"]["Sociative"], expectedVal, u"Expected {0} as the singular sociative form, but received {1} instead".format(expectedVal, declensions["Singular"]["Sociative"]))

    def testSingularInstrumental(self):
        declensions = decline(self.noun)
        expectedVal = u"\u0d05\u0d35\u0d28\u0d3e\u0d7d" # /aʋan̪aːl/
        self.assertEqual(declensions["Singular"]["Instrumental"], expectedVal, u"Expected {0} as the singular instrumental form, but received {1} instead".format(expectedVal, declensions["Singular"]["Instrumental"]))

    def testPluralNominative(self):
        declensions = decline(self.noun)
        expectedVal = u"\u0d05\u0d35\u0d7c" # /aʋaɾ/
        self.assertEqual(declensions["Plural"]["Nominative"], expectedVal, u"Expected {0} as the plural nominative form, but received {1} instead".format(expectedVal, declensions["Plural"]["Nominative"]))

    def testPluralAccusative(self):
        declensions = decline(self.noun)
        expectedVal = u"\u0d05\u0d35\u0d30\u0d46" # /aʋaɾe/
        self.assertEqual(declensions["Plural"]["Accusative"], expectedVal, u"Expected {0} as the plural accusative form, but received {1} instead".format(expectedVal, declensions["Plural"]["Accusative"]))

    def testPluralGenitive(self):
        declensions = decline(self.noun)
        expectedVal = u"\u0d05\u0d35\u0d30\u0d41\u0d1f\u0d46" # /aʋaɾuʈe/
        self.assertEqual(declensions["Plural"]["Genitive"], expectedVal, "Expected {0} as the plural genitive form, but received {1} instead".format(expectedVal, declensions["Plural"]["Genitive"]))

    def testPluralDative(self):
        declensions = decline(self.noun)
        expectedVal = u"\u0d05\u0d35\u0d7c\u0d15\u0d4d\u0d15\u0d4d" # /aʋaɾkːə/
        self.assertEqual(declensions["Plural"]["Dative"], expectedVal, u"Expected {0} as the plural dative form, but received {1} instead".format(expectedVal, declensions["Plural"]["Dative"]))

    def testPluralLocative(self):
        declensions = decline(self.noun)
        expectedVal = u"\u0d05\u0d35\u0d30\u0d3f\u0d7d" # /aʋaɾil/
        self.assertEqual(declensions["Plural"]["Locative"], expectedVal, u"Expected {0} as the plural locative form, but received {1} instead".format(expectedVal, declensions["Plural"]["Locative"]))

    def testPluralSociative(self):
        declensions = decline(self.noun)
        expectedVal = u"\u0d05\u0d35\u0d30\u0d4b\u0d1f\u0d4d" # /aʋaɾoːʈə/
        self.assertEqual(declensions["Plural"]["Sociative"], expectedVal, u"Expected {0} as the plural sociative form, but received {1} instead".format(expectedVal, declensions["Plural"]["Sociative"]))

    def testPluralInstrumental(self):
        declensions = decline(self.noun)
        expectedVal = u"\u0d05\u0d35\u0d30\u0d3e\u0d7d" # /aʋaɾaːl/
        self.assertEqual(declensions["Plural"]["Instrumental"], expectedVal, "Expected {0} as the plural instrumental form, but received {1} instead".format(expectedVal, declensions["Plural"]["Instrumental"]))

class DuhStemTests(TestCase):
    def setUp(self):
        self.noun = "\u0d15\u0d3e\u0d1f\u0d4d" # /kaːʈə/

    def testSingularNominative(self):
        declensions = decline(self.noun)
        self.assertEqual(declensions["Singular"]["Nominative"], self.noun, "A noun should be the same as its singular nominative form.")

    def testSingularAccusative(self):
        declensions = decline(self.noun)
        exVal = "\u0d15\u0d3e\u0d1f\u0d4d\u0d1f\u0d3f\u0d28\u0d46" # /kaːʈːin̪e/
        self.assertEqual(declensions["Singular"]["Accusative"], exVal, "Expected {0} as the singular accusative form of {1}, but received {2}".format(exVal, self.noun, declensions["Singular"]["Accusative"]))

    def testSingularGenitive(self):
        declensions = decline(self.noun)
        exVal = "\u0d15\u0d3e\u0d1f\u0d4d\u0d1f\u0d3f\u0d7b\u0d31\u0d4d\u0d31\u0d46" # /kaːʈːin̪te/
        self.assertEqual(declensions["Singular"]["Genitive"], exVal, "Expected {0} as the singular genitive form of {1}, but received {2}".format(exVal, self.noun, declensions["Singular"]["Genitive"]))

    def testSingularDative(self):
        declensions = decline(self.noun)
        exVal = "\u0d15\u0d3e\u0d1f\u0d4d\u0d1f\u0d3f\u0d28\u0d4d\u0d28\u0d4d" # /kaːʈːinːə/
        self.assertEqual(declensions["Singular"]["Dative"], exVal, "Expected {0} as the singular dative form of {1}, but received {2}".format(exVal, self.noun, declensions["Singular"]["Dative"]))

    def testSingularLocative(self):
        declensions = decline(self.noun)
        exVal = "\u0d15\u0d3e\u0d1f\u0d4d\u0d1f\u0d3f\u0d7d" # /kaːʈːil/
        self.assertEqual(declensions["Singular"]["Locative"], exVal, "Expected {0} as the singular locative form of {1}, but received {2}".format(exVal, self.noun, declensions["Singular"]["Locative"]))

    def testSingularSociative(self):
        declensions = decline(self.noun)
        exVal = "\u0d15\u0d3e\u0d1f\u0d4d\u0d1f\u0d3f\u0d28\u0d4b\u0d1f\u0d4d" # /kaːʈːin̪oːʈə/
        self.assertEqual(declensions["Singular"]["Sociative"], exVal, "Expected {0} as the singular sociative form of {1}, but received {2}".format(exVal, self.noun, declensions["Singular"]["Sociative"]))

    def testSingularInstrumental(self):
        declensions = decline(self.noun)
        exVal = "\u0d15\u0d3e\u0d1f\u0d4d\u0d1f\u0d3f\u0d28\u0d3e\u0d7d" # /kaːʈːin̪aːl/
        self.assertEqual(declensions["Singular"]["Instrumental"], exVal, "Expected {0} as the singular instrumental form of {1}, but received {2}".format(exVal, self.noun, declensions["Singular"]["Instrumental"]))

    def testPluralNominative(self):
        declensions = decline(self.noun)
        exVal = "\u0d15\u0d3e\u0d1f\u0d4d\u0d15\u0d7e" # /kaːʈəkaɭ/
        self.assertEqual(declensions["Plural"]["Nominative"], exVal, "Expected {0} as the plural nominative form of {1}, but received {2}".format(exVal, self.noun, declensions["Plural"]["Nominative"]))

    def testPluralAccusative(self):
        declensions = decline(self.noun)
        exVal = "\u0d15\u0d3e\u0d1f\u0d4d\u0d15\u0d33\u0d46" # /kaːʈəkaɭe/
        self.assertEqual(declensions["Plural"]["Accusative"], exVal, "Expected {0} as the plural accusative form of {1}, but received {2}".format(exVal, self.noun, declensions["Plural"]["Accusative"]))

    def testPluralGenitive(self):
        declensions = decline(self.noun)
        exVal = "\u0d15\u0d3e\u0d1f\u0d4d\u0d15\u0d33\u0d41\u0d1f\u0d46" # /kaːʈəkaɭuʈe/
        self.assertEqual(declensions["Plural"]["Genitive"], exVal, "Expected {0} as the plural genitive form of {1}, but received {2}".format(exVal, self.noun, declensions["Plural"]["Genitive"]))

    def testPluralDative(self):
        declensions = decline(self.noun)
        exVal = "\u0d15\u0d3e\u0d1f\u0d4d\u0d15\u0d7e\u0d15\u0d4d\u0d15\u0d4d" # /kaːʈəkaɭkːə/
        self.assertEqual(declensions["Plural"]["Dative"], exVal, "Expected {0} as the plural dative form of {1}, but received {2}".format(exVal, self.noun, declensions["Plural"]["Dative"]))

    def testPluralLocative(self):
        declensions = decline(self.noun)
        exVal = "\u0d15\u0d3e\u0d1f\u0d4d\u0d15\u0d33\u0d3f\u0d7d" # /kaːʈəkaɭil/
        self.assertEqual(declensions["Plural"]["Locative"], exVal, "Expected {0} as the plural locative form of {1}, but received {2}".format(exVal, self.noun, declensions["Plural"]["Locative"]))

    def testPluralSociative(self):
        declensions = decline(self.noun)
        exVal = "\u0d15\u0d3e\u0d1f\u0d4d\u0d15\u0d33\u0d4b\u0d1f\u0d4d" # /kaːʈəkaɭoːʈə/
        self.assertEqual(declensions["Plural"]["Sociative"], exVal, "Expected {0} as the plural sociative of {1}, but received {2}".format(exVal, self.noun, declensions["Plural"]["Sociative"]))

    def testPluralInstrumental(self):
        declensions = decline(self.noun)
        exVal = "\u0d15\u0d3e\u0d1f\u0d4d\u0d15\u0d33\u0d3e\u0d7d" # /kaːʈəkaɭaːl/
        self.assertEqual(declensions["Plural"]["Instrumental"], exVal, "Expected {0} as the plural instrumental of {1}, but received {2}".format(exVal, self.noun, declensions["Plural"]["Instrumental"]))

class VowelStemTests(TestCase):
    def setUp(self):
        self.noun = "\u0d24\u0d31" # /t̪ara/ (floor)

    def testSingularNominative(self):
        declensions = decline(self.noun)
        exVal = "\u0d24\u0d31" # The singular nominative should be the same as the noun
        self.assertEqual(declensions["Singular"]["Nominative"], exVal, "Expected {0} as the singular nominative of {1}, but received {2} instead".format(exVal, self.noun, declensions["Singular"]["Nominative"]))

    def testSingularAccusative(self):
        declensions = decline(self.noun)
        exVal = "\u0d24\u0d31\u0d2f\u0d46" # /t̪araje/
        self.assertEqual(declensions["Singular"]["Accusative"], exVal, "Expected {0} as the singular accusative form of {1}, but received {2} instead".format(exVal, self.noun, declensions["Singular"]["Accusative"]))

    def testSingularGenitive(self):
        declensions = decline(self.noun)
        exVal = "\u0d24\u0d31\u0d2f\u0d41\u0d1f\u0d46" # /t̪arajuʈe/
        self.assertEqual(declensions["Singular"]["Genitive"], exVal, "Expected {0} as the singular genitive form of {1}, but received {2} instead".format(exVal, self.noun, declensions["Singular"]["Genitive"]))

    def testSingularDative(self):
        declensions = decline(self.noun)
        exVal = "\u0d24\u0d31\u0d15\u0d4d\u0d15\u0d4d" # /t̪arakːə/
        self.assertEqual(declensions["Singular"]["Dative"], exVal, "Expected {0} as the singular dative form of {1}, but received {2} instead".format(exVal, self.noun, declensions["Singular"]["Dative"]))

    def testSingularLocative(self):
        declensions = decline(self.noun)
        exVal = "\u0d24\u0d31\u0d2f\u0d3f\u0d7d" # /t̪arajil/
        self.assertEqual(declensions["Singular"]["Locative"], exVal, "Expected {0} as the singular locative form of {1}, but received {2} instead".format(exVal, self.noun, declensions["Singular"]["Locative"]))

    def testSingularSociative(self):
        declensions = decline(self.noun)
        exVal = "\u0d24\u0d31\u0d2f\u0d4b\u0d1f\u0d4d" # /t̪arajoːʈə/
        self.assertEqual(declensions["Singular"]["Sociative"], exVal, "Expected {0} as the singular sociative form of {1}, but received {2}".format(exVal, self.noun, declensions["Singular"]["Sociative"]))

    def testSingularInstrumental(self):
        declensions = decline(self.noun)
        exVal = "\u0d24\u0d31\u0d2f\u0d3e\u0d7d" # /t̪arajaːl/
        self.assertEqual(declensions["Singular"]["Instrumental"], exVal, "Expected {0} as the singular instrumental form of {1}, but received {2}".format(exVal, self.noun, declensions["Singular"]["Instrumental"]))

    def testPluralNominative(self):
        declensions = decline(self.noun)
        exVal = "\u0d24\u0d31\u0d15\u0d7e" # /t̪arakaɭ/
        self.assertEqual(declensions["Plural"]["Nominative"], exVal, "Expected {0} as the plural nominative form of {1}, but received {2}".format(exVal, self.noun, declensions["Plural"]["Nominative"]))

    def testPluralAccusative(self):
        declensions = decline(self.noun)
        exVal = "\u0d24\u0d31\u0d15\u0d33\u0d46" # /t̪arakaɭe/
        self.assertEqual(declensions["Plural"]["Accusative"], exVal, "Expected {0} as the accusative plural of {1}, but received {2}".format(exVal, self.noun, declensions["Plural"]["Accusative"]))

    def testPluralGenitive(self):
        declensions = decline(self.noun)
        exVal = "\u0d24\u0d31\u0d15\u0d33\u0d41\u0d1f\u0d46" # /t̪arakaɭuʈe/
        self.assertEqual(declensions["Plural"]["Genitive"], exVal, "Expected {0} as the genitive plural of {1}, but received {2}".format(exVal, self.noun, declensions["Plural"]["Genitive"]))

    def testPluralDative(self):
        declensions = decline(self.noun)
        exVal = "\u0d24\u0d31\u0d15\u0d7e\u0d15\u0d4d\u0d15\u0d4d" # /t̪arakaɭkːə/
        self.assertEqual(declensions["Plural"]["Dative"], exVal, "Expected {0} as the dative plural of {1}, but received {2}".format(exVal, self.noun, declensions["Plural"]["Dative"]))

    def testPluralLocative(self):
        declensions = decline(self.noun)
        exVal = "\u0d24\u0d31\u0d15\u0d33\u0d3f\u0d7d" # /t̪arakaɭil/
        self.assertEqual(declensions["Plural"]["Locative"], exVal, "Expected {0} as the locative plural of {1}, but received {2}".format(exVal, self.noun, declensions["Plural"]["Locative"]))

    def testPluralSociative(self):
        declensions = decline(self.noun)
        exVal = "\u0d24\u0d31\u0d15\u0d33\u0d4b\u0d1f\u0d4d" # /t̪arakaɭoːʈə/
        self.assertEqual(declensions["Plural"]["Sociative"], exVal, "Expected {0} as the sociative plural of {1}, but received {2}".format(exVal, self.noun, declensions["Plural"]["Sociative"]))

    def testPluralInstrumental(self):
        declensions = decline(self.noun)
        exVal = "\u0d24\u0d31\u0d15\u0d33\u0d3e\u0d7d" # /t̪arakaɭaːl/
        self.assertEqual(declensions["Plural"]["Instrumental"], exVal, "Expected {0} as the instrumental plural of {1}, but received {2}".format(exVal, self.noun, declensions["Plural"]["Instrumental"]))

class ALStemTests(TestCase):
    def setUp(self) -> None:
        self.noun = "\u0d2a\u0d4a\u0d30\u0d41\u0d7e" # /poɾuɭ/

    def testSingularNominative(self):
        declensions = decline(self.noun)
        eVal = "\u0d2a\u0d4a\u0d30\u0d41\u0d7e" # Should be unchanged
        self.assertEqual(declensions["Singular"]["Nominative"], eVal, "Expected {0} as the nominative singular of {1}, but received {2}".format(eVal, self.noun, declensions["Singular"]["Nominative"]))

    def testSingularAccusative(self):
        declensions = decline(self.noun)
        eVal = "\u0d2a\u0d4a\u0d30\u0d41\u0d33\u0d46" # /poɾuɭe/
        self.assertEqual(declensions["Singular"]["Accusative"], eVal, "Expected {0} as the accusative singular of {1}, but received {2}".format(eVal, self.noun, declensions["Singular"]["Accusative"]))

    def testSingularGenitive(self):
        declensions = decline(self.noun)
        eVal = "\u0d2a\u0d4a\u0d30\u0d41\u0d33\u0d41\u0d1f\u0d46" # /poɾuɭuʈe/
        self.assertEqual(declensions["Singular"]["Genitive"], eVal, "Expected {0} as the genitive singular of {1}, but received {2}".format(eVal, self.noun, declensions["Singular"]["Genitive"]))
    
    def testSingularDative(self):
        declensions = decline(self.noun)
        eVal = "\u0d2a\u0d4a\u0d30\u0d41\u0d7e\u0d15\u0d4d\u0d15\u0d4d" # /poɾuɭkːə/
        self.assertEqual(declensions["Singular"]["Dative"], eVal, "Expected {0} as the dative singular of {1}, but received {2}".format(eVal, self.noun, declensions["Singular"]["Dative"]))

    def testSingularLocative(self):
        declensions = decline(self.noun)
        eVal = "\u0d2a\u0d4a\u0d30\u0d41\u0d33\u0d3f\u0d7d" # /poɾuɭil/
        self.assertEqual(declensions["Singular"]["Locative"], eVal, "Expected {0} as the locative singular of {1}, but received {2}".format(eVal, self.noun, declensions["Singular"]["Locative"]))

    def testSingularSociative(self):
        declensions = decline(self.noun)
        eVal = "\u0d2a\u0d4a\u0d30\u0d41\u0d33\u0d4b\u0d1f\u0d4d" # /poɾuɭoːʈə/
        self.assertEqual(declensions["Singular"]["Sociative"], eVal, "Expected {0} as the sociative singular of {1}, but received {2}".format(eVal, self.noun, declensions["Singular"]["Sociative"]))

    def testSingularInstrumental(self):
        declensions = decline(self.noun)
        eVal = "\u0d2a\u0d4a\u0d30\u0d41\u0d33\u0d3e\u0d7d" # /poɾuɭaːl/
        self.assertEqual(declensions["Singular"]["Instrumental"], eVal, "Expected {0} as the instrumental singular of {1}, but received {2}".format(eVal, self.noun, declensions["Singular"]["Instrumental"]))

    def testPluralNominative(self):
        declensions = decline(self.noun)
        eVal = "\u0d2a\u0d4a\u0d30\u0d41\u0d7e\u0d15\u0d7e"  # /poɾuɭkaɭ/
        self.assertEqual(declensions["Plural"]["Nominative"], eVal, "Expected {0} as the nominative plural of {1}, but received {2}".format(eVal, self.noun, declensions["Plural"]["Nominative"]))

    def testPluralAccusative(self):
        declensions = decline(self.noun)
        eVal = "\u0d2a\u0d4a\u0d30\u0d41\u0d7e\u0d15\u0d33\u0d46"  # /poɾuɭkaɭe/
        self.assertEqual(declensions["Plural"]["Accusative"], eVal, "Expected {0} as the accusative plural of {1}, but received {2}".format(eVal, self.noun, declensions["Plural"]["Accusative"]))

    def testPluralGenitive(self):
        declensions = decline(self.noun)
        eVal = "\u0d2a\u0d4a\u0d30\u0d41\u0d7e\u0d15\u0d33\u0d41\u0d1f\u0d46"  # /poɾuɭkaɭuʈe/
        self.assertEqual(declensions["Plural"]["Genitive"], eVal, "Expected {0} as the genitive plural of {1}, but received {2}".format(eVal, self.noun, declensions["Plural"]["Genitive"]))

    def testPluralDative(self):
        declensions = decline(self.noun)
        eVal = "\u0d2a\u0d4a\u0d30\u0d41\u0d7e\u0d15\u0d7e\u0d15\u0d4d\u0d15\u0d4d" # /poɾuɭkaɭkːə/
        self.assertEqual(declensions["Plural"]["Dative"], eVal, "Expected {0} as the dative plural of {1} but received {2}".format(eVal, self.noun, declensions["Plural"]["Dative"]))

class SchwaStemTests(TestCase):
    def setUp(self):
        self.noun = "\u0d15\u0d24\u0d15\u0d4d" # കതക് (door)

    def testSingularNominative(self):
        declensions = decline(self.noun)
        eVal = "\u0d15\u0d24\u0d15\u0d4d" # /kat̪akə/ (unchanged)
        self.assertEqual(declensions["Singular"]["Nominative"], eVal, "Expected {0} as the nominative singular of {1}, but received {2}".format(eVal, self.noun, declensions["Singular"]["Nominative"]))