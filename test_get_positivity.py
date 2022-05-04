import unittest

from main import get_positivity_dictionary, get_positivity


class PositivityTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.positivity_values = get_positivity_dictionary()

    def test_text_is_empty(self):
        expected = 0

        text = ""
        actual = get_positivity(self.positivity_values, text)
        self.assertEqual(expected, actual)

    def test_text_one_word(self):
        expected = 10

        text = "fantástico"
        actual = get_positivity(self.positivity_values, text)
        self.assertEqual(expected, actual)

    def test_average_zero(self):
        expected = 0

        text = "fantástico destestable"
        actual = get_positivity(self.positivity_values, text)
        self.assertEqual(expected, actual)

    def test_text_not_empty(self):
        expected = 10/4

        text = "El camino es fantástico"
        actual = get_positivity(self.positivity_values, text)
        self.assertEqual(expected, actual)

    def test_text_not_empty_with_symbols(self):
        expected = 10/4

        text = "El camino es fantástico."
        actual = get_positivity(self.positivity_values, text)
        self.assertEqual(expected, actual)

    def test_only_symbols(self):
        expected = 0

        text = "@.,#:;()'{}[];"
        actual = get_positivity(self.positivity_values, text)
        self.assertEqual(expected, actual)

    def test_text_have_upper_case_chars(self):
        expected = 10/4

        text = "El camino es fANtástico."
        actual = get_positivity(self.positivity_values, text)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
