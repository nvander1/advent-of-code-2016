from sys import stdin
from collections import Counter
text = [line for line in stdin]
transpose = list(map(list, zip(*text)))
message = [Counter(line).most_common(1)[0][0] for line in transpose]
print(''.join(message[:-1]))
