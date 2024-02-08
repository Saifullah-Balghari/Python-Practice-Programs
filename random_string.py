import random
import string

alphabets = list(string.ascii_letters)
random_string = random.sample(alphabets, 3)

r1 = ''.join(random_string)
r1 = r1[::-1]
r2 = ''.join(random_string)
