# Laboratório de segurança

Código de teste **do próprio projeto**, de laboratório, para praticar a skill [`vulnerability-analysis`](../skills/vulnerability-analysis/SKILL.md) com o DIO Agent. Nada aqui usa sistemas de terceiros.

## Arquivos

- [`app.py`](app.py) — um login **intencionalmente vulnerável** a SQL Injection. A consulta é montada concatenando o que a pessoa digitou.
- [`app_fixed.py`](app_fixed.py) — a **versão corrigida**, com consulta parametrizada (prepared statement).

## Como rodar

Só precisa de Python 3 (usa `sqlite3`, que já vem na biblioteca padrão):

```bash
python3 lab/app.py        # veja o ataque  ' OR '1'='1  funcionar
python3 lab/app_fixed.py  # o mesmo ataque deixa de funcionar
```

## Como usar com o agente

Abra o harness na pasta do projeto e peça algo como:

> Aja como especialista em AppSec. Analise o `lab/app.py`, encontre a falha, explique a exploração, cite a técnica do MITRE ATT&CK e me oriente a corrigir.

Depois de aplicar a correção (ou de apontar o `app_fixed.py`), peça uma nova varredura para confirmar que o SQL Injection foi mitigado. O agente deve seguir a skill `vulnerability-analysis` e entregar a ficha padronizada (impacto, probabilidade e severidade).
