import random

class TextGenerator:
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

    def random_text(self, num_chars: int, with_paragraphs: bool) -> str:
        # Generate a random text of approximately the specified length. The text will be made
        # up of lines of random length.
        # I've come from hashing, to anonymizing, to just generating random text.
        # This is because every time I think I've messed up a text enough to be sure I'm not
        # giving away sensitive data, I find a new way that someone could extract SOME data
        # that I want to keep hidden.
        # Examples:
        # - If you map every letter to another letter, this is easy to crack, using the frequency
        # of words in natural language. For example the most common word in English is 'the' and
        # you can just find the most common 3-letter word in the encoded text and assume it will
        # be 'the' and continue like this to crack the rest of the mapping.
        # - If you map every word to a random word, but you do it consistently (word X will always
        # be replaced by word Y), you are again vulnerable to attacks by using word frequency.
        # - If you add variations, you are just reducing how much sensitive data can be extracted,
        # but you never know what you still give people.
        # - Also, if you keep separators intact, including digits, there go your dates, hours and
        # notes regarding money, which can all be somewhat guessed by the size of the number.
        # - Even if you randomize each digit, you are giving away SOME info. If a figure can be
        # suspected to be money, it matters if it is 3 digits or 5 digits.
        #
        # In the end, the only way to be safe is to just not read any of the sensitive data, and
        # just generate it, based on text length. I hope I won't think of a way that text length
        # can give away sensitive information.

        text = ""
        if num_chars == 0:
            return text

        while True:
            text += self._random_word()
            if len(text) >= num_chars:
                break

            # Randomly break up the text in paragraphs.
            if with_paragraphs and random.random() < 0.01:
                text += '\n\n'
            else:
                text += " "

        return text


# If this script is running directly, test the function.
if __name__ == "__main__":
    anonymizer = TextGenerator()
    result = anonymizer.random_text(len(
        "Am pierdut o batistuta, ma bate mamica, 123.\n"
        "And I will strike down upon thee with great vengeance and furious\n"
        "Anger those who attempt to poison and destroy my brothers.\n"
        "And you will know My name is the Lord when I lay my vengeance upon thee!"))
    print(result)