#!/usr/bin/env python
from collections import defaultdict
import sys

word_count = defaultdict(int)
for line in sys.stdin:
    try:
        line = line.strip()
        word, count = line.split("\t", 1)
        count = int(count)

    except:
        continue
    word_count[word] += count

for word, count in word_count.items():
    print(word, count)
