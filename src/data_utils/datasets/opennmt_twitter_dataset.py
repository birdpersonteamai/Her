import os
from data_utils.dataset_helper import Dataset
from data_utils.tokenizer_wrapper import TokenizerWrapper

class OpenNMTTwitterDataset(Dataset):

    def __init__(self, tokenizer, twitter_filename='twitter'):
        super(OpenNMTTwitterDataset, self).__init__(twitter_filename, tokenizer)
        self.source = None
        self.target = None

        self.retrieve_data()

    def retrieve_data(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_path = os.path.join(dir, '../', '../', '../', 'data')
        data_file = os.path.join(data_path, self.filename)

        # read raw twitter file and separate them into source and target
        with open(data_file, 'r') as f:
            self._raw_data = f.read()
            self._raw_data = self._raw_data.split('\n')

            self.source = self._raw_data[::2]
            self.target = self._raw_data[1::2]

            # for open nmt , we first have to split the source and target from the text file
            trim_length = min(len(self.source), len(self.target))
            self.source = self.source[:trim_length]
            self.target = self.target[:trim_length]

        save_source = os.path.join(data_path, 'opennmt_twitter_source.txt')
        save_target = os.path.join(data_path, 'opennmt_twitter_target.txt')

        # save the source
        with open(save_source, 'w') as f:
            for data in self.source:
                f.write(data)

        #save the target
        with open(save_target, 'w') as f:
            for data in self.target:
                f.write(data)

    def preprocess_data(self):
        pass



tokenizer_wrapper = TokenizerWrapper(None, None)
open = OpenNMTTwitterDataset(tokenizer_wrapper, 'twitter')