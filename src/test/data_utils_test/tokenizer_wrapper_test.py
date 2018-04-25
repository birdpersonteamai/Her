from nltk.tokenize import word_tokenize
import numpy as np
import unittest

from src.data_utils.tokenizer_wrapper import TokenizerWrapper


class TokenizerWrapperTest(unittest.TestCase):
    # TokenizerWrapper accepts a callable function that tokenizes right away
    tokenizer_wrapper = TokenizerWrapper(lambda string: string.split())

    def test_initialization(self):
        tokenizer_wrapper = TokenizerWrapper(lambda string: string.split())
        self.assertTrue(callable(tokenizer_wrapper.tokenize))

    def test_split_tokenize(self):
        tokenizer_wrapper = TokenizerWrapper(lambda string: string.split())
        tokenized_text = tokenizer_wrapper.tokenize('hello how are you')
        self.assertTrue(tokenized_text[0] == 'hello')

        tokenized_text = tokenizer_wrapper.tokenize("it is, crazy. No matter what he is.")
        self.assertTrue(tokenized_text[0] == "it's,")

    def test_split_detokenize(self):
        tokenizer_wrapper = TokenizerWrapper(lambda string: string.split(), lambda array_of_word: ' '.join(array_of_word))
        detokenized_text = tokenizer_wrapper.detokenize(['hello', 'how', 'are', 'you'])
        self.assertTrue(detokenized_text[0] == 'h')
        self.assertFalse(detokenized_text[-1] == 'a')
        self.assertTrue(type(detokenized_text) == str)

        detokenized_text = tokenizer_wrapper.detokenize([
            ['hello', 'how', 'are', 'you'],
            ['my', 'name', 'welcomes', 'you']
        ])
        self.assertTrue(detokenized_text[0] == 'hello how are you')
        self.assertTrue(detokenized_text[1] == 'my name welcomes you')

    def test_nltk_word_tokenize(self):
        # test nltk tokenizer
        tokenizer_wrapper = TokenizerWrapper(word_tokenize)
        tokenized_text = tokenizer_wrapper.tokenize('hello how are you')
        self.assertTrue(tokenized_text[0] == 'hello')
        self.assertTrue(tokenized_text[-1] == 'you')

        # if an unknown character is passed in, it should return back the unknown character
        tokenized_text = tokenizer_wrapper.tokenize('a')
        self.assertFalse(tokenized_text[0] is None)

        """ test passing list or numpy array to tokenize function """
        tokenized_texts = tokenizer_wrapper.tokenize(['hello how are you', 'i am fine, thank you'])
        self.assertTrue(tokenized_texts[0][0] == 'hello')
        self.assertTrue(tokenized_texts[0][-1] == 'you')
        self.assertTrue(tokenized_texts[1][0] == "i'm")
        self.assertTrue(tokenized_texts[1][-1] == 'you')

        tokenized_texts = np.array(['hello how are you', 'i am fine, thank you'])
        tokenized_texts = tokenizer_wrapper.tokenize(tokenized_texts)
        self.assertTrue(tokenized_texts[0][0] == 'hello')
        self.assertTrue(tokenized_texts[0][-1] == 'you')
        self.assertTrue(tokenized_texts[1][0] == "i'm")
        self.assertTrue(tokenized_texts[1][-1] == 'you')

        """ test edge cases"""
        tokenized_texts = "how is he doing there he said he did not do that then it is not his fault"
        tokenized_texts = tokenizer_wrapper.tokenize(tokenized_texts)
        self.assertTrue(tokenized_texts[0] == "how's")
        self.assertTrue(tokenized_texts[-1] == "fault")

        tokenized_texts = "I would not ever want to would not play with would not"
        tokenized_texts = tokenizer_wrapper.tokenize(tokenized_texts)
        self.assertTrue(tokenized_texts[0] == "i")
        self.assertTrue(tokenized_texts[-1] == "wouldn't")

        tokenized_texts = np.array([12,34])

        def tokenize_test_type_error():
            return tokenizer_wrapper.tokenize(tokenized_texts)
        self.assertRaises(TypeError, tokenize_test_type_error)