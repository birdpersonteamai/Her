import os

from data_utils.dataset_helper import Dataset

class OpenNMTTwitterDataset(Dataset):
    """
    1. retrieve dataset
    2. save source and target to prepare for training the model
    3. build and save the vocabulary
    """

    def __init__(self, tokenizer, twitter_filename='twitter'):
        super(OpenNMTTwitterDataset, self).__init__(twitter_filename, tokenizer)
        self.source = None
        self.target = None

        dir = os.path.dirname(os.path.realpath(__file__))
        data_path = os.path.join(dir, '../', '../', '../', 'data', twitter_filename)
        self.data_file = os.path.join(data_path, 'cleaned_' + self.filename)
        self.opennmt_twitter_data_path = os.path.join(data_path, 'opennmt_{}'.format(twitter_filename))

        if not os.path.isdir(self.opennmt_twitter_data_path):
            os.mkdir(self.opennmt_twitter_data_path)

        self.save_source = os.path.join(self.opennmt_twitter_data_path, 'opennmt_twitter_source.txt')
        self.save_target = os.path.join(self.opennmt_twitter_data_path, 'opennmt_twitter_target.txt')

        self.retrieve_data()
        self.preprocess_data()

    def retrieve_data(self):

        # read raw twitter file and separate them into source and target
        with open(self.data_file, 'r') as f:
            self._raw_data = f.read()
            self._raw_data = self._raw_data.split('\n')

            self.source = self._raw_data[::2]
            self.target = self._raw_data[1::2]

            # for open nmt , we first have to split the source and target from the text file
            trim_length = min(len(self.source), len(self.target))
            self.source = self.source[:trim_length]
            self.target = self.target[:trim_length]



        # save the source
        with open(self.save_source, 'w') as f:
            for data in self.source:
                f.write(data + '\n')

        #save the target
        with open(self.save_target, 'w') as f:
            for data in self.target:
                f.write(data + '\n')

    def preprocess_data(self):
        source_vocab_file = os.path.join(self.opennmt_twitter_data_path, 'opennmt_twitter_source_vocab.txt')
        target_vocab_file = os.path.join(self.opennmt_twitter_data_path, 'opennmt_twitter_target_vocab.txt')

        os.system('onmt-build-vocab --save_vocab {} {}'.format(source_vocab_file, self.save_source))
        os.system('onmt-build-vocab --save_vocab {} {}'.format(target_vocab_file, self.save_target))
