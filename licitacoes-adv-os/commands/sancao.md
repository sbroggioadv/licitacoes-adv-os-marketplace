---
description: Tier 5 - defesa em sancao (art. 156 + 158 Lei 14.133 - 15 dias) + PAR Lei 12.846 (Decreto 11.129/2022 - 30 dias) + acordo de leniencia + programa de integridade (atenuante ate 4%). Coordenacao bis in idem (PA-12).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch
argument-hint: [referencia da notificacao + tipo (apenamento / PAR / leniencia / compliance)]
---

Voce foi acionado pelo comando `/sancao` do plugin Licitacoes Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** defesa em processo sancionatorio - apenamento art. 156 ou PAR Lei 12.846 - Tier 5.

## PROTOCOLO

1. **Acionar `licitacoes-master`** para Selo + fase F5 + esfera.
2. Acionar `calendario-licitatorio`:
   - Defesa **art. 156**: 15 dias uteis art. 158 Lei 14.133.
   - Defesa **PAR**: 30 dias uteis Decreto 11.129/2022 art. 13.
3. Conforme situacao:
   - **Apenamento Lei 14.133** -> `defesa-apenamento-art-156` (4 sancoes: advertencia/multa/impedimento/inidoneidade; dosimetria art. 156 §3º).
   - **PAR Lei 12.846** -> `par-lei-12846` (multa 0,1-20% faturamento + publicacao extraordinaria).
   - **Acordo de leniencia** -> `acordo-leniencia` (reducao ate 2/3 + isencao de inidoneidade).
   - **Programa de integridade** -> `programa-integridade-compliance` (16 parametros - atenuante ate 4% Decreto 11.129/2022 arts. 56-58).
4. **Bis in idem** (PA-12): se ha apenamento + PAR concomitantes, articular preliminar.
5. Entrega passa por `revisao-final-licitacoes` (R1-R4).
6. Se decisao desfavoravel -> coordenacao P4 com `ms-licitacao-contrato` (120d) + `acao-anulatoria-licitacao` (CPC).

**Skills:** `licitacoes-master` -> `calendario-licitatorio` -> [skills Tier 5 conforme] -> `revisao-final-licitacoes`.
