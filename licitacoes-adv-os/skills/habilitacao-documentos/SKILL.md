---
name: habilitacao-documentos
description: >
  Conferencia documental de habilitacao - 4 categorias da Lei 14.133/2021: juridica (art. 66), tecnica (art. 67), economico-financeira (art. 69), fiscal/trabalhista (art. 68 + CNDT Lei 12.440/2011). SICAF, PNCP, CADIN (art. 70). Regularizacao de pendencias (art. 64 - diligencia saneadora). Saneamento de vicios formais sob Sum. TCU 269 (formalismo moderado - falha sanavel). Estrategia em caso de inabilitacao (intencao de recurso preservada na sessao art. 165; razoes em 3 dias uteis). Fronteira com plugin tributario-societario sem citar (PA-18) - regularidade fiscal e conferencia documental aqui, nao apuracao tributaria. Aciona: habilitacao, documentos de habilitacao, art. 66, 67, 68, 69, 70, SICAF, PNCP, CNDT, inabilitacao, saneamento.
---

# HABILITACAO E DOCUMENTOS

> Skill **Tier 3** - conferencia documental da habilitacao da PJ-cliente nas 4 categorias da Lei 14.133/2021. Preparacao previa para evitar inabilitacao surpresa. Implementa P1, P2, P5; respeita PA-15 (vinculacao), PA-18 (fronteira sem cross-sell).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `planejamento-proposta`, `analise-edital` (apos definicao de participar). Tambem acionada **reativamente** se a PJ-cliente foi inabilitada e precisa recorrer. Recebe: edital + lista de documentos exigidos + situacao documental atual da PJ-cliente (PA-09 sigilo).

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `planejamento-proposta`, `analise-edital`, `recurso-administrativo` (apos inabilitacao).
- **Pre-requisito:** Selo (PA-04); edital com lista clara de documentos (`analise-edital`).
- **Aciona em sequencia:** `recurso-administrativo` se ha inabilitacao injusta; `tratamento-me-epp` em paralelo se ME/EPP; `contrarrazoes-recurso` se concorrente recorre da habilitacao do cliente.
- **Entrega para:** checklist documental + plano de saneamento + roteiro para defesa em recurso.

## 2. Marco normativo

- **Lei 14.133/2021:**
  - **art. 64** - diligencia saneadora (saneamento documental e admissivel).
  - **art. 66** - habilitacao **juridica** (registro empresarial, ato constitutivo, eleicao de administradores, etc.).
  - **art. 67** - habilitacao **tecnica** (registro profissional, atestados de capacidade tecnico-operacional e tecnico-profissional, certidoes profissionais, etc.).
  - **art. 68** - habilitacao **fiscal, social e trabalhista** (CNDs federais, estaduais, municipais + FGTS + CNDT).
  - **art. 69** - habilitacao **economico-financeira** (balanco patrimonial, indices, patrimonio liquido, garantia de proposta ≤1%).
  - **art. 70** - **SICAF / PNCP** (sistemas de registro cadastral - substituem documentos quando atualizado).
  - **art. 165** - recurso (3 dias uteis intencao + razoes).
- **Lei 12.440/2011** - **CNDT** (Certidao Negativa de Debitos Trabalhistas).
- **CADIN federal** - art. 6º Lei 10.522/2002.
- **LC 123/2006 art. 43 §1º** - regularizacao fiscal de ME/EPP em 5 dias uteis prorrogaveis (apos declaracao de vencedora).
- **Sumulas TCU:**
  - **Sum. 269** - formalismo moderado (falha sanavel; saneamento admitido).
  - **Sum. 222** - capacidade tecnico-operacional razoavel.
  - **Sum. 251** - clausulas tecnicas justificadas.

## 3. Checklist documental - 4 categorias

### Categoria 1 - Habilitacao juridica (art. 66)

- Registro empresarial (Junta Comercial) - certidao simplificada vigente.
- Ato constitutivo/estatuto consolidado + ultima alteracao.
- Inscricao no CNPJ.
- Eleicao de administradores - ata vigente.
- Procuracao especifica para o certame (se aplicavel).
- Documentos do representante legal (RG + CPF + procuracao OAB).

### Categoria 2 - Habilitacao tecnica (art. 67)

- Registro profissional (CREA, CRC, etc. - conforme objeto).
- Atestados de capacidade tecnico-operacional (PJ) - **proporcionais** (Sum. TCU 222, 251).
- Atestados de capacidade tecnico-profissional (PF dos responsaveis tecnicos).
- Certificados profissionais (responsavel tecnico inscrito no Conselho).
- Equipamentos disponiveis (declaracao + atestado de propriedade/leasing).
- Vinculo do responsavel tecnico (quadro permanente / contrato com profissional / vinculo do consorciado).

### Categoria 3 - Habilitacao economico-financeira (art. 69)

- **Balanco patrimonial** do ultimo exercicio social - registrado.
- **Indices economico-financeiros** (LG, LC, SG) conforme exigencia do edital (Sum. TCU 251 - justificados).
- **Patrimonio liquido minimo** - razoavel (jurisprudencia TCU consolidada: ≤ 10% do valor estimado).
- **Garantia da proposta** (ate 1% do valor estimado - art. 58).
- Certidao negativa de falencia/recuperacao judicial (Lei 11.101/2005).

### Categoria 4 - Habilitacao fiscal, social e trabalhista (art. 68)

- **CND federal** (Receita Federal + PGFN).
- **CND estadual** (Fazenda estadual de sede).
- **CND municipal** (mobiliario + imobiliario, se sede no municipio).
- **CRF FGTS** (Caixa).
- **CNDT** (TST - Lei 12.440/2011).
- **CADIN** (consulta federal).
- **SICAF / PNCP** (art. 70) - registro atualizado substitui documentos conforme regulamento.

## 4. Diligencia saneadora (art. 64) - estrategia

Sum. TCU **269** - formalismo moderado: vicio formal sanavel pode ser corrigido sem desclassificacao automatica. Estrategia:

1. **Preventivamente:** conferir todos os documentos antes da sessao; suprir falhas antes que aparecam.
2. **Reativamente** (apos diligencia ou inabilitacao): responder com saneamento + fundamentar no art. 64 + Sum. 269.
3. **Documentar a tentativa de saneamento** - preserva-se prova para futura impugnacao/recurso.

## 5. Inabilitacao - estrategia de defesa

```
SE inabilitacao -> intencao de recurso NA SESSAO (motivada - art. 165 §1º)
  -> razoes em 3 dias uteis (art. 165 §3º) - acionar `recurso-administrativo`
  -> peca articula:
    - vinculacao ao edital (PA-15 - documento exigido nao cumpre principio da proporcionalidade)
    - Sum. TCU 269 - falha sanavel se aplicavel
    - Sum. TCU 222 - exigencia razoavel
    - Art. 64 - diligencia saneadora omitida ou indevidamente nao oferecida
    - Eventual vicio do edital nao impugnado tempestivamente (preclusao Sum. 274) - cuidado
```

## 6. ME/EPP - regularizacao fiscal especifica

LC 123/2006 art. 43 §1º + LC 147/2014:
- ME/EPP que apresentar **alguma restricao** em regularidade fiscal e trabalhista nao e inabilitada imediatamente.
- **Prazo de 5 dias uteis prorrogaveis** apos declaracao de vencedora para regularizar.
- Estrategia: nao usar como descuido; usar quando ha pendencia objetiva e regularizavel. Articular com `tratamento-me-epp` (Tier 3).

## 7. Output - Checklist + plano

```
CHECKLIST DE HABILITACAO - CASO [slug]
Edital: [orgao + n° + objeto]
Data-base: [DD/MM/AAAA] · Selo: [referencia]

CATEGORIA 1 - JURIDICA (art. 66 Lei 14.133):
[ ] Registro empresarial - [conforme / pendencia: X]
[continuar 6 itens]

CATEGORIA 2 - TECNICA (art. 67):
[ ] Atestado de capacidade operacional - [conforme / pendencia]
[continuar]

CATEGORIA 3 - ECONOMICO-FINANCEIRA (art. 69):
[ ] Balanco patrimonial - [conforme]
[continuar]

CATEGORIA 4 - FISCAL/TRABALHISTA (art. 68):
[ ] CND federal - [conforme / vencida em DD/MM]
[continuar]

PENDENCIAS IDENTIFICADAS:
1. [pendencia] - acao: [renovar / sanear / regularizar] - prazo: [DD/MM]
[lista priorizada]

ESTRATEGIA:
- Sanar [N] pendencias ate [data] (antes da sessao)
- Se inabilitacao -> intencao de recurso NA SESSAO + razoes 3 dias uteis (`recurso-administrativo`)
- Se ME/EPP -> regularizacao 5 dias uteis LC 123 art. 43 §1º (`tratamento-me-epp`)

ATENCAO PA-18:
- Pendencia fiscal contenciosa (auto de infracao, parcelamento em discussao) -> "encaminhar
  a especialista em direito tributario/auditoria contabil" sem citar produto irmao.

[VERIFICAR]: [regulamento UF/Municipio; jurisprudencia TCU recente]

---
[Ressalva OAB - PA-07]
```

## 8. Vedacoes especificas

- **PA-04** Selo. **PA-09** sigilo de documentos da PJ.
- **PA-15** argumentacao ancorada na vinculacao ao edital + arts. 66-70.
- **PA-17** vedado opinar sobre conveniencia do agente em aceitar saneamento (discricionariedade); apenas vicio de legalidade.
- **PA-18** - regularidade fiscal contenciosa: documental aqui; apuratorio = "encaminhar a especialista" sem citar produto.

## 9. Protocolos acionados

- **P1** Selo. **P2** integridade documental. **P5** esfera do ente afeta CNDs aplicaveis.

## 10. Localizacao

CNDs municipais conforme municipio sede da PJ + municipio do orgao licitante (raro). Cada UF tem regramento proprio de CND estadual. `[VERIFICAR - calendario de CND]` quando emissao automatica nao confirmada.

## 11. Integracao

**Chamada por:** `licitacoes-master`, `planejamento-proposta`, `analise-edital`, `recurso-administrativo`.

**Entrega para:** checklist + plano + `CASO.md`. Se inabilitacao -> `recurso-administrativo` + `proposta-exequibilidade` (se pertinente). ME/EPP -> `tratamento-me-epp`. Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** inabilitacao por documento faltante/vencido; perda do certame por formalidade evitavel; ausencia de defesa estruturada em recurso.
