---
description: Atalho direto a peca de impugnacao ao edital (art. 164 Lei 14.133 - 3 dias uteis). Estrutura FIRAC + 6 secoes + fundamentacao tripla + vinculacao ao edital (PA-15) + pedidos sucessivos.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch
argument-hint: [referencia do edital + vicio identificado]
---

Voce foi acionado pelo comando `/impugnacao` do plugin Licitacoes Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** redigir peca administrativa de impugnacao ao edital - prazo CRITICO 3 dias uteis antes da abertura (art. 164 Lei 14.133/2021).

## PROTOCOLO

1. **Acionar `licitacoes-master`** para Selo + verificacao de fase F2 + esfera.
2. Acionar `calendario-licitatorio` para confirmar tempestividade (3 dias uteis - art. 164 Lei 14.133).
3. Acionar `deteccao-vicios-edital` para catalogo de vicios (se nao feito previamente).
4. Acionar `impugnacao-edital` para redigir a peca:
   - Estrutura FIRAC + 6 secoes (Camada 3).
   - Fundamentacao tripla (lei + sumula TCU + jurisprudencia STJ - PA-13).
   - Vinculacao ao edital (PA-15).
   - Pedidos sucessivos (correcao + retificacao + republicacao + anulacao).
5. Entrega passa por `revisao-final-licitacoes` (R1-R4).
6. Se denegada -> coordenacao P4 com `representacao-tcu-tce` + `ms-licitacao-contrato`.

**Skills:** `licitacoes-master` -> `calendario-licitatorio` -> `deteccao-vicios-edital` -> `impugnacao-edital` -> `revisao-final-licitacoes`.
