#!/bin/bash
# Envia 10 BTC para um endereço novo e confirma minerando um bloco

DATADIR=$HOME/bitcoin-regtest

echo "[1] Gerando endereço de destino..."
ADDR_DEST=$(bitcoin-cli -regtest -datadir=$DATADIR -rpcwallet=reg2 getnewaddress)

echo "[2] Definindo taxa manual..."
bitcoin-cli -regtest -datadir=$DATADIR -rpcwallet=reg2 settxfee 0.0001

echo "[3] Enviando 10 BTC para $ADDR_DEST"
TXID=$(bitcoin-cli -regtest -datadir=$DATADIR -rpcwallet=reg2 sendtoaddress "$ADDR_DEST" 10)
echo "TXID: $TXID"

echo "[4] Minerando 1 bloco para confirmar..."
ADDR_MINER=$(bitcoin-cli -regtest -datadir=$DATADIR -rpcwallet=reg2 getnewaddress)
bitcoin-cli -regtest -datadir=$DATADIR generatetoaddress 1 "$ADDR_MINER"

echo "[5] Saldos:"
bitcoin-cli -regtest -datadir=$DATADIR -rpcwallet=reg2 getbalances