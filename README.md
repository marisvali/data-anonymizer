# Purpose

I use Azharja to take personal notes. I've used it for several years and collected many personal notes. I'd like to give this repository to other people that are developing Azharja, to test things like the speed of a new search function or the speed of starting the application.

My notes are currently the only representative data repository for Azharja. However, I want to anonymize the data. For the purposes of running tests, the content itself is not that important.

These Python scripts anonymize data from an Azharja data repository.

# Short history

At first, I wanted to retain the structure of the original text as much as possible, in order to simulate how often a phrase appears in the overall text, how many lines or paragraphs there are etc.

If you look in the commit history, I implemented several solutions and ended up with a simple random text generator. I've come from hashing, to "anonymizing", to just generating random text.

This is because every time I thought I've messed up a text enough to be sure I'm not giving away sensitive data, I found a new way that someone could extract SOME data that I want to keep hidden.

Examples:
- If you map every letter to another letter, this is easy to crack, using the frequency of words in natural language. For example the most common word in English is 'the' and you can just find the most common 3-letter word in the encoded text and assume it will be 'the' and continue like this to crack the rest of the mapping.
- If you map every word to a random word, but you do it consistently (word X will always be replaced by word Y), you are again vulnerable to attacks by using word frequency.
- If you add variations, you are just reducing how much sensitive data can be extracted, but you never know what you still give people.
- Also, if you keep separators intact, including digits, there go your dates, hours and notes regarding money, which can all be somewhat guessed by the size of the number.
- Even if you randomize each digit, you are giving away SOME info. If a figure can be suspected to represent a sum of money, it matters if it is 3 digits or 5 digits.

In the end, the only way to be safe is to just not use any of the original text as input. Just generate text based on the original text length. I hope I won't now think of a way that text length can give away sensitive information, in this case.

So in the end what is kept from the original files are the number of files, how they are connected and the length of the text.

The generated text lightly simulates natural language in that it picks words at random based on the frequency with which they appear in the English language. In order to do this I found a frequency list for English words (there are several freely available) and processed it to get what I need in words_frequencies.csv: the top 10 000 English words, lowercase, with no punctuation or special characters, and their frequencies.