"""
app.py - CÓDIGO DE LABORATÓRIO, INTENCIONALMENTE VULNERÁVEL

Este é um login simples e PROPOSITALMENTE inseguro, usado para praticar
análise de vulnerabilidade com o DIO Agent (skill vulnerability-analysis).

A FALHA: a consulta SQL é montada concatenando diretamente o que a pessoa
digitou. Isso abre uma brecha de SQL Injection.

NÃO use este padrão em produção. A versão corrigida está em app_fixed.py.
Rode apenas no seu próprio ambiente de laboratório.
"""

import sqlite3


def criar_banco_de_teste():
    """Cria um banco em memória com um usuário de exemplo (dados fictícios)."""
    conexao = sqlite3.connect(":memory:")
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE usuarios (id INTEGER, usuario TEXT, senha TEXT)")
    cursor.execute("INSERT INTO usuarios VALUES (1, 'admin', 'senha_super_secreta')")
    conexao.commit()
    return conexao


def login(conexao, usuario, senha):
    cursor = conexao.cursor()

    # VULNERÁVEL: a entrada do usuário é concatenada direto na consulta.
    # Um valor como  ' OR '1'='1  no campo senha faz a condição ser sempre
    # verdadeira e autentica sem conhecer a senha.
    consulta = (
        "SELECT * FROM usuarios "
        f"WHERE usuario = '{usuario}' AND senha = '{senha}'"
    )
    print(f"[debug] SQL executado: {consulta}")

    cursor.execute(consulta)
    resultado = cursor.fetchone()
    return resultado is not None


if __name__ == "__main__":
    conexao = criar_banco_de_teste()

    print("== Login legítimo ==")
    print("Acesso liberado?", login(conexao, "admin", "senha_super_secreta"))

    print("\n== Senha errada ==")
    print("Acesso liberado?", login(conexao, "admin", "chute_qualquer"))

    print("\n== Ataque de SQL Injection (sem saber a senha) ==")
    print("Acesso liberado?", login(conexao, "admin", "' OR '1'='1"))
