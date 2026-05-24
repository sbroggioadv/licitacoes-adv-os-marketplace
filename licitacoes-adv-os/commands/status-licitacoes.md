---
description: Status do caso ativo (ou caso especifico) - fase atual + fases paralelas (P4) + Selo vigente + proximo prazo critico + skills acionadas + alertas. Le CASO.md sem expor identidade do cliente (PA-22).
allowed-tools: Read, Bash, Glob, Grep
argument-hint: [opcional - slug do caso especifico]
---

Voce foi acionado pelo comando `/status-licitacoes` do plugin Licitacoes Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** mostrar status sintetico do(s) caso(s) ativo(s) - fase, prazos, Selo, vias paralelas.

## PROTOCOLO

1. **Acionar `memoria-de-caso-licitacao`** com subcomando de status.
2. Caso especifico (slug) -> ler `<cwd>/licitacoes/casos/<slug>/CASO.md` integralmente.
3. Sem slug -> listar todos os casos em `<cwd>/licitacoes/casos/` com:
   - Slug (sem expor identidade - PA-22)
   - Fase atual (F1-F7)
   - Fases paralelas (P4 - quando aplicavel)
   - Proximo prazo critico (com data)
   - Selo vigente (data-base + validade 60 dias)
   - Skills mais recentes acionadas
4. **Alertas:**
   - Selo expirado (>60 dias) -> "acionar `validador-legislacao-vigente`".
   - Prazo proximo (<7 dias) -> destacar.
   - Pasta sincronizada detectada -> warning.

**Skill a acionar:** `memoria-de-caso-licitacao`.
