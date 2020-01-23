#!/usr/bin/env python
import sys
import string
from sklearn.feature_extraction import stop_words

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace and convert all characters to lowercase
    line = line.strip().lower()

    # remove punctuation
    line = line.translate(None, string.punctuation)

    # split the line into a list of strings; splits on any whitespace
    words = line.split()

    # Use list of stopwords from sklearn
    stopwords = set(stop_words.ENGLISH_STOP_WORDS)

    # output tuples (word, 1) in tab-delimited format
    
    for word in words:
        if word not in stopwords:
            print '%s\t%s' % (word, "1")
