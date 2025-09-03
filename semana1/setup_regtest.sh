#!/bin/bash
# Configura ambiente regtest e minera blocos iniciais

DATADIR=$HOME/bitcoin-regtest

echo "[1] Criando diretório de dados em $DATADIR"
mkdir -p $DATADIR

echo "[2] Iniciando bitcoind em regtest..."
bitcoind -regtest -daemon -datadir=$DATADIR

sleep 3

echo "[3] Criando wallet reg2 com chaves privadas..."
bitcoin-cli -regtest -datadir=$DATADIR createwallet "reg2" false false "" true true

echo "[4] Gerando endereço para mineração..."
ADDR_MINER=$(bitcoin-cli -regtest -datadir=$DATADIR -rpcwallet=reg2 getnewaddress)

echo "[5] Minerando 101 blocos..."
bitcoin-cli -regtest -datadir=$DATADIR generatetoaddress 101 "$ADDR_MINER"

echo "[6] Saldo inicial:"
bitcoin-cli -regtest -datadir=$DATADIR -rpcwallet=reg2 getbalance