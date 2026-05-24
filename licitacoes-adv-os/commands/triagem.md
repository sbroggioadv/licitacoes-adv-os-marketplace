---
description: Atalho direto a triagem por fase do procedimento (F1-F7) + esfera do ente + vias paralelas. Aciona licitacoes-master + calendario-licitatorio + memoria-de-caso-licitacao.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [descricao do caso ou referencia do certame]
---

Voce foi acionado pelo comando `/triagem` do plugin Licitacoes Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** identificar rapidamente a fase do procedimento + esfera + vias paralelas para rotear ao Tier correto.

## PROTOCOLO

1. **Acionar `licitacoes-master`** para triagem por fase.
2. Identificar:
   - **Fase atual** (F1 pre-edital | F2 edital | F3 sessao/habilitacao/recurso | F4 contrato | F5 sancao/PAR | F6 TCU/TCE | F7 judicial).
   - **Fases paralelas** (P4 - exemplo F5 + F7).
   - **Esfera do ente** (P5 - federal/estadual/municipal/estatal).
   - **Regime aplicavel** (Lei 14.133 vs Lei 8.666 residual - PA-03).
3. Atualizar `CASO.md` via `memoria-de-caso-licitacao`.
4. Acionar `calendario-licitatorio` para mapear prazos da fase.
5. Acionar `validador-legislacao-vigente` para emitir Selo.
6. Recomendar skill(s) Tier 1-6 a acionar em sequencia.

**Skills a acionar (encadeadas):** `licitacoes-master` -> `calendario-licitatorio` -> `validador-legislacao-vigente` -> Tier correspondente.
