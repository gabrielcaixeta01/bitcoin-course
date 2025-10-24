import random
import sys
from typing import Tuple

import sys
sys.path.insert(0, 'functions')

from functions.hash0 import xor32_hash

PRINTABLE_MIN, PRINTABLE_MAX = 32, 126

def pre_image_constructive_ascii(target_hash: str, max_tries: int = 1_000_000, seed: int | None = None) -> str:
    if seed is not None:
        random.seed(seed)

    t = int(target_hash, 16)

    for _ in range(max_tries):
        b0 = [random.randint(PRINTABLE_MIN, PRINTABLE_MAX) for _ in range(4)]
        W0 = b0[0] | (b0[1] << 8) | (b0[2] << 16) | (b0[3] << 24)
        W1 = W0 ^ t
        b1 = [(W1 >> (8*k)) & 0xFF for k in range(4)]

        if all(PRINTABLE_MIN <= x <= PRINTABLE_MAX for x in b1):
            s = ''.join(map(chr, b0 + b1))
            if xor32_hash(s) == target_hash:
                return s
    raise ValueError("Pré-imagem não encontrada no limite dado")


target = xor32_hash("bitcoin0")
pre_img = pre_image_constructive_ascii(target, seed=123)
print(f"alvo: bitcoin0, hash_alvo: {target}")
print("pré-imagem:", pre_img)
print("confere:", xor32_hash(pre_img))