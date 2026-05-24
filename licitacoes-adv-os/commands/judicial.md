---
description: Tier 6 - controle externo (representacao TCU/TCE art. 174 §1º Lei 14.133 + art. 113 §1º Lei 8.443 + cautelar art. 276 RI TCU) + judicial (MS Lei 12.016/2009 120d + anulatoria CPC + cobranca contra Fazenda Tema 905 STJ).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch
argument-hint: [referencia do ato impugnado + via (TCU / MS / anulatoria / cobranca)]
---

Voce foi acionado pelo comando `/judicial` do plugin Licitacoes Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** acoes de controle externo (TCU/TCE) + judiciais - Tier 6.

## PROTOCOLO

1. **Acionar `licitacoes-master`** para Selo + fase F6/F7 + esfera (P5).
2. Acionar `calendario-licitatorio`:
   - **MS**: decadencia de 120 dias art. 23 Lei 12.016/2009.
   - **Anulatoria/Cobranca**: prescricao quinquenal Decreto 20.910/1932.
   - **Representacao TCU**: sem prazo decadencial.
3. Conforme situacao:
   - **Representacao TCU/TCE** -> `representacao-tcu-tce` (art. 174 §1º + art. 113 §1º Lei 8.443 + cautelar art. 276 RI TCU - acordao vincula Administracao CF art. 71 IX).
   - **MS preventivo/repressivo** -> `ms-licitacao-contrato` (Lei 12.016/2009 + CF art. 5º LXIX - JF/JE/STJ/STF conforme autoridade).
   - **Anulatoria** -> `acao-anulatoria-licitacao` (CPC + art. 149 Lei 14.133 indenizacao do contratado de boa-fé + tutela urgencia CPC 300).
   - **Cobranca** -> `acao-cobranca-administracao` (CPC + art. 141 Lei 14.133 ordem cronologica + Tema 905 STJ Selic combinada + precatorio/RPV CF art. 100).
4. **Coordenacao P4** (cruzamento administrativo + TCU + judicial) - vias paralelas com aproveitamento defensivo cruzado.
5. Entrega passa por `revisao-final-licitacoes` (R1-R4).

**Skills:** `licitacoes-master` -> `calendario-licitatorio` -> [skills Tier 6 conforme via] -> `revisao-final-licitacoes`.
