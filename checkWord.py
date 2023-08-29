from latcyruz import toLatin, toCyrillic
from uzwords import words
from random import randint

word = words[randint(1,30000)]
print(word)
print(toLatin(word))
print(toCyrillic(toLatin(word)))