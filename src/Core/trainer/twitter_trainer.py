import os

def train_twitter_dataset():
    config_file = os.path.join(os.path.dirname(__file__), '../', '../', '../', 'config', 'transformer.yml')
    os.system('onmt-main train_and_eval --model_type Transformer --config {}'.format(config_file))

if __name__ == '__main__':
    train_twitter_dataset()
