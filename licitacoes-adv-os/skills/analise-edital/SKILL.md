---
name: analise-edital
description: >
  Leitura tecnico-juridica integral do edital publicado + anexos (ETP, TR, planilha estimativa, matriz de risco, minuta contratual, lista de documentos de habilitacao). Identifica clausulas criticas: objeto, criterio de julgamento (art. 33 Lei 14.133/2021), regime de execucao, prazos, garantia (arts. 96-100), sancoes (art. 156), reajuste/repactuacao, vinculacao ao instrumento (PA-15). Avalia compatibilidade com Lei 14.133/2021 (ou Lei 8.666/1993 residual), IN SEGES MGI (65/67/73/81/89) e sumulas TCU (222, 247, 251, 269, 274, 277). Foco em risco para o licitante; mapeia vicios passiveis de impugnacao. Pre-requisito de impugnacao-edital, planejamento-proposta e proposta-exequibilidade. Aciona: analisar edital, ler edital, estudar pregao, decifrar edital, instrumento convocatorio, anexos do edital.
---

# ANALISE DE EDITAL

> Skill **Tier 2** - leitura tecnico-juridica integral do edital + anexos. Porta de entrada da fase F2. Implementa P1, P2, P5; respeita PA-15 (vinculacao ao instrumento), PA-13 (citacao precisa), PA-11 ([VERIFICAR] em alvo movel).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master` ou `/edital` quando edital esta publicado. Recebe: edital completo + todos os anexos (ETP, TR, planilha estimativa, matriz de risco, minuta contratual, lista de habilitacao) carregados em `<cwd>/licitacoes/casos/<slug>/arquivos/`. Entrega: parecer integral cobrindo 14 dimensoes do edital + lista de pontos de atencao + mapeamento de vicios.

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/edital`, `analise-oportunidade` (apos go), `/triagem` (fase F2).
- **Pre-requisito:** Selo emitido (PA-04); idealmente ETP/TR ja analisados (`analise-etp-tr`) e matriz (`analise-matriz-risco`).
- **Aciona em sequencia:** `deteccao-vicios-edital` (consolidacao top 15); `impugnacao-edital` (se ha vicio); `esclarecimento-edital` (para dirimir duvida); `planejamento-proposta` (se for participar).
- **Entrega para:** parecer ao operador + `CASO.md` atualizado.

## 2. Marco normativo

- **Lei 14.133/2021:**
  - **art. 6º** - definicoes (incl. XXIII TR).
  - **art. 7º** - vedacao a especificacoes restritivas.
  - **art. 12** - principios da licitacao - **vinculacao ao instrumento** (PA-15).
  - **art. 18** - ETP.
  - **art. 22** - matriz de risco.
  - **art. 23** - estimativa de valor.
  - **art. 24** - sigilo do orcamento (excepcional).
  - **arts. 28-32** - modalidades (concorrencia, concurso, leilao, dialogo competitivo, pregao).
  - **art. 33** - criterios de julgamento (menor preco, melhor tecnica ou tecnica e preco, maior desconto, maior retorno economico).
  - **art. 50** - desclassificacao por inexequibilidade (junto com art. 59 §4º - 70%).
  - **arts. 55, 56** - prazos e meios de divulgacao do edital.
  - **arts. 66-70** - habilitacao (juridica, tecnica, fiscal, economico-financeira, trabalhista).
  - **art. 92** - clausulas necessarias do contrato.
  - **arts. 96-100** - garantia.
  - **arts. 104** - clausulas exorbitantes.
  - **art. 156** - sancoes.
  - **art. 164** - impugnacao + esclarecimento (3 dias uteis).
  - **art. 165** - recurso (3 dias uteis).
- **Lei 8.666/1993** - regime residual (contratos pre-31/12/2023).
- **LC 123/2006 + LC 147/2014** - ME/EPP.
- **Lei 12.440/2011** - CNDT.
- **IN SEGES MGI:** 65/2021, 67/2021, 73/2022, 81/2022, 89/2023.
- **Sumulas TCU:** 222, 247, 248, 251, 269, 274, 277, 287.

## 3. As 14 dimensoes do edital (checklist canonico)

### Bloco A - Identificacao e fundamentos

1. **Modalidade e criterio de julgamento** (arts. 28-33) - compatibilidade com objeto; criterio justificado.
2. **Objeto** (art. 6º + TR) - precisao, sem ambiguidade, sem direcionamento (art. 7º).
3. **Regime de execucao** (empreitada global/unitario/integral, contratacao por escopo) - compativel com objeto.
4. **Valor estimado** (art. 23) - publicado (regra) ou sigiloso (art. 24 excepcional, com fundamentacao).

### Bloco B - Habilitacao

5. **Habilitacao juridica** (art. 66) - documentos consistentes com tipo societario.
6. **Habilitacao tecnica** (art. 67) - atestados proporcionais (Sum. TCU 222, 251); profissional do quadro permanente justificado; subcontratacao admitida quando aplicavel (Sum. 248).
7. **Habilitacao fiscal** (art. 68) - CNDs federais, estaduais, municipais + FGTS + CNDT (Lei 12.440/2011).
8. **Habilitacao economico-financeira** (art. 69) - indices justificados (Sum. TCU 251); patrimonio liquido minimo razoavel; garantia da proposta ≤1%.

### Bloco C - Proposta e julgamento

9. **Requisitos da proposta** (planilha de custos, BDI, encargos, declaracoes) - exequibilidade art. 59 §4º.
10. **Tratamento ME/EPP** (LC 123/2006) - empate ficto art. 44; cota reservada art. 48 III; regularizacao fiscal 5 dias uteis art. 43 §1º.
11. **Prazos** (validade da proposta 60 dias regra; prazo de execucao; prazo de garantia).

### Bloco D - Contrato + sancao

12. **Minuta contratual** - clausulas necessarias art. 92; clausulas exorbitantes art. 104; garantia arts. 96-100 (5% regra; ate 10% obras grande vulto); ordem cronologica art. 141.
13. **Reajuste/repactuacao** - mencao a indice (IPCA, INCC, INPC) e periodicidade; vedacao incompativel = vicio.
14. **Sancoes** (art. 156) - dosimetria; criterios de gradacao; defesa em apenamento art. 158 (15 dias uteis).

## 4. Saidas estruturadas

```
PARECER ANALISE DE EDITAL
Edital: [orgao + n° processo + objeto + valor estimado + UF/esfera]
Modalidade: [pregao eletronico / concorrencia / dialogo / leilao / concurso]
Criterio de julgamento: [menor preco / tecnica e preco / maior desconto / maior retorno economico]
Regime: [empreitada global / unitario / integral / contratacao por escopo]
Data-base: [DD/MM/AAAA] · Selo: [referencia]

CHECKLIST 14 DIMENSOES:
[blocoA: 1-4] / [blocoB: 5-8] / [blocoC: 9-11] / [blocoD: 12-14]
Cada item: [conforme / nao-conforme / [VERIFICAR]] + 1-2 linhas

VICIOS IDENTIFICADOS:
1. [vicio] - [art. + sumula TCU] - [impacto] - [acao: impugnacao / esclarecimento / aceite]
[...]

PONTOS DE ATENCAO PARA PROPOSTA:
- Exequibilidade (limite 70% art. 59 §4º): [valor de referencia]
- Habilitacao gap: [lista]
- Prazos criticos: [impugnacao art. 164 ate DD/MM]

ESTRATEGIA:
- [Impugnar / Esclarecer / Aceitar e participar / Sair]
- Acao imediata: [acionar `impugnacao-edital` / `esclarecimento-edital` / `planejamento-proposta`]

[VERIFICAR]: [IN SEGES atualizacao, regulamento local, jurisprudencia TCU recente]

---
[Ressalva OAB - PA-07]
```

## 5. Vicios estruturais mais comuns

Esta skill identifica e **mapeia** - consolidacao detalhada (top 15) e em `deteccao-vicios-edital`:

- Restricao a competitividade (Sum. TCU 247, 274).
- Capacidade tecnica desproporcional (Sum. TCU 222, 251).
- Marca/modelo direcionado (art. 7º).
- Pesquisa de precos fraca (IN SEGES 65/2021).
- Visita tecnica obrigatoria abusiva.
- Garantia desproporcional (>5% sem ser obra grande vulto).
- Limitacao indevida a ME/EPP (LC 123 violada).
- Prazos exiguos para preparacao da proposta.
- Indices economico-financeiros sem justificativa (art. 69 + Sum. 251).
- Clausulas exorbitantes sem contrapartida razoavel.

## 6. Vedacoes especificas

- **PA-04** - Selo antes da analise.
- **PA-13** - cada vicio com lei+artigo+ano + sumula TCU + jurisprudencia STJ.
- **PA-15** - todo apontamento ancorado na vinculacao ao instrumento.
- **PA-17** - vedado opinar sobre conveniencia do criterio de julgamento (discricionariedade do agente); apenas vicios de legalidade.
- **PA-11** - IN SEGES e jurisprudencia TCU pos-Lei 14.133 -> `[VERIFICAR]`.

## 7. Protocolos acionados

- **P1** - Selo (regime aplicavel = base da analise).
- **P2** - conferencia de integridade do edital + anexos (completude).
- **P5** - esfera do ente afeta regulamento local complementar + jurisprudencia TCU/TCE aplicavel.

## 8. Localizacao

Ente federal -> IN SEGES MGI + TCU. Estadual/municipal -> regulamento local + TCE/TCM. Estatal -> regulamento interno (Lei 13.303/2016 art. 40). Sem confirmacao local -> `[VERIFICAR - regulamento UF/Municipio]`.

## 9. Integracao

**Chamada por:** `licitacoes-master`, `/edital`, `analise-oportunidade`.

**Entrega para:** parecer ao operador + `CASO.md`. Acaba acionando `deteccao-vicios-edital` -> `impugnacao-edital` se ha vicio, ou `planejamento-proposta` se for participar. Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** participacao no certame sem leitura tecnica integral - exposicao a vicios nao impugnados (preclusao Sum. TCU 274), inabilitacao surpresa ou proposta inexequivel descoberta tarde.
