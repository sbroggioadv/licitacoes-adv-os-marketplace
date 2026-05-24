---
description: "Tier 3 - recurso administrativo (art. 165 Lei 14.133/2021 - 3 dias uteis). Pre-requisito ABSOLUTO: intencao motivada na sessao (PA-19 - preclusao Sum. TCU 274). Efeito suspensivo automatico."
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch
argument-hint: [referencia do ato recorrido]
---

Voce foi acionado pelo comando `/recurso` do plugin Licitacoes Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** peca CRITICA da fase F3 - recurso administrativo contra ato (inabilitacao/desclassificacao/adjudicacao).

## PROTOCOLO

1. **Acionar `licitacoes-master`** para Selo + fase F3 + esfera.
2. Acionar `calendario-licitatorio` - prazo 3 dias uteis art. 165 Lei 14.133.
3. **Verificar intencao de recurso na sessao** (PA-19 - art. 165 §1º + Sum. TCU 274) - pre-requisito ABSOLUTO. Sem intencao motivada = inadmissivel.
4. Conforme situacao, acionar:
   - **Defesa de exequibilidade** (`proposta-exequibilidade` - art. 59 §4º 70%) se desclassificacao por inexequibilidade.
   - **Habilitacao** (`habilitacao-documentos` - arts. 66-70 + Sum. TCU 269) se inabilitacao.
   - **Tratamento ME/EPP** (`tratamento-me-epp` - LC 123) se enquadramento.
5. Acionar `recurso-administrativo` para redigir a peca - FIRAC + 6 secoes + fundamentacao tripla + vinculacao ao edital + pedidos sucessivos.
6. Entrega passa por `revisao-final-licitacoes` (R1-R4).
7. Se improvido -> coordenacao P4 com `representacao-tcu-tce` + `ms-licitacao-contrato`.

**Modo contrarrazoes:** se concorrente recorre contra ato favoravel ao cliente, acionar `contrarrazoes-recurso`.

**Skills:** `licitacoes-master` -> `calendario-licitatorio` -> [skills auxiliares] -> `recurso-administrativo` (ou `contrarrazoes-recurso`) -> `revisao-final-licitacoes`.
