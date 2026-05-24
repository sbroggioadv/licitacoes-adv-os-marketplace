---
description: Cadeia completa de orquestracao - injeta 4 Camadas (22 PAs + 6 Protocolos + FIRAC), faz triagem por fase (F1-F7), identifica esfera (federal/estadual/municipal/estatal), roteia ao Tier correto, exige Selo P1, garante R1-R4.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch
argument-hint: [demanda - descricao do caso]
---

Voce foi acionado pelo comando `/licitacoes-master` do plugin Licitacoes Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** cadeia completa de orquestracao do plugin - da triagem ate a entrega revisada.

## PROTOCOLO

1. **Acionar a skill `licitacoes-master`** - orquestradora invariante Tier 0.
2. Triagem por **fase do procedimento** (F1 pre-edital -> F2 edital -> F3 sessao/habilitacao/recurso -> F4 contrato -> F5 sancao/PAR -> F6 TCU/TCE -> F7 judicial).
3. Identificar **esfera** do ente (P5 - federal/estadual/municipal/estatal) e **fases paralelas** (P4).
4. Acionar `validador-legislacao-vigente` para emitir Selo de Validacao Legal Previa (PA-04).
5. Acionar skills Tier 1-6 conforme fase identificada.
6. **Antes da entrega** - acionar `revisao-final-licitacoes` (R1-R4) - veredito APROVADO/REVISAR/BLOQUEADO.
7. Atualizar `CASO.md` via `memoria-de-caso-licitacao`.

**Skill a acionar:** `licitacoes-master`.
