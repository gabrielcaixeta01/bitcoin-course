import random
import sys
import itertools

sys.path.insert(0, 'functions')

from hash0 import xor32_hash 
from hash1 import simple_hash
from sha256 import hashlib  


""" QUESTAO 1 """

#chutei e acertei


""" QUESTAO 2 """

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

"""
target = xor32_hash("bitcoin0")
pre_img = pre_image_constructive_ascii(target, seed=123)
print(f"alvo: bitcoin0, hash_alvo: {target}")
print("pré-imagem:", pre_img)
print("confere:", xor32_hash(pre_img))
"""

""" QUESTAO 3 """

#Usei a mesma função da 2

"""
target = "1b575451"
pre_img = pre_image_constructive_ascii(target, seed=123)
print(f"hash_alvo: {target}")
print("pré-imagem:", pre_img)
print("confere:", xor32_hash(pre_img))
"""

""" QUESTAO 4 """
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


"""
a, b, h = find_collision_simple(len_str=8, max_iters=200_000)
print("Colisão encontrada:")
print("A:", a)
print("B:", b)
print("hash:", h)
"""

""" QUESTAO 5 """

MASK = 0xFFFFFFFF
BASE = 31
POW_BASE4 = pow(BASE, 4, 2**32)

def find_second_preimage(original: str, alphabet: str = "abcdefghijklmnopqrstuvwxyz") -> str:
    target = int(simple_hash(original), 16) & MASK

    suffix_table = {}
    for combination in itertools.product(alphabet, repeat=4):
        q = ''.join(combination)
        hq = int(simple_hash(q), 16) & MASK

        if hq not in suffix_table:
            suffix_table[hq] = q

    for combination in itertools.product(alphabet, repeat=4):
        p = ''.join(combination)
        hp = int(simple_hash(p), 16) & MASK
        needed = (target - ((hp * POW_BASE4) & MASK)) & MASK

        q = dict.get(suffix_table, needed)
        if q is not None:
            candidate = p + q
            if candidate != original and (int(simple_hash(candidate), 16) & MASK) == target:
                return candidate

    raise RuntimeError("Não achou pré-imagem com esses parâmetros")



name = "caixeta"
found = find_second_preimage(original=name, alphabet="abcdefghijklmnopqrstuvwxyz")
print("original:", name)
print("found   :", found)
print("hashes  :", simple_hash(name), simple_hash(found))


""" QUESTAO 6 """

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def mine(base: str, target_prefix: str) -> str:
    from itertools import count
    for i in count():
        candidate = f"{base}{i}"
        h = sha256_hex(candidate)
        if h.startswith(target_prefix):
            print(f"[ok] {candidate} -> {h[:10]}...")
            return candidate


"""
base = "bitcoin"
results = []
results.append(mine(base, "cafe"))
results.append(mine(base, "faded"))
results.append(mine(base, "decade"))
"""
