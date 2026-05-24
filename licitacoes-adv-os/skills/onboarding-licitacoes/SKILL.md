---
name: onboarding-licitacoes
description: >
  Wizard de configuracao inicial do plugin no ambiente do escritorio especialista em licitacoes. Coleta identidade do advogado (nome, OAB e UF), escritorio, cidade e UF de atuacao (eixo critico - Protocolo 5: TCE/TCM aplicavel, foro estadual, JF para MS contra autoridade federal), AREA_FOCO (consultivo-edital / contencioso-administrativo / tcu-tce / judicial / todos), frentes ativas, tom de voz e modo de melhor saida. Grava persona local em `<cwd>/licitacoes/persona.md` (fora do plugin distribuido). LGPD + sigilo comercial reforcado - alerta agressivo se pasta sincronizada (proposta, planilha de custos e segredo industrial sao sigilosos - Lei 9.279/96 art. 195 XI + Lei 14.133 arts. 13 §3º e 17). Aciona: configurar plugin, primeira vez, /start-licitacoes, onboarding, instalar, comecar a usar, configurar escritorio, persona.
---

# ONBOARDING LICITACOES

> Wizard de configuracao inicial **Tier 0**. Linguagem acolhedora, tom didatico. Conduz o operador a configurar o plugin ao perfil do escritorio especialista em licitacoes - com atencao especial a **localizacao** (cidade + UF - eixo do Protocolo 5), a **AREA_FOCO** (define prioridade de roteamento) e ao alerta de **sigilo comercial agressivo** (proposta + planilha + segredo industrial - PA-09, PA-22).

---

## 0. Escopo e acionamento

Acionada por `/start-licitacoes` ou quando o operador disser "configurar plugin", "primeira vez", "onboarding", "instalar", "configurar escritorio". Cria a pasta `licitacoes/` no diretorio de trabalho com identidade, localizacao, AREA_FOCO, frentes, tom e modo de melhor saida.

## 1. Posicao na orquestra

- **Chamada por:** `/start-licitacoes` ou intencao de configuracao.
- **Entrega para:** arquivos de runtime em `<cwd>/licitacoes/` - lidos por `licitacoes-master`, `validador-legislacao-vigente`, `calendario-licitatorio` e todas as demais skills via hook SessionStart.
- Roda uma vez na instalacao; idempotente nas execucoes seguintes.

## 2. Regras do wizard

1. Portugues (Brasil), tom acolhedor e direto.
2. Uma pergunta por vez para campos criticos; agrupar quando fizer sentido.
3. Defaults inteligentes - operador aceita com Enter.
4. Validar em tempo real (OAB numerica/com pontos, UF com 2 letras maiusculas, email).
5. Confirmar antes de gravar (resumo + "confirma? s/n").
6. **Idempotencia** - se ja existe `licitacoes/cowork-state.json`, perguntar atualizar vs recriar; nunca sobrescrever sem confirmacao.
7. **Sigilo comercial reforcado (PA-09, PA-22)** - NUNCA pedir nome de cliente PJ, CNPJ, conteudo de proposta, planilha de custos, segredo industrial. NUNCA armazenar esses dados no estado.
8. **Localizacao** (cidade + UF) e campo critico - explicar por que importa (P5: TCU x TCE x TCM x foro JF/JE).
9. **AREA_FOCO** define prioridade de roteamento pelo `licitacoes-master` - explicar com clareza.

## 3. Fluxo do wizard

### Bloco 0 - Abertura

> "Ola! Sou o assistente do **Plugin Licitacoes Adv-OS**. Vou te guiar na configuracao (~5 min). Ao final, as 33 skills estarao adaptadas ao seu escritorio (consultivo pre-edital + impugnacao + recurso + contrato + sancao + TCU/TCE + judicial). Pronto?"

### Bloco 1 - Diretorio (sigilo comercial reforcado)

Detectar cwd. Mostrar:

> "Vou criar `licitacoes/` em `<cwd>`.
>
> **ALERTA SIGILO COMERCIAL (PA-09, PA-22):** plugin opera proposta + planilha de custos + segredo industrial - dados sensiveis (Lei 9.279/96 art. 195 XI - crime de concorrencia desleal; Lei 14.133 arts. 13 §3º e 17 - sigilo de proposta antes da abertura). Pasta dentro de iCloud/OneDrive/Dropbox/Drive sincroniza esses dados para a nuvem = vazamento de proposta com potencial nulidade do certame + responsabilidade do advogado. Recomendo caminho local (ex.: `~/Dev/licitacoes/`). Confirma?"

Pasta sincronizada -> alertar 2x; so prosseguir com "confirmo o risco" expresso.

### Bloco 2 - Identidade do advogado

> "Sua identidade:
> 1. Nome completo do advogado responsavel?
> 2. Numero da OAB?
> 3. UF da OAB?
> 4. Nome do escritorio?
> 5. Email institucional (opcional)?
> 6. Telefone (opcional)?"

Validar OAB (digitos/pontos), UF (2 letras maiusculas), email. **OAB ativa sustenta responsabilidade tecnica (PA-07).**

### Bloco 3 - Localizacao (eixo do Protocolo 5)

> "Localizacao do escritorio:
> 1. Cidade-sede?
> 2. UF de atuacao predominante?
>
> Por que importa (P5):
> - MS contra autoridade federal -> JF (CF art. 109 I + Lei 12.016/2009 art. 2º);
> - MS estadual/municipal -> JE;
> - Representacao -> TCU (recurso federal - Lei 8.443/1992) ou TCE estadual ou TCM (onde existir - SP capital, RJ, BA, GO, CE);
> - Civel/anulatoria/cobranca -> Vara da Fazenda Publica da JE local, ou JF para uniao.
>
> A esfera do ente licitante (federal/estadual/municipal/estatal) e confirmada por caso no `CASO.md`."

Gravar `cidade` e `uf`.

### Bloco 4 - AREA_FOCO (prioridade de roteamento)

> "Area predominante (define priorizacao do `licitacoes-master`):
> 1. **consultivo-edital** - pareceres pre-edital, analise de risco, ETP/TR, matriz de risco, planejamento de proposta. Tier 1-2 com peso. Ticket alto.
> 2. **contencioso-administrativo** - impugnacao, recurso, contrarrazoes, defesa em apenamento, PAR. Tier 2-5.
> 3. **tcu-tce** - representacao ao TCU/TCE com cautelar. Tier 6 (parte). Frente especializada.
> 4. **judicial** - MS, anulatoria, cobranca, indenizacao. Tier 6 (parte).
> 5. **todos** *(default)* - 4 frentes.
>
> Toda demanda passa pela triagem por FASE - `area_foco` so prioriza."

### Bloco 5 - Frentes ativas

> "Frentes atendidas (multi-select ou `todas`):
> - consultivo-licitacao (pre-edital + analise de oportunidade)
> - fase-interna-edital (ETP/TR/matriz de risco)
> - fase-externa-recurso (sessao publica, habilitacao, recurso)
> - contrato-administrativo (clausulas exorbitantes, garantia, fiscalizacao)
> - reequilibrio-rescisao (arts. 124-125, 137-139 Lei 14.133)
> - sancao-apenamento (art. 156 + PAD art. 158 Lei 14.133)
> - par-anticorrupcao (Lei 12.846 + Decreto 11.129/2022)
> - controle-externo-tcu (representacao + cautelar art. 276 RI TCU)
> - judicial-ms-anulatoria (MS Lei 12.016 + anulatoria CPC)
> - compliance-publico (programa de integridade)"

### Bloco 6 - Subdominios

> "Subdominios (multi-select ou `todos`):
> - obras-engenharia (BDI, encargos, cronograma, garantia quinquenal CC art. 618)
> - servicos-comuns
> - tic-software (IN SGD - quando aplicavel)
> - publicidade-governamental (Lei 12.232/2010)
> - concessao-ppp (Lei 8.987/1995 + Lei 11.079/2004 - v0.2 com profundidade)
> - estatal (Lei 13.303/2016 - v0.2 com profundidade)
> - dispensa-inexigibilidade (arts. 74-75 Lei 14.133)"

### Bloco 7 - Tom de voz

> "Perfil:
> 1. **tecnico-objetivo** *(default)* - direto, sem floreio;
> 2. **tecnico-didatico** - explicativo, com fundamentacao expandida;
> 3. **tecnico-formal** - estilo de peca contenciosa rigorosa.
>
> Intensidade combativa 0-10 *(default 4)*: 0=neutro/didatico; 10=maximo direto e assertivo nas pecas (impugnacao, recurso, representacao)."

### Bloco 8 - Modo de melhor saida

> "Em comparacao de estrategia (impugnar vs participar; recurso vs MS; representacao TCU vs judicial):
> 1. **recomenda-e-lista** *(default)* - recomenda E lista alternativas;
> 2. **apenas-lista** - so opcoes, voce decide."

### Bloco 9 - Confirmacao + gravacao

Resumo + "confirma? s/n". Se s -> gravar:
- `<cwd>/licitacoes/persona.md` (com tokens resolvidos)
- `<cwd>/licitacoes/cowork-state.json` (state do schema)
- `<cwd>/licitacoes/CLAUDE.md` (atalhos do operador)
- `<cwd>/licitacoes/MEMORY.md` (estado executivo do operador)

Adicionar `licitacoes/` ao `.gitignore` do projeto (LGPD + segredo comercial).

### Bloco 10 - Proximo passo

> "Pronto! `licitacoes-master` ja esta ativo. Sugestoes:
> - `/triagem` - identificar a fase de um caso novo;
> - `/edital` - analisar um edital publicado (carregar PDF em `<cwd>/licitacoes/casos/<slug>/arquivos/`);
> - `/caso-licitacao` - abrir/retomar caso;
> - `/status-licitacoes` - ver casos ativos."

## 4. Vedacoes especificas

- **PA-09 + PA-22** - NUNCA armazenar proposta, planilha de custos, segredo industrial, CNPJ de cliente ou dados de representante legal no state. Esses ficam em `<cwd>/licitacoes/casos/<slug>/arquivos/` (gitignored).
- **PA-07** - alertar sobre OAB ativa - responsabilidade tecnica do operador.
- **PA-18** - nunca citar outro plugin da familia no fluxo.
- Idempotente - jamais sobrescrever state sem confirmacao expressa.
- Pasta sincronizada (iCloud/OneDrive/Dropbox/Drive) - alerta agressivo 2x.

## 5. Protocolos acionados

- **P5 - Localizacao** - Bloco 3 captura cidade + UF; cada caso confirma esfera do ente.
- **P1 - Validador** - nao roda no onboarding (Selo emitido por caso, nao por setup).

## 6. Localizacao

Localizacao do escritorio (cidade + UF) e capturada e gravada em `<cwd>/licitacoes/persona.md`. Esfera do ente licitante (federal/estadual/municipal/estatal) e confirmada por caso no `CASO.md` (eixo do P5 - define TCU x TCE x TCM e JF x JE).

## 7. Integracao

**Chamada por:** `/start-licitacoes` ou intencao de configuracao.

**Entrega para:** runtime de todas as outras skills (via hook SessionStart -> `resolve-persona.py` -> `<cwd>/licitacoes/persona.md` -> tokens da persona resolvidos em runtime).

**Sem esta skill:** plugin opera com `context/persona-fallback.md` (generica, sem identidade) - utilizavel mas sem personalizacao por escritorio.
