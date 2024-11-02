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
        # Generate a random text of approximately the specified length.
        # The text will be made up of random English words. The words are chosen based on
        # the frequency with which they are used in regular English speech.
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