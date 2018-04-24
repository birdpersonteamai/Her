from data_utils.datasets.twitter_dataset import TwitterDataset
from data_utils.datasets.opennmt_twitter_dataset import OpenNMTTwitterDataset
from data_utils.tokenizer_wrapper import TokenizerWrapper


def main():
    tokenize = lambda string: string.split()
    detokenize = lambda string: ' '.join(string)
    tokenizer_wrapper = TokenizerWrapper(tokenize, detokenize)
    # clean twitter dataset
    twitter_dataset = TwitterDataset(tokenizer_wrapper)

    # create dataset for opennmt
    opennmt_twitter_dataset = OpenNMTTwitterDataset(tokenizer_wrapper, 'twitter')


if __name__ == '__main__':
    main()
