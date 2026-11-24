"""
app_fixed.py - VERSÃO CORRIGIDA do app.py

A correção: a consulta passou a usar CONSULTA PARAMETRIZADA (prepared
statement). Os valores digitados viajam separados do comando SQL, como
parâmetros (os '?'), então não conseguem mais alterar a estrutura da
consulta. Isso mitiga o SQL Injection.

Rode e compare com app.py: o ataque  ' OR '1'='1  deixa de funcionar.
"""

import sqlite3


def criar_banco_de_teste():
    conexao = sqlite3.connect(":memory:")
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE usuarios (id INTEGER, usuario TEXT, senha TEXT)")
    cursor.execute("INSERT INTO usuarios VALUES (1, 'admin', 'senha_super_secreta')")
    conexao.commit()
    return conexao


def login(conexao, usuario, senha):
    cursor = conexao.cursor()

    # CORRIGIDO: os valores entram como parâmetros (?), separados do comando.
    # O driver do banco trata 'usuario' e 'senha' como dados, nunca como SQL.
    consulta = "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?"
    cursor.execute(consulta, (usuario, senha))

    resultado = cursor.fetchone()
    return resultado is not None


if __name__ == "__main__":
    conexao = criar_banco_de_teste()

    print("== Login legítimo ==")
    print("Acesso liberado?", login(conexao, "admin", "senha_super_secreta"))

    print("\n== Senha errada ==")
    print("Acesso liberado?", login(conexao, "admin", "chute_qualquer"))

    print("\n== Mesmo ataque de SQL Injection de antes ==")
    print("Acesso liberado?", login(conexao, "admin", "' OR '1'='1"))
    # Agora retorna False: a injeção foi mitigada.
