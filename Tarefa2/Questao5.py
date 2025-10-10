from ecdsa import SECP256k1

INP = "data/f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16.dat"
OUT = "solutions/exercise05.txt"
N = SECP256k1.order

raw = open(INP, "rb").read()

s = raw.decode().strip()
tx = bytes.fromhex(s) if len(s) % 2 == 0 and all(c in "0123456789abcdefABCDEF" for c in s) else raw

i = 0
while i < len(tx) and tx[i] != 0x30:
    i += 1

ln = tx[i+1]
p = i + 2

assert tx[p] == 0x02; p += 1
lr = tx[p]; p += 1
r_bytes = tx[p:p+lr]; p += lr

assert tx[p] == 0x02; p += 1
ls = tx[p]; p += 1
s_bytes = tx[p:p+ls]

r32 = int.from_bytes(r_bytes, "big").to_bytes(32, "big")
s  = int.from_bytes(s_bytes, "big")
sprime32 = ((N - s) % N).to_bytes(32, "big")

buf = bytearray(113)               
buf[47:79] = r32                   
buf[79:81] = b"\x00\x00"   
buf[81:113] = sprime32

print(buf.hex())