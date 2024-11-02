import random
import string

class TextHasher:
    def __init__(self):
        # Load dictionary.
        with open('words_alpha.txt') as file:
            self.all_english_words = [line.strip() for line in file]

        # Create buckets of words of similar length (+/-2 chars).
        self.english_words_of_length: dict[int, list[str]] = {}
        for word in self.all_english_words:
            fixed_length = len(word)
            # Add to all buckets where it belongs.
            for var_length in range(fixed_length-2, fixed_length+2):
                # Protect against things like fixed_length == 1.
                if var_length > 0:
                    # Create list if it was never created.
                    if var_length not in self.english_words_of_length.keys():
                        self.english_words_of_length[var_length] = []
                    # Add word to this list.
                    self.english_words_of_length[var_length].append(word)

        self.map: dict[str, str] = {}

    def _hashed_word(self, word: str) -> str:
        if len(word) == 0:
            return word
        if word not in self.map:
            # Choose a random word of similar length.
            # We might encounter words that are too long and don't have a bucket.
            # In that case, map them to a random word.
            length = len(word)
            if length not in self.english_words_of_length.keys():
                self.map[word] = random.choice(self.all_english_words)
            else:
                self.map[word] = random.choice(self.english_words_of_length[length])


        return self.map[word]

    def hashed_text(self, text: str) -> str:
        # Go through the string. Add separators to the hashed text as they are.
        # Transform words between separators by hashing them and then add them to the hashed text.
        # We consider any non-letter to be a separator. Separators are ignored.
        # The purpose is only to make the original meaning of the text impenetrable.
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