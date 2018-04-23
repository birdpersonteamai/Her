import os

from src.data_utils.dataset_helper import Dataset


"""
TwitterDataset
Steps:
1.  retrieve data
2.  preprocess data
3.  save preprocessed data
"""
class TwitterDataset(Dataset):

    def __init__(self, tokenizer, twitter_filename='twitter'):
        super(TwitterDataset, self).__init__(twitter_filename, tokenizer)

        dir = os.path.dirname(os.path.realpath(__file__))
        self.data_path = os.path.join(dir, '../', '../', '../', 'data', twitter_filename)
        self.data_file = os.path.join(self.data_path, self.filename)

        self.inputs = []
        self.targets = []

        self.retrieve_data()
        self.preprocessed_data()
        self.save_preprocessed_data()

    def retrieve_data(self):
        with open(self.data_file, 'r') as f:
            self._raw_data = f.read()

    def preprocessed_data(self):
        preprocessed_data = self._raw_data.split('\n')
        preprocessed_data = [self.tokenizer.tokenize(single_data) for single_data in preprocessed_data]

        self._preprocessed_data = preprocessed_data

        self.inputs = preprocessed_data[::2]
        self.targets = preprocessed_data[1::2]

        shorter_length = min(len(self.inputs), len(self.targets))
        self.inputs = self.inputs[:shorter_length]
        self.targets = self.targets[:shorter_length]

    def save_preprocessed_data(self):
        preprocessed_file = os.path.join(self.data_path, 'cleaned_{}'.format(self.filename))
        with open(preprocessed_file, 'w') as f:
            for data in self._preprocessed_data:

                # check if it is at the end
                if len(data) == 0:
                    break

                detokenized_data = self.tokenizer.detokenize(data)
                f.write(detokenized_data + '\n')

