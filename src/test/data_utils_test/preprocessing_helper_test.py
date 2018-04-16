import unittest

from src.data_utils.preprocessing_helper import get_abbreviations, get_contractions


class PreprocessingHelperTest(unittest.TestCase):

    def test_get_abbreviations(self):
        abbreviations = get_abbreviations()
        self.assertTrue(type(abbreviations) is dict)
        self.assertTrue(abbreviations.get("let us") is not None)

        self.assertTrue(abbreviations.get("hello") is None)
        self.assertTrue(abbreviations.get("") is None)


    def test_get_contractions(self):
        contractions = get_contractions()
        self.assertTrue(type(contractions) is dict)
        self.assertTrue(contractions.get("let's") is not None)

        self.assertTrue(contractions.get("hello") is None)
        self.assertTrue(contractions.get("") is None)

    #TODO create test for dictionary word index