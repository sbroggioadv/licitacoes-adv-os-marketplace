---
description: Tier 2 - analise integral de edital + deteccao de vicios + impugnacao + esclarecimento + planejamento de proposta. Fase F2 do procedimento.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch
argument-hint: [referencia do edital ou caminho do PDF]
---

Voce foi acionado pelo comando `/edital` do plugin Licitacoes Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** analise integral do edital + identificacao de vicios + estrategia (impugnar/esclarecer/participar).

## PROTOCOLO

1. **Acionar `licitacoes-master`** para confirmar fase F2 + esfera + Selo via `validador-legislacao-vigente`.
2. Carregar edital + anexos em `<cwd>/licitacoes/casos/<slug>/arquivos/` (gitignored - PA-09).
3. Acionar `analise-edital` - checklist 14 dimensoes (modalidade, criterio art. 33, objeto, regime, habilitacao arts. 66-70, contrato art. 92, garantia arts. 96-100, etc.).
4. Acionar `analise-etp-tr` se ha ETP + TR disponiveis (preventivamente).
5. Acionar `analise-matriz-risco` se ha matriz (art. 22).
6. Acionar `deteccao-vicios-edital` para catalogo dos 15 vicios.
7. Decisao estrategica: **impugnar** (`impugnacao-edital` - prazo 3 dias uteis art. 164) / **esclarecer** (`esclarecimento-edital` - art. 164 §1º) / **participar** (`planejamento-proposta`).
8. Entrega passa por `revisao-final-licitacoes` (R1-R4).

**Skills:** `licitacoes-master` -> `analise-edital` -> `deteccao-vicios-edital` -> [`impugnacao-edital` OU `esclarecimento-edital` OU `planejamento-proposta`].
