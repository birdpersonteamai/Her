import os

def train_twitter_dataset():
    data_file = os.path.join(os.path.dirname(__file__), '../', '../', '../', 'Data', 'twitter', 'opennmt_py_twitter')
    os.system('source activate py35 && python ../../OpenNMT-py/train.py -data {} -save_model demo_model'.format(data_file))

if __name__ == '__main__':
    train_twitter_dataset()
