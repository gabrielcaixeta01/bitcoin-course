import hashlib
from ecdsa import SigningKey, SECP256k1, util

sig1_hex = "4264b8b1ef4c77bf259a8d144689a0e6ea1aa6daf3761eb28b8b8669cf72f73907d78eea283d3841716efdd6eae4f559bc670f2674d0e4ffb66774c4796f71e6"
sig2_hex = "4264b8b1ef4c77bf259a8d144689a0e6ea1aa6daf3761eb28b8b8669cf72f73905a3eb1483b5498908be8c05c40da3e5a4d5d5cdfb1dc1f8adaca890a67605b0"

m1 = b"Edil Medeiros"
m2 = b"Neha Narula"
target_msg = b"I broke ECDSA again!"
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

r1 = int(sig1_hex[:64], 16)
s1 = int(sig1_hex[64:], 16)
r2 = int(sig2_hex[:64], 16)
s2 = int(sig2_hex[64:], 16)

assert r1 == r2, "Nao usaram o mesmo k"
r = r1

z1 = int.from_bytes(hashlib.sha256(m1).digest(), "big")
z2 = int.from_bytes(hashlib.sha256(m2).digest(), "big")

numerador = (z1 - z2) % n
denominador = (s1 - s2) % n
k = (numerador * pow(denominador, -1, n)) % n

d = ((s1 * k - z1) * pow(r, -1, n)) % n
d = d.to_bytes(32, "big")

sk = SigningKey.from_string(d, curve=SECP256k1)
sig_rs = sk.sign(target_msg, hashfunc=hashlib.sha256, sigencode=util.sigencode_string)
sig_hex = sig_rs.hex()

print("signature (r||s, hex):", sig_hex)