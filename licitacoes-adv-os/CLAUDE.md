# CLAUDE.md — Plugin Licitacoes Adv-OS

> Instrucoes para futuras sessoes neste sub-repositorio. Ler PRIMEIRO ao retomar trabalho.
> Estende o CLAUDE.md da familia de plugins Adv-OS e os niveis superiores do workspace.

---

## Identidade do Projeto

- **Nome:** Plugin Licitacoes Adv-OS
- **Slug:** `licitacoes-adv-os`
- **Audiencia:** advogado brasileiro especialista em licitacoes e contratos administrativos, atendendo a **empresa fornecedora/licitante** (PJ que participa de licitacoes publicas, contrata com a Administracao, defende-se de sancoes e atua em PARs/TCU)
- **Versao atual:** 0.1.0 (Release v0.1 — Nucleo Operacional)
- **Plugin de referencia (engine):** `direito-medico-adv-os` (engine portado em Sprint 0)
- **Repo marketplace:** `licitacoes-adv-os-marketplace` (a criar nas FASES 2-7 do PLAYBOOK)

---

## REGRA DE OURO — DESPERSONALIZACAO ABSOLUTA (PLUGIN COMERCIAL)

Plugin comercializado via Kirvano + marketplace publico. Zero mencoes ao criador da metodologia ou dados de clientes reais (empresas fornecedoras atendidas).

**Atencao redobrada:** clientes do advogado de licitacoes sao **PJs** — segredos comerciais, propostas, planilhas de custos. NUNCA gravar dados reais no plugin distribuido.

```bash
# Antes de CADA commit
python3 audit/audit.py
```

---

## Hierarquia das 4 Camadas

```
CAMADA 1 — PROIBICOES ABSOLUTAS (PA-01 a PA-22)
CAMADA 2 — PROTOCOLOS TECNICOS (6 + P4 Cruzamento Administrativo-TCU-Judicial)
CAMADA 3 — IDENTIDADE FIRAC + estrutura padrao peca/parecer + ressalva OAB
CAMADA 4 — SKILLS OPERACIONAIS (~33 em 7 Tiers + transversais)
```

Detalhes: `.planning/HIERARQUIA-4-CAMADAS.md`, `.planning/PROIBICOES-ABSOLUTAS.md`, `.planning/PROTOCOLOS-TECNICOS.md`, `.planning/design-spec.md`, `.planning/build-plan-v0.1.md`. Deep research: `.planning/deep-research/deep-research-licitacoes.md` (153 KB, 6 queries Perplexity, 42 citacoes).

---

## Arquitetura em Uma Frase

Plugin operacional para o advogado da empresa licitante brasileira — **triagem por fase do procedimento** (fase interna -> fase externa -> habilitacao -> recurso -> contrato -> sancao -> TCU -> judicial), **~33 skills em 7 Tiers** (0-6 + transversais), com **engine portado** do `direito-medico-adv-os`, **governanca de 4 Camadas** (primazia da legislacao vigente — Lei 14.133 vs Lei 8.666 transicao + sumulas TCU + STJ), **Protocolo P4 Cruzamento Administrativo-TCU-Judicial** e **Revisao Tecnica R1-R4** sobre toda entrega.

---

## Triagem por Fase do Procedimento (decisao de arquitetura)

Diferente do medico (4D simultaneo), aqui o caso evolui em **fases sequenciais** do procedimento licitatorio. A `triagem-licitacao` identifica em que fase do procedimento o cliente esta e roteia ao Tier correto:

| Fase | Skills do Tier |
|------|----------------|
| Pre-edital (consultivo) | Tier 1 (analise de oportunidade, ETP, TR, matriz de risco) |
| Edital publicado | Tier 2 (analise de edital, deteccao de vicios, impugnacao) |
| Sessao publica/habilitacao | Tier 3 (proposta, lances, habilitacao, recurso administrativo) |
| Adjudicacao e contrato | Tier 4 (contrato administrativo, garantia, reequilibrio) |
| Inadimplemento e sancao | Tier 5 (defesa em apenamento, PAR Lei 12.846, leniencia) |
| Controle externo e judicial | Tier 6 (TCU/TCE, MS, anulatoria, cobranca, indenizacao) |

A fase fica gravada no `CASO.md`. Casos podem voltar a fases anteriores (recurso reabre fase, MS pode suspender contrato).

---

## Fronteira com plugins irmaos (sem cross-sell — PA-20)

| Tema | Este plugin (licitacoes) | Plugin irmao |
|------|--------------------------|--------------|
| Improbidade administrativa | **Skill `improbidade-licitacao-fraude`** — Lei 8.429+14.230 quando ato licitatorio fraudulento | Plugin de direito penal/administrativo amplo (futuro) quando ato sem nexo com licitacao |
| Constituicao societaria do fornecedor | Sinaliza encaminhamento | `tributario-societario-adv-os` (sociedade empresarial generica, holdings, M&A) |
| Trabalhista de empregado da contratada | Sinaliza encaminhamento | `trabalhista-adv-os` (reclamacoes de empregados da fornecedora) |
| Tributario da contratada | Sinaliza encaminhamento | `auditoria-contabil-os` (CND, Simples, Real, certidoes fiscais sob auditoria) |

Cross-sell vedado (PA-20).

---

## Padroes a Seguir

1. **Skill folder = so `SKILL.md`.**
2. **Limites Cowork:** `SKILL.md` ≤ 11000 B (margem); `description` ≤ 1024 chars.
3. **plugin.json minimal:** name, version, description, author, license.
4. **Tokens `{{...}}`** literais no disco — LLM resolve em runtime via persona.
5. **Privacidade LGPD + segredo industrial:** pasta `<cwd>/licitacoes/casos/<slug>/` gitignored; warning se pasta sincronizada. Compartimentacao rigida.
6. **Eixo Lei 14.133 vs Lei 8.666:** datar peca/parecer pelo regime aplicavel ao contrato (transicao encerrou 1º abr 2023 para novos, mas contratos antigos ainda vigem sob Lei 8.666). Skill `validador-legislacao-vigente` faz check obrigatorio.
7. **Eixo geografico:** federal (Justica Federal / TCU) vs estadual (TCE estadual) vs municipal (TCM/TCE municipal). MS contra autoridade federal -> JF; estadual -> JE; municipal -> JE.

---

## Proibicoes (resumo das 22 PAs)

1. NAO opinar sobre conveniencia administrativa (decisao discricionaria da Administracao) — plugin e JURIDICO.
2. NAO prometer resultado em peca processual.
3. Datar pelo regime aplicavel (Lei 14.133 vs Lei 8.666).
4. Selo de Validacao Legal Previa antes de qualquer estrategia.
5. Ressalva final OAB do advogado.
6. Dados sigilosos de empresa cliente (proposta, planilha, segredo industrial) NUNCA no plugin.
7. Confidencialidade processual (recurso administrativo, sigilo de proposta).
8. Independencia das esferas (administrativa != TCU != judicial).
9. NAO confundir empresa licitante (subjetiva) com Administracao (objetiva CF art. 37 §6º).
10. Cross-sell vedado entre plugins irmaos.
... (completa em `.planning/PROIBICOES-ABSOLUTAS.md`)

---

## Como Retomar Trabalho

1. **Ler `MEMORY.md`** — estado executivo, sprint ativa.
2. **Ler `.planning/build-plan-v0.1.md`** — plano de sprints.
3. **`git status` + `git log -8`** — estado real do repo.
4. **`python3 audit/audit.py`** — verificar despersonalizacao.

---

**Ultima atualizacao:** 2026-05-24 (Sprint 0 — scaffold + engine portado + deep research).
