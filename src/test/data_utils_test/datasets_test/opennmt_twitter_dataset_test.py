import os
import unittest

from data_utils.datasets.opennmt_twitter_dataset import OpenNMTTwitterDataset
from data_utils.tokenizer_wrapper import TokenizerWrapper


class OpenNMTTwitterDatasetTest(unittest.TestCase):
    tokenizer_wrapper = TokenizerWrapper(lambda sentence: sentence.split(),
                                         lambda tokens: ' '.join(tokens))
    opennmt_twitter_dataset = OpenNMTTwitterDataset(tokenizer_wrapper, 'twitter_test')

    def test_retrieve_data(self):
        opennmt_twitter_dataset = OpenNMTTwitterDatasetTest.opennmt_twitter_dataset
        raw_data = opennmt_twitter_dataset.get_raw_data
        self.assertTrue(raw_data is not None)
        self.assertTrue(type(raw_data) is list)

        # make sure dir is created
        self.assertTrue(os.path.isdir(opennmt_twitter_dataset.opennmt_twitter_data_path))

    def test_preprocess_data(self):
        opennmt_twitter_dataset = OpenNMTTwitterDatasetTest.opennmt_twitter_dataset
        self.assertTrue(os.path.isfile(opennmt_twitter_dataset.save_source))
        self.assertTrue(os.path.isfile(opennmt_twitter_dataset.save_target))
