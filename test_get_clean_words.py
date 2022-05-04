import unittest

from main import get_clean_words


class CleanWordsTestCase(unittest.TestCase):
    def test_text_is_empty(self):
        expected = []

        text = ""
        actual = get_clean_words(text)
        self.assertEqual(expected, actual)

    def test_text_one_word(self):
        expected = ["fantástico"]

        text = "fantástico"
        actual = get_clean_words(text)
        self.assertEqual(expected, actual)

    def test_text_one_word_with_symbol(self):
        expected = ["fantástico"]

        text = "fantástico."
        actual = get_clean_words(text)
        self.assertEqual(expected, actual)

    def test_only_symbols(self):
        expected = []

        text = "@.,#:;()'{}[];"
        actual = get_clean_words(text)
        self.assertEqual(expected, actual)

    def test_phrase(self):
        expected = ["el", "camino", "es", "fantástico"]

        text = "El camino es fantástico"
        actual = get_clean_words(text)
        self.assertEqual(expected, actual)

    def test_text_have_upper_case_chars(self):
        expected = ["el", "camino", "es", "fantástico"]

        text = "El camino es fANtástico."
        actual = get_clean_words(text)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
