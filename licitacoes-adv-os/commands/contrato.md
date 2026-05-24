---
description: Tier 4 - contrato administrativo (arts. 89-145 Lei 14.133) + reequilibrio (arts. 124-125 - revisao/reajuste/repactuacao) + aditivo (vs apostilamento art. 136) + rescisao (art. 137 - inclui §4º atraso 90 dias da Administracao).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch
argument-hint: [referencia do contrato + tema (analise / reequilibrio / aditivo / rescisao)]
---

Voce foi acionado pelo comando `/contrato` do plugin Licitacoes Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** consultivo + defesa em contrato administrativo - Tier 4.

## PROTOCOLO

1. **Acionar `licitacoes-master`** para Selo + fase F4 + esfera.
2. Conforme situacao concreta:
   - **Analise integral** do contrato/minuta -> `contrato-administrativo` (arts. 89-145, clausulas exorbitantes art. 104, garantia arts. 96-100).
   - **Matriz de risco** -> `analise-matriz-risco` (art. 22).
   - **Reequilibrio** -> `reequilibrio-economico-financeiro` (arts. 124-125 + 3 especies: revisao/reajuste/repactuacao + Tema 905 STJ Selic).
   - **Aditivo/apostilamento** -> `aditivo-contratual` (distincao critica - limites 25%/50%).
   - **Rescisao** -> `rescisao-contrato` (art. 137 - 4 hipoteses; §4º atraso >90 dias da Administracao).
   - **Gestao + fiscalizacao** -> `gestao-cronograma-fiscalizacao` (art. 119 diario + notificacoes formais).
3. Entrega passa por `revisao-final-licitacoes` (R1-R4).
4. Se questao judicial -> coordenacao P4 com `acao-cobranca-administracao` + `acao-anulatoria-licitacao` + `ms-licitacao-contrato`.

**Skills:** `licitacoes-master` -> [skills Tier 4 conforme situacao] -> `revisao-final-licitacoes`.
