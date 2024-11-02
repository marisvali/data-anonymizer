import random
import string

class TextAnonymizer:
    def __init__(self):
        self.words : list[str] = []
        self.weights : list[int] = []
        with open('words_frequencies.csv') as file:
            for line in file:
                tokens = line.split(',')
                self.words.append(tokens[0])
                self.weights.append(int(tokens[1]))

    def _random_word(self) -> str:
        # Choose a random word based on its frequency as used in the English language.
        return random.choices(population=self.words, weights=self.weights, k=1)[0]

    def anonymize_text(self, text: str) -> str:
        # Go through the string. Add separators to the anonymized text as they are.
        # Replace words between separators with random English words based on their frequency.
        # This creates random text that retains only the number of words from the original text.
        # If the original text uses natural language and is large enough, the randomly generated
        # text should exhibit some properties of the original text, such as:
        # - similar overall text size
        # - similar number of times a random part of the text is found throughout the whole text.
        # The reason for not using another hashing technique is because of the possibility of
        # deciphering the original text based on the frequency of words in natural language.
        # For example the most common word in English is 'the' and you can just find the most
        # common word in the encoded text and assume it will be 'the'.
        # So if there is any 1-to-1 relationship between a word in the original text and a word
        # in the encoded text, the encoded text can theoretically be decoded by someone patient
        # enough.
        # We consider any non-letter to be a separator.
        h_text = ""
        word = ""
        for c in text:
            if c.isalpha():
                # Build up the current word until we reach a separator.
                word += c
            else:
                # We reached a separator.
                # If we have a word since the last separator, hash it.
                if len(word) > 0:
                    h_text += self._random_word()
                # Add the separator to the hashed text.
                h_text += c
                # Now, reset the word and let it build up until the next separator.
                word = ""
        # If the text didn't end with a separator, we might still have a word.
        if len(word) > 0:
            h_text += self._random_word()
        return h_text

# If this script is running directly, test the function.
if __name__ == "__main__":
    anonymizer = TextAnonymizer()
    result = anonymizer.anonymize_text(
        "Am pierdut o batistuta, ma bate mamica.\n"
        "And I will strike down upon thee with great vengeance and furious\n"
        "Anger those who attempt to poison and destroy my brothers.\n"
        "And you will know My name is the Lord when I lay my vengeance upon thee!")
    print(result)