---
description: Aciona diretamente a revisao tecnica R1-R4 (Suprema Corte) sobre entrega previa - 4 rodadas auditadas (escopo, tecnica juridica, conformidade, entrega). Veredito APROVADO / REVISAR / BLOQUEADO.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [referencia do artefato a revisar]
---

Voce foi acionado pelo comando `/revisao-final` do plugin Licitacoes Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** auditoria R1-R4 sobre entrega previa - peca administrativa, peca judicial, parecer, defesa, contrato, deck ou memoria de quantum.

## PROTOCOLO

1. **Acionar `revisao-final-licitacoes`** - Protocolo 6 - 4 rodadas:
   - **R1 Escopo e Dados** - entendimento + esfera + fase + vias + regime aplicavel + documentos.
   - **R2 Tecnica Juridica** - Selo P1 + normas vigentes (lei+artigo+ano) + sumula TCU (n°+tema) + jurisprudencia (Tema/REsp/RE+ano) + vinculacao ao edital (PA-15) + onus probatorio + prescricao + memoria de quantum.
   - **R3 Conformidade + Cruzamento** - foro (P5) + vias paralelas (P4) + prazos + esgotamento (PA-21) + preclusao (PA-19) + sigilo (PA-09/22) + sem critica pessoal (PA-08) + sem promessa (PA-02) + sem discricionariedade (PA-17) + sem orientacao a Administracao (PA-06) + ressalva OAB (PA-07).
   - **R4 Entrega e Clareza** - FIRAC + 6 secoes + fundamentacao tripla + memoria de quantum auditavel + linguagem tecnica + [VERIFICAR] sinalizados.
2. **Veredito:** APROVADO (libera) / REVISAR (ajustes) / BLOQUEADO (refazer).

**Skill a acionar:** `revisao-final-licitacoes`.
