---
description: Abre, retoma ou lista caso licitatorio em `licitacoes/casos/`. Compartimentado por certame (PA-22 + sigilo comercial PA-09). Suporta `novo <slug>`, `<slug>` (retomar), `list`, `arquivar <slug>`.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [novo <slug> | <slug> | list | arquivar <slug>]
---

Voce foi acionado pelo comando `/caso-licitacao` do plugin Licitacoes Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** gerenciar pasta de caso/certame - compartimentacao absoluta por LGPD + sigilo comercial (PA-09, PA-22).

## PROTOCOLO

1. **Acionar a skill `memoria-de-caso-licitacao`** - orquestra CRUD do caso.
2. Subcomandos:
   - `novo <slug>` -> cria `<cwd>/licitacoes/casos/<slug>/` com `CASO.md` (estrutura canonica) + `arquivos/` (gitignored). Slug **deterministico** (UF-orgao-ano-modalidade-seq) **sem expor identidade** do cliente.
   - `<slug>` -> retoma caso; verifica **Selo** vigente (>60 dias = expirado).
   - `list` -> lista slugs em `casos/` (sem expor identidade).
   - `arquivar <slug>` -> move para `casos/_arquivados/`.
3. **Sigilo:** proposta + planilha de custos + segredo industrial **nunca** no plugin distribuido - apenas em `casos/<slug>/arquivos/` (gitignored).
4. **Warning** se pasta sincronizada (iCloud/OneDrive/Dropbox/Drive) - Lei 14.133 arts. 13 §3º e 17 + Lei 9.279/96.

**Skill a acionar:** `memoria-de-caso-licitacao`.
