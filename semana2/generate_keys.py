from bitcoin import random_key, privtopub, pubtoaddr

# Gera uma chave privada aleatória
priv_key = random_key()
print("Chave privada:", priv_key)

# Obtém a chave pública correspondente
pub_key = privtopub(priv_key)
print("Chave pública:", pub_key)

# Gera o endereço Bitcoin a partir da chave pública
address = pubtoaddr(pub_key)
print("Endereço Bitcoin:", address)