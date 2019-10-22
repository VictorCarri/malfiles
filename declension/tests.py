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
        expectedVal = "\u0d05\u0d35\u0d28\u0d4d\u0d28\u0d4d"  # /aʋanːə/
        self.assertEqual(declensions["Singular"]["Dative"], expectedVal, "Expected {0} as the singular dative form, but received {1} instead".format(expectedVal, declensions["Singular"]["Dative"]))

    def testSingularLocative(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d35\u0d28\u0d3f\u0d7d" # /aʋan̪il/
        self.assertEqual(declensions["Singular"]["Locative"], expectedVal, "Expected {0} as the singular locative form, but received {1} instead".format(expectedVal, declensions["Singular"]["Locative"]))

    def testSingularSociative(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d35\u0d28\u0d4b\u0d1f\u0d4d" # /aʋan̪oːʈə/
        self.assertEqual(declensions["Singular"]["Sociative"], expectedVal, "Expected {0} as the singular sociative form, but received {1} instead".format(expectedVal, declensions["Singular"]["Sociative"]))

    def testSingularInstrumental(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d35\u0d28\u0d3e\u0d7d" # /aʋan̪aːl/
        self.assertEqual(declensions["Singular"]["Instrumental"], expectedVal, "Expected {0} as the singular instrumental form, but received {1} instead".format(expectedVal, declensions["Singular"]["Instrumental"]))

    def testPluralNominative(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d35\u0d7c" # /aʋaɾ/
        self.assertEqual(declensions["Plural"]["Nominative"], expectedVal, "Expected {0} as the plural nominative form, but received {1} instead".format(expectedVal, declensions["Plural"]["Nominative"]))