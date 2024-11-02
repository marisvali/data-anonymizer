def hashed_letter(letter: str, word_len: int) -> str:
    # Go from letter to ASCII code.
    x1 = ord(letter)
    # Do some deterministic hashing that depends on the word length.
    x2 = int((x1 * word_len * word_len * 2953) / 13)
    # Bring it back to the domain of letters.
    # We have ASCII ranges 65-90 (uppercase letters) and 97-122 (lowercase letters).
    # That means 52 letters.
    x3 = x2 % 52
    # Become one of the 52 letters.
    if x3 < 26:
        # Become a capital letter.
        x4 = 65 + x3
    else:
        # Become a lowercase letter.
        x4 = 97 + (x3 - 26)
    return chr(x4)

def hashed_word(word: str) -> str:
    word_len = len(word)
    h_word = ""
    for letter in word:
        h_word += hashed_letter(letter, word_len)
    return h_word

def hashed_text(text: str) -> str:
    # Go through the string. Add separators to the hashed text as they are.
    # Transform words between separators by hashing them and then add them to the hashed text.
    # We consider any non-letter to be a separator. Separators are ignored.
    # The purpose is only to make the text illegible.
    h_text = ""
    word = ""
    for c in text:
        if c.isalpha():
            # Build up the current word until we reach a separator.
            word += c
        else:
            # We reached a separator.
            # If we have a word since the last separator, hash it.
            h_text += hashed_word(word)
            # Add the separator to the hashed text.
            h_text += c
            # Now, reset the word and let it build up until the next separator.
            word = ""
    # If the text didn't end with a separator, we might still have a word.
    h_text += hashed_word(word)
    return h_text

# If this script is running directly, test the function.
if __name__ == "__main__":
    result = hashed_text("Am pierdut o batistuta, ma bate mamica.\n"
                         "And I will strike down upon thee with great vengeance and furious\n"
                         "Anger those who attempt to poison and destroy my brothers.\n"
                         "And you will know My name is the Lord when I lay my vengeance upon thee!")
    print(result)