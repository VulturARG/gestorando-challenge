from typing import List


def get_positivity_dictionary():
    return {
        "fantástico": 10,
        "destestable": -10
    }


def get_text_to_analyze():
    return "El camino es fantástico."


def get_clean_words(text_to_sanitized: str) -> List[str]:
    text_to_sanitized = text_to_sanitized.lower()
    text_to_sanitized = ''.join(char for char in text_to_sanitized if char.isalnum() or char == ' ')
    return text_to_sanitized.split()


def get_positivity(positivity: dict, text_to_analyze: str) -> float:
    clean_text = get_clean_words(text_to_analyze)
    word_values = [positivity.get(word, 0) for word in clean_text]
    number_of_words = len(word_values)
    if number_of_words == 0:
        return 0
    return sum(word_values) / number_of_words


if __name__ == '__main__':
    positivity_values = get_positivity_dictionary()
    text = get_text_to_analyze()
    positivity_value = get_positivity(positivity_values, text)
    print(positivity_value)
