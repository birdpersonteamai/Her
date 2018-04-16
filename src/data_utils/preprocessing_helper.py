import json
import os
import pickle

ABBREVIATIONS_FILES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..', 'Data', 'abbreviations')
ABBREVIATIONS_DIR = os.path.join(ABBREVIATIONS_FILES_DIR, 'abbreviations.json')
PRIORITIZED_ABBREVIATIONS_DIR = os.path.join(ABBREVIATIONS_FILES_DIR, 'prioritized_abbreviations.json')
WORD_DICT_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..', 'Data', 'word_index_dictionary')
WORD_INDEX_FILE_DIR = os.path.join(WORD_DICT_DIR, 'word_to_index_dict.pkl')
INDEX_WORD_FILE_DIR = os.path.join(WORD_DICT_DIR, 'index_to_word_dict.pkl')


with open(ABBREVIATIONS_DIR) as abbreviations_file:
    ABBREVIATIONS = json.load(abbreviations_file)
with open(PRIORITIZED_ABBREVIATIONS_DIR) as prioritized_abbreviations_file:
    PRIORITIZED_ABBREVIATIONS = json.load(prioritized_abbreviations_file)


def get_abbreviations():
    return ABBREVIATIONS


def get_prioritized_abbreviations():
    return PRIORITIZED_ABBREVIATIONS


def get_contractions():
    return __get_contractions(ABBREVIATIONS)


def get_priortized_contractions():
    return __get_contractions(PRIORITIZED_ABBREVIATIONS)


def __get_contractions(abbreviations: dict):
    contractions = dict()

    for key, value in abbreviations.items():
        contractions[value] = key

    return contractions


def load_word_to_index_dict():
    if os.path.isfile(WORD_INDEX_FILE_DIR):
        print('found word to index dictionary. Loading dictionary...')
        with open(WORD_INDEX_FILE_DIR, 'r') as f:
            return pickle.load(f)
    else:
        print('word to index dictionary not found. Obtain an empty dictionary instead.')
        return {'<unk>': 0, '<start>': 1, '<end>': 2}


def load_index_to_word_dict():
    if os.path.isfile(INDEX_WORD_FILE_DIR):
        print('found index to word dictionary. Loading dictionary...')
        with open(INDEX_WORD_FILE_DIR, 'r') as f:
            return pickle.load(f)
    else:
        print('index to word dictionary not found. Obtain an empty dictionary instead.')
        return {0: '<unk>', 1: '<start>', 2:'<end>'}


def save_word_to_index_dict(word_to_index: dict):
    print('saving word to index dictionary...')
    with open(WORD_INDEX_FILE_DIR, 'w') as f:
        pickle.dump(word_to_index, f)


def save_index_to_word_dict(index_to_word: dict):
    print('saving index to word dictionary...')
    with open(INDEX_WORD_FILE_DIR, 'w') as f:
        pickle.dump(index_to_word, f)

