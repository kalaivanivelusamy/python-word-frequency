filename = "sample.txt"
with open(filename) as file:
    text = file.read()

import string
import pprint

text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))
print(text)

words = text.split()
print(words)


word_count = {}
word_count = {word: words.count(word) for word in set(words)}
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
pprint.pprint(sorted_word_count)
print("\nTop 10 most frequent words:")
pprint.pprint(sorted_word_count[:10], width=1)
