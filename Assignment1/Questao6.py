import sys
import hashlib
sys.path.insert(0, 'functions')



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


base = "bitcoin"
results = []
results.append(mine(base, "cafe"))
results.append(mine(base, "faded"))
results.append(mine(base, "decade"))