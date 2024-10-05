from models import Usuario, Transacao
from database import conectar_banco, criar_tabelas

criar_tabelas()

# Simulação de criação de usuário e transações
usuario1 = Usuario("Carlos", saldo=1000)
transacao1 = Transacao("entrada", 500)
usuario1.adicionar_transacao(transacao1)

transacao2 = Transacao("saída", 200)
usuario1.adicionar_transacao(transacao2)

print(f"Usuário: {usuario1.nome}, Saldo: {usuario1.saldo}")
for transacao in usuario1.transacoes:
    print(f"{transacao.tipo.capitalize()} de {transacao.valor} em {transacao.data}")

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Bem-vindo ao MovtoDimDim em Python!"

if __name__ == '__main__':
    app.run(debug=True)

