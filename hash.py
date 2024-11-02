import random
import string

class TextHasher:
    def __init__(self):
        # Load dictionary.
        self.words : list[str] = []
        self.weights : list[int] = []
        with open('words_frequencies.csv') as file:
            for line in file:
                tokens = line.split(',')
                self.words.append(tokens[0])
                self.weights.append(int(tokens[1]))

    def _hashed_word(self, word: str) -> str:
        if len(word) == 0:
            return word
        # Choose a random word based on its frequency as used in the English language.
        # This creates random speech that retains only the number of words from the original text.
        # If the original text uses natural language and is large enough, the randomly generated
        # text should exhibit some properties of the original text, such as:
        # - similar overall text size
        # - similar number of times a random part of the text is found throughout the whole text
        return random.choices(population=self.words, weights=self.weights, k=1)[0]

    def hashed_text(self, text: str) -> str:
        # Go through the string. Add separators to the hashed text as they are.
        # Transform words between separators by hashing them and then add them to the hashed text.
        # We consider any non-letter to be a separator. Separators are ignored.
        h_text = ""
        word = ""
        for c in text:
            if c.isalpha():
                # Build up the current word until we reach a separator.
                word += c
            else:
                # We reached a separator.
                # If we have a word since the last separator, hash it.
                h_text += self._hashed_word(word)
                # Add the separator to the hashed text.
                h_text += c
                # Now, reset the word and let it build up until the next separator.
                word = ""
        # If the text didn't end with a separator, we might still have a word.
        h_text += self._hashed_word(word)
        return h_text

# If this script is running directly, test the function.
if __name__ == "__main__":
    hasher = TextHasher()
    result = hasher.hashed_text(
        "Am pierdut o batistuta, ma bate mamica.\n"
        "And I will strike down upon thee with great vengeance and furious\n"
        "Anger those who attempt to poison and destroy my brothers.\n"
        "And you will know My name is the Lord when I lay my vengeance upon thee!")
    print(result)