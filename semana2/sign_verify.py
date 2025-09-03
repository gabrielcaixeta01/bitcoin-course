from ecdsa import SigningKey, SECP256k1

# Gerar chave privada e pública
sk = SigningKey.generate(curve=SECP256k1)
vk = sk.verifying_key

message = b"Transacao de teste"
signature = sk.sign(message)

print("Mensagem:", message)
print("Assinatura:", signature.hex())

# Verificação
try:
    vk.verify(signature, message)
    print("Assinatura verificada com sucesso!")
except:
    print("Assinatura inválida!")