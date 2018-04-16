import numpy as np
from typing import Union

from data_utils.preprocessing_helper import INDEX_WORD_FILE_DIR, WORD_INDEX_FILE_DIR, \
    load_index_to_word_dict, load_word_to_index_dict

class WordIndexVectorizer:

    def __init__(self):
        self.word_to_index = load_word_to_index_dict()
        self.index_to_word = load_index_to_word_dict()

    def fit_transform(self, inputs: Union[list, np.ndarray]):
        if type(inputs[0]) not in [np.ndarray, list]:
            raise TypeError('inputs passed into fit_transform must have 2 dimensions')

    def transform(self, inputs: Union[list, np.ndarray]):
        if type(inputs[0]) not in [np.ndarray, list]:
            raise TypeError('inputs passed into transform must have 2 dimensions')