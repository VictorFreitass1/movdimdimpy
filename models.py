from datetime import datetime

class Usuario:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
        self.saldo += transacao.valor

class Transacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo  # 'entrada' ou 'saída'
        self.valor = valor if tipo == 'entrada' else -valor
        self.data = datetime.now()
