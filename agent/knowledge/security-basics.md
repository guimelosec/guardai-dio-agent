# Fundamentos de segurança

Conceitos de base que o agente usa ao conduzir uma análise de vulnerabilidade. A skill que consome este arquivo é `skills/vulnerability-analysis/SKILL.md`. Leia este arquivo sempre que a conversa envolver segurança, análise de código ou avaliação de risco.

## Os três conceitos que as pessoas confundem

Entender a diferença entre eles é o que separa uma análise amadora de uma profissional.

- **Vulnerabilidade:** uma **fraqueza** no sistema. É a porta destrancada. Exemplos: um código que monta SQL juntando o que o usuário digitou, uma senha padrão que ninguém trocou, uma porta aberta sem necessidade. A vulnerabilidade existe mesmo que ninguém a explore.
- **Ameaça:** o **agente ou evento** que pode explorar a vulnerabilidade. É o ladrão que pode entrar pela porta. Pode ser uma pessoa (um atacante), um programa (um malware) ou até um acidente.
- **Risco:** a **probabilidade** de uma ameaça explorar uma vulnerabilidade **vezes o impacto** disso. É a resposta à pergunta "o quão preocupado eu devo estar?". Risco alto = a porta está destrancada (vulnerabilidade), tem gente querendo entrar (ameaça) e dentro tem algo valioso (impacto).

Resumindo: **vulnerabilidade** é a falha, **ameaça** é quem a explora, **risco** é o quanto isso importa no seu contexto.

## A tríade CIA

Toda a segurança da informação se organiza em torno de três propriedades. Quando uma falha é explorada, ela viola uma ou mais delas. Na análise, sempre diga qual lado da tríade está em jogo.

- **Confidencialidade (Confidentiality):** só quem tem autorização acessa a informação. É violada quando dados vazam (um SQL Injection que lê a tabela de usuários, por exemplo).
- **Integridade (Integrity):** a informação não é alterada de forma indevida. É violada quando alguém modifica ou apaga dados que não deveria (adulterar um registro, um ataque que altera o saldo de uma conta).
- **Disponibilidade (Availability):** o sistema está acessível para quem precisa, quando precisa. É violada por ataques que derrubam o serviço (negação de serviço, ransomware que trava tudo).

Uma mesma falha pode atingir mais de um lado. SQL Injection, por exemplo, pode ler dados (confidencialidade), alterá-los (integridade) e até derrubar o banco (disponibilidade).

## Severidade: impacto × probabilidade

A severidade de uma falha não é uma propriedade fixa do código: ela depende do **contexto**. A regra prática:

- **Impacto:** se for explorada, o quão ruim é? (um dado público exposto é diferente de senhas vazando)
- **Probabilidade:** no cenário real, o quão fácil e provável é explorar? (um sistema exposto na internet sem autenticação é muito mais provável que um script que só roda na máquina local)
- **Severidade = combinação dos dois.** Escala usada nas análises: **Baixa**, **Média**, **Alta**, **Crítica**.

Por isso a skill pergunta o contexto antes de avaliar: a mesma linha de código pode ser Baixa num laboratório local e Crítica em produção exposta.

## Referências que o agente cita

- **OWASP Top 10:** lista das categorias de falhas mais comuns em aplicações web (Injection, Broken Access Control, Security Misconfiguration, etc.). Útil para nomear e classificar a falha. https://owasp.org/www-project-top-ten/
- **MITRE ATT&CK:** base de conhecimento de táticas e técnicas de atacantes, com códigos (ex.: `T1190 – Exploit Public-Facing Application`, que cobre exploração de aplicações expostas, como SQL Injection). Útil para explicar *como* a falha se encaixa no comportamento real de um atacante. https://attack.mitre.org/
- **CVE / CVSS:** CVE é o identificador público de uma vulnerabilidade conhecida; CVSS é a pontuação (0 a 10) que mede a severidade dela. Serve de referência quando a falha é de um componente conhecido.

## Boas práticas de defesa

Princípios que o agente recomenda. Mais importante que corrigir uma falha é adotar o padrão que impede a próxima.

- **Nunca confie na entrada do usuário.** Todo dado que vem de fora (formulário, URL, API, arquivo) é suspeito até ser validado. A causa raiz de muitas falhas é tratar entrada como se fosse confiável.
- **Consultas parametrizadas (prepared statements).** Nunca monte comandos SQL concatenando string com o que o usuário digitou. Use parâmetros, que separam o comando dos dados e eliminam a maior parte dos SQL Injection.
- **Validação e sanitização.** Valide formato, tipo e tamanho do que entra; escape o que sai (para evitar XSS, por exemplo).
- **Menor privilégio.** Cada parte do sistema (usuário, serviço, processo) recebe só a permissão mínima que precisa. Se for comprometida, o estrago é menor.
- **Defesa em profundidade.** Não dependa de uma única proteção. Camadas (validação + autenticação + firewall + logs) se cobrem.
- **Segredos fora do código.** Senhas, tokens e chaves nunca ficam escritos no código ou no repositório. Use variáveis de ambiente ou um cofre de segredos.
- **Mantenha tudo atualizado.** Boa parte dos ataques explora falhas já conhecidas e já corrigidas. Atualizar dependências e o sistema fecha essas portas.
- **Reduza a superfície de ataque.** Feche portas, serviços e permissões que não são usados. O que não existe não pode ser atacado.
- **Logs e monitoramento.** Você não defende o que não enxerga. Registrar o que acontece permite detectar e responder.
