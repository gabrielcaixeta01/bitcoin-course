m = b"transfer 100 BTC"
signature = "f474d12468415184847778e455189eb0a07df7696d69777008f59fe9ebe497727739e65b40f2a1587b47e953d6fdec9934e82c45c00fe41d446347f35b74708f"
public_key = "020e7d4f8640ec6f3382a1dd61b4b292f815864dc7b6c12ba2744597aa3504d674"

r = int(signature[:64], 16)
s = int(signature[64:], 16)
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

new_s = n - s
new_sig = (r.to_bytes(32, "big") + new_s.to_bytes(32, "big")).hex()
print(new_sig)