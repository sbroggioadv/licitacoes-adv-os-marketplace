# Licitações Adv-OS

> Sistema operacional do advogado brasileiro especialista em licitações (Lei 14.133/2021) e contratos administrativos.
> Plugin Claude Code com **~33 skills** em 7 Tiers, cobrindo todo o ciclo licitatório do fornecedor/licitante.

---

## O que faz

Plugin operacional para o advogado que atende a **empresa fornecedora/licitante**:

- **Consultivo pré-edital** — análise de oportunidade, ETP/TR/projeto básico/matriz de risco, calendário licitatório.
- **Edital e impugnação** — detecção de vícios típicos (top 15), impugnação ao edital, pedido de esclarecimento, planejamento da proposta.
- **Sessão e habilitação** — proposta exequível (limite 70%), habilitação documental, recurso administrativo, contrarrazões.
- **Contrato administrativo** — gestão, reequilíbrio econômico-financeiro, aditivos, rescisão.
- **Sanção e PAR** — defesa em apenamento (art. 156 Lei 14.133), PAR Lei 12.846/2013, acordo de leniência, Programa de Integridade.
- **Controle externo e judicial** — representação TCU/TCE, MS, ação anulatória, ação de cobrança, ação de ressarcimento.

---

## Cobertura técnica (v0.1 — Núcleo Operacional)

### ~33 skills em 7 Tiers + transversais

| Tier | Skills | Foco |
|------|--------|------|
| 0 — Núcleo & Governança | 3 | Orquestração + Selo de Validação Legal + Onboarding |
| 1 — Fase interna (consultivo pré-edital) | 4 | Análise de oportunidade, ETP/TR, matriz de risco, calendário |
| 2 — Edital + impugnação | 5 | Análise de edital, detecção de vícios, impugnação, esclarecimento, proposta |
| 3 — Sessão + habilitação + recurso | 5 | Proposta exequível, habilitação, recurso, contrarrazões |
| 4 — Contrato administrativo | 5 | Contrato, reequilíbrio, aditivo, rescisão, cronograma |
| 5 — Sanção + PAR + leniência | 4 | Defesa em apenamento, PAR Lei 12.846, leniência, compliance |
| 6 — Controle externo + judicial | 4 | TCU/TCE, MS, anulatória, cobrança |
| Transversais | 3 | Revisão R1-R4, estilo de entrega, memória de caso (LGPD) |

### Commands diretos

`/start-licitacoes` · `/licitacoes-master` · `/caso-licitacao` · `/triagem` · `/edital` · `/impugnacao` · `/recurso` · `/contrato` · `/sancao` · `/judicial` · `/revisao-final` · `/status-licitacoes`

### 4 hooks automáticos

SessionStart (persona) · UserPromptSubmit (detecta demanda licitatória e injeta protocolo) · PostToolUse (evolui memória de caso) · PreCompact (snapshot)

---

## Legislação coberta (atualizada 2024-2026)

- **Constituição:** art. 22 XXVII, 37 caput e XXI, 173, 175, 195 §3º
- **Lei 14.133/2021** (Nova Lei de Licitações) — integral
- **Lei 8.666/93** — transição (contratos antigos ainda vigentes)
- **Lei 10.520/2002** (Pregão), **Lei 12.462/2011** (RDC), **Lei 11.079/2004** (PPPs), **Lei 8.987/1995** (Concessões), **Lei 13.303/2016** (Estatais)
- **Lei 12.846/2013** (Anticorrupção) + **Decreto 11.129/2022** (Programa de Integridade)
- **Lei 8.429/1992** + **Lei 14.230/2021** (Reforma da Improbidade)
- **Lei 12.527/2011** (LAI), **Lei 13.140/2015** (Mediação), **Lei 9.307/1996** (Arbitragem)
- **Decretos:** 10.024/2019 (Pregão eletrônico), 11.246/2022 (Regulamentação Lei 14.133)
- **IN SEGES/MGI:** 65/2021, 67/2021, 73/2022, 81/2022, 89/2023
- **Súmulas TCU:** 222, 247, 248, 251, 263, 269, 272, 274, 275, 277, 287
- **Súmulas STJ:** 333, 510, 467, 562
- **Súmula STF:** 473 (autotutela administrativa)

---

## Governança técnica (4 Camadas)

```
Camada 1 — 22 PROIBIÇÕES ABSOLUTAS (invioláveis)
Camada 2 — 6 PROTOCOLOS TÉCNICOS (Vigência, Integridade, Memória, Cruzamento Adm-TCU-Judicial, Localização, Revisão R1-R4)
Camada 3 — IDENTIDADE FIRAC + estrutura padrão peça/parecer + ressalva OAB
Camada 4 — ~33 SKILLS OPERACIONAIS
```

**Revisão Técnica R1-R4** sobre toda entrega: escopo · técnica jurídica · conformidade · clareza.

---

## Como instalar (Claude Cowork)

1. Abra **Claude Cowork** → **Settings** → **Plugins**
2. Aba **Pessoal** → clique em **+ Uploads locais**
3. Cole a URL do marketplace recebida na sua compra
4. Clique em **Sincronizar**
5. Em "Pessoal → Uploads locais", clique em **Instalar** no plugin `licitacoes-adv-os`
6. Rode `/start-licitacoes` no Claude Cowork para configurar sua persona (advogado, OAB, cidade, área de foco, tom de voz)

---

## Privacidade (LGPD + Segredo Comercial)

- Propostas, planilhas de custos, segredos comerciais da empresa cliente **NUNCA** são gravados no plugin.
- Casos vivem em `<seu-workspace>/licitacoes/casos/<slug>/` — pasta gitignored por default.
- Compartimentação por cliente (PA-22).
- Warning automático se pasta de workspace estiver sincronizada (Dropbox/iCloud/OneDrive).

---

## Licença

MIT. Ver `LICENSE`.

---

**Versão:** 0.1.0 · **Autor:** IA Combativa
