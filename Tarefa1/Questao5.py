import sys
sys.path.insert(0, 'functions')

from functions.hash1 import simple_hash

import itertools
from pathlib import Path

MASK = 0xFFFFFFFF
BASE = 31

def pow31(n: int) -> int:
    """Calcula (31^n mod 2^32)."""
    p = 1
    for _ in range(n):
        p = (p * BASE) & MASK
    return p

def find_second_preimage(
    original: str,
    alphabet: str = "abcdefghijklmnopqrstuvwxyz",
    len_prefix: int = 4,
    len_suffix: int = 4,
    verbose: bool = True
) -> str:
    
    target = int(simple_hash(original), 16)

    suffix_table = {}
    for tup in itertools.product(alphabet, repeat=len_suffix):
        q = ''.join(tup)
        hq = int(simple_hash(q), 16)
        suffix_table.setdefault(hq, q)

    pow_base_n = pow31(len_suffix)

    if verbose:
        print(f"Buscando prefixos (len={len_prefix}) ...")
    for i, tup in enumerate(itertools.product(alphabet, repeat=len_prefix), 1):
        p = ''.join(tup)
        hp = int(simple_hash(p), 16)
        needed = (target - (hp * pow_base_n & MASK)) & MASK
        q = suffix_table.get(needed)
        if q is not None:
            candidate = p + q
            if candidate != original and int(simple_hash(candidate), 16) == target:
                return candidate

    raise RuntimeError("Não achou pré-imagem com esses parâmetros")



name = "gabriel"
found = find_second_preimage(original=name, alphabet="abcdefghijklmnopqrstuvwxyz", len_prefix=4,len_suffix=4)
print("original:", name)
print("found   :", found)
print("hashes  :", simple_hash(name), simple_hash(found))