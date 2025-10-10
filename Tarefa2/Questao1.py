import hashlib
from ecdsa import SigningKey, SECP256k1, util

def pubkey_compressed_from_vk(vk):
    xy = vk.to_string()
    x = xy[:32]
    y = xy[32:]

    prefix = b'\x02' if (y[-1] % 2 == 0) else b'\x03'
    return prefix + x


sk = SigningKey.generate(curve=SECP256k1)
vk = sk.get_verifying_key()

message = b"Hello Bitcoin!"

pb_compressed = pubkey_compressed_from_vk(vk)
pub_hex = pb_compressed.hex()

sig_rs = sk.sign(message, hashfunc=hashlib.sha256, sigencode=util.sigencode_string)
sig_hex = sig_rs.hex()

print("Public key (compressed, 66 hex):", pub_hex)
print("Signature (r||s, 128 hex):     ", sig_hex)