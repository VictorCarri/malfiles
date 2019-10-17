from django.test import TestCase

from declension.maldecl.decline import decline


class AMStemTests(TestCase):
    def setUp(self):
        self.noun = "\u0d05\u0d24\u0d40\u0d24\u0d02" # atiiTam

    def test_singular_nominative(self):
        declensions = decline(self.noun)
        self.assertEqual(declensions["Singular"]["Nominative"], self.noun, "The generated nominative singular should be the same as the given noun.")

    def test_singular_accusative(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d24\u0d40\u0d24\u0d24\u0d4d\u0d24\u0d3f\u0d28\u0d46"
        self.assertEqual(declensions["Singular"]["Accusative"], expectedVal, "The generated accusative singular should be {0}, but {1} was returned.".format(expectedVal, declensions["Singular"]["Accusative"]))

    def test_singular_genitive(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d24\u0d40\u0d24\u0d24\u0d4d\u0d24\u0d3f\u0d7b\u0d31\u0d4d\u0d31\u0d46"
        self.assertEqual(declensions["Singular"]["Genitive"], expectedVal, "The generated genitive singular should be {0}, but {1} was returned.".format(expectedVal, declensions["Singular"]["Genitive"]))

    def test_singular_dative(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d24\u0d40\u0d24\u0d24\u0d4d\u0d24\u0d3f\u0d28\u0d4d\u0d28\u0d4d" # atiitattin_n_uh
        self.assertEqual(declensions["Singular"]["Dative"], expectedVal, "The generated dative singular should be {0}, but {1} was returned.".format(expectedVal, declensions["Singular"]["Dative"]))

    def test_singular_locative(self):
        declensions = decline(self.noun)
        expectedVal = "\u0d05\u0d24\u0d40\u0d24\u0d24\u0d4d\u0d24\u0d3f\u0d7d" # atiitattil
        self.assertEqual(declensions["Singular"]["Locative"], expectedVal, "The generated locative singular should be {0}, but {1} was returned.".format(expectedVal, declensions["Singular"]["Locative"]))
