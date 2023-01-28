from doctest import set_unittest_reportflags
import re
from collections import Counter

PUNCTUATION = r"[!\"#\$%&\(\)\*\+,-\./:;<=>\?@\[\\\]\^_`{\|}~]"

def count_words(sentence: str) -> Counter:
    # remove puncuation
    sentence = re.sub(PUNCTUATION, " ", sentence)
    # sentence = re.sub(APOSTROPHES, " ", sentence)
    # split by whitespace
    words = re.split('[\s]',sentence.lower())
    words = list(filter(lambda x: len(x) > 0, words))
    return Counter(words)

print(count_words("'First: don't laugh. Then: don't cry. You're getting it.'"))