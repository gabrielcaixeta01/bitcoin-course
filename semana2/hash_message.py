import hashlib

def sha256_hash(message: str) -> str:
    return hashlib.sha256(message.encode()).hexdigest()

if __name__ == "__main__":
    msg = input("Digite a mensagem: ")
    h = sha256_hash(msg)
    print("Mensagem:", msg)
    print("SHA-256:", h)