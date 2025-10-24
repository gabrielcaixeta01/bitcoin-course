import random
import sys

import sys
sys.path.insert(0, 'functions')

from functions.hash1 import simple_hash

PRINTABLE_ASCII = ''.join(chr(c) for c in range(32, 127))

def random_ascii(n: int = 8, alphabet: str = PRINTABLE_ASCII) -> str:
    return ''.join(random.choice(alphabet) for _ in range(n))

def find_collision_simple(len_str=8, max_iters=200_000):
    seen = {}
    for _ in range(max_iters):
        s = random_ascii(len_str)
        h = simple_hash(s)
        if h in seen and seen[h] != s:
            return seen[h], s, h
        seen.setdefault(h, s)
    raise ValueError("Colisão não encontrada no limite dado")


a, b, h = find_collision_simple(len_str=8, max_iters=200_000)
print("Colisão encontrada:")
print("A:", a)
print("B:", b)
print("hash:", h)