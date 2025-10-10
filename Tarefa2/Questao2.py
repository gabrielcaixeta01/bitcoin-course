import hashlib
from ecdsa import SigningKey, SECP256k1, util


signature_hex = "133c76589b4cce6898e63a366e40d43a6471db814f5a354d52c4abcd067942780cc9b3d891c9a4eb8bcce6edc20f31937005595a7f7ea6a4bf20c3f6367f5155"
k_hex = "718768e4b0ec256839ddcba80b7902a361d525f4be8c4904c275edd35625afb5"

message_orig = b"Satoshi Nakamoto"
target_msg = b"I broke ECDSA!"

n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

r = int(signature_hex[:64], 16)
s = int(signature_hex[64:], 16)
k = int(k_hex, 16)
z = int.from_bytes(hashlib.sha256(message_orig).digest(), "big")

r_inv = pow(r, -1, n)
d = ((s * k - z) * r_inv) % n
d = d.to_bytes(32, "big")

sk = SigningKey.from_string(d, curve=SECP256k1)
sig_rs = sk.sign(target_msg, hashfunc=hashlib.sha256, sigencode=util.sigencode_string)
sig_hex = sig_rs.hex()

print(sig_hex)