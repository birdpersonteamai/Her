import unittest
import numpy as np
from nltk.tokenize.simple import string_span_tokenize

from src.data_utils import TwitterDataset
from src.data_utils.tokenizer_wrapper import TokenizerWrapper

class TwitterDatasetTest(unittest.TestCase):
    dataset = TwitterDataset(TokenizerWrapper(lambda string: string.split(),
                                              lambda tokens: ' '.join(tokens)),
                             twitter_filename='twitter_test')


    def test_retrieve_data(self):
        data = self.dataset.get_raw_data

        self.assertTrue(data is not None)
        self.assertTrue(data[0] is not None)

    def test_preprocess_data(self):
        preprocessed_data = self.dataset.get_preprocessed_data

        self.assertTrue(type(preprocessed_data) in (np.ndarray, list))
        self.assertTrue(preprocessed_data is not None)
        self.assertTrue(preprocessed_data[0] is not None)

    def test_inputs(self):
        self.assertTrue(len(self.dataset.inputs) > 0)

    def test_targets(self):
        self.assertTrue(len(self.dataset.targets) > 0)

    def test_same_inputs_targets(self):
        self.assertTrue(len(self.dataset.inputs) == len(self.dataset.targets))


if __name__ == '__main__':
    unittest.main()