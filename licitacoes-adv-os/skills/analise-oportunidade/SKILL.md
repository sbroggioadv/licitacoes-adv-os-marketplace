---
name: analise-oportunidade
description: >
  Diligencia previa de participacao em certame - parecer go/no-go fundamentado para a empresa licitante. Avalia 8 eixos: (1) compatibilidade objeto x capacidade tecnica (atestados Sum. TCU 222, 251); (2) exequibilidade do preco-teto (art. 59 §4º Lei 14.133/2021 - 70% do referencial); (3) viabilidade economico-financeira (BDI, encargos, margem); (4) regularidade fiscal/trabalhista atual (arts. 68 + CNDT - Lei 12.440/2011); (5) capacidade economica (art. 69 - indices); (6) prazos e cronograma; (7) clausulas exorbitantes e matriz de risco (arts. 22, 104 Lei 14.133); (8) requisitos restritivos como vicios oportunos (PA-15 vinculacao ao edital). Sinaliza fronteira com plugin tributario-societario/contabil sem citar (PA-18). Aciona: participar do pregao, vale a pena, go/no-go, analise de viabilidade, capacidade tecnica, exequibilidade, margem de contribuicao, BDI.
---

# ANALISE DE OPORTUNIDADE

> Skill **Tier 1** - porta de entrada **consultiva** pré-edital. Parecer go/no-go fundamentado para a empresa licitante decidir participar ou nao do certame. Implementa P1, P2, P5; respeita PA-15 (vinculacao ao edital), PA-09 (sigilo comercial), PA-18 (sem cross-sell).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master` quando o operador disser "vale a pena participar?", "analisar viabilidade do edital", "go/no-go", "compensar participar deste pregao", "capacidade tecnica suficiente", "margem de contribuicao", "preco-teto exequivel". Recebe: edital + anexos (ETP, TR, planilha estimativa, matriz de risco, minuta) carregados em `<cwd>/licitacoes/casos/<slug>/arquivos/`, perfil da PJ-cliente (capacidade tecnica, capacidade economica, regularidade) - dados sigilosos (PA-09).

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/triagem` (quando triagem indica fase F1).
- **Pre-requisito:** Selo emitido por `validador-legislacao-vigente` (PA-04).
- **Aciona em sequencia:** `analise-edital` (Tier 2) se for go; `analise-etp-tr` + `analise-matriz-risco` em paralelo se houver duvida tecnica; `calendario-licitatorio` para travar prazos da fase externa.
- **Entrega para:** parecer go/no-go ao operador, com tabela de pontos pro/contra, riscos e recomendacao.

## 2. Marco normativo

- **Lei 14.133/2021:** art. 18 (ETP), art. 6º XXIII (TR), art. 22 (matriz de risco), art. 59 §4º (exequibilidade - 70%), arts. 66-70 (habilitacao), art. 96 (garantia), arts. 89, 104 (clausulas), art. 7º (vedacao a especificacoes restritivas), art. 12 (vinculacao).
- **Lei 8.666/1993:** regime residual para contratos pre-31/12/2023.
- **LC 123/2006 + LC 147/2014:** ME/EPP (empate ficto art. 44; cota reservada art. 48 III).
- **Lei 12.440/2011:** CNDT como requisito de habilitacao trabalhista.
- **CC arts. 421-422:** boa-fé objetiva como parametro de risco contratual.
- **Sumulas TCU:** 222 (capacidade tecnica razoavel); 247 (parcelamento); 251 (clausulas tecnicas justificadas); 269 (formalismo moderado); 274 (preclusao).
- **Jurisprudencia STJ:** habilitacao fiscal e tecnica (REsp paradigmas variaveis - `[VERIFICAR]`).

## 3. Os 8 eixos de avaliacao

### Eixo 1 - Compatibilidade objeto x capacidade tecnica

- Atestados de capacidade tecnica exigidos vs atestados disponiveis (Sum. TCU 222 - razoabilidade; 251 - tecnicas justificadas).
- Quantitativos minimos (Sum. TCU 247 - parcelamento; vedada exigencia desproporcional).
- Profissionais do quadro permanente exigidos vs equipe atual.
- Subcontratacao prevista (Sum. TCU 248 - quando expressamente admitida).
- **Output:** match (sim/parcial/nao) + lista de gap + risco de desclassificacao na habilitacao.

### Eixo 2 - Exequibilidade do preco-teto

- Valor estimado vs custo realista da PJ-cliente.
- Margem entre custo + lucro razoavel e preco-teto.
- **Limite legal de exequibilidade (art. 59 §4º Lei 14.133):** proposta inferior a **70% do valor de referencia ou da media das propostas validas** presume-se inexequivel. Mesmo se PJ-cliente cobrir custo, abaixo do limite ha onus de comprovar viabilidade (diligencia art. 64).
- **Output:** preco-teto exequivel (sim/marginal/nao) + cenarios de margem (alto/medio/baixo).

### Eixo 3 - Viabilidade economico-financeira

- BDI proprio (encargos sociais, tributos, lucro, riscos contingentes, despesas indiretas).
- Capital de giro disponivel x prazo medio de pagamento (art. 141 Lei 14.133 - ordem cronologica).
- Garantia exigida (5% regra; ate 10% obras grande vulto - arts. 96-100).
- **Output:** viabilidade financeira (sim/marginal/nao) + impacto no fluxo.

### Eixo 4 - Regularidade fiscal/trabalhista atual

- CNDs federais, estaduais, municipais (art. 68); CNDT (Lei 12.440/2011); FGTS; SICAF/PNCP/CADIN (art. 70).
- **Documental, nao apuratorio.** Fronteira (PA-18): se ha auto de infracao em aberto ou tributario contencioso, sinalizar "encaminhar a especialista em direito tributario/auditoria contabil" - sem citar produto.
- **Output:** regular (sim/sanavel/nao).

### Eixo 5 - Capacidade economica

- Indices economico-financeiros (art. 69 Lei 14.133): liquidez corrente, geral, solvencia, endividamento - **somente se justificados pelo edital** (Sum. TCU 251).
- Patrimonio liquido minimo (≤ 10% do valor estimado - jurisprudencia TCU consolidada).
- Garantia da proposta (ate 1% - art. 58).
- **Output:** atende (sim/marginal/nao).

### Eixo 6 - Prazos e cronograma

- Prazo de execucao vs capacidade operacional da PJ.
- Prazo de validade da proposta (60 dias regra).
- Prazo de garantia.
- Compatibilidade com outros certames simultaneos da PJ (PA-22 - compartimentacao por certame, mas analise agregada de capacidade operacional).
- **Output:** factivel (sim/marginal/nao).

### Eixo 7 - Clausulas exorbitantes e matriz de risco

- Clausulas exorbitantes (art. 104 Lei 14.133): modificacao unilateral, rescisao unilateral, fiscalizacao, sancoes, ocupacao de bens.
- Matriz de alocacao de riscos (art. 22): riscos retidos pela Administracao vs transferidos a contratada.
- Garantia desproporcional (>5% sem justificativa - vicio).
- Clausula vedando reajuste/repactuacao - vicio (impacto futuro no reequilibrio).
- **Output:** riscos contratuais (baixo/medio/alto) + clausulas criticas listadas.

### Eixo 8 - Vicios oportunos no edital (vinculacao - PA-15)

- Identificacao de vicios passiveis de **impugnacao** (art. 164 Lei 14.133 - 3 dias uteis): marca/modelo direcionado (art. 7º), capacidade tecnica desproporcional (Sum. TCU 222), atestados especificos demais, visita tecnica obrigatoria abusiva, prazo exiguo, garantia desproporcional.
- Estrategia: impugnar antes da sessao publica × participar e recorrer × sair do certame.
- **Output:** lista de vicios + recomendacao de impugnacao (sim/nao) + roteiro para `impugnacao-edital`.

## 4. Output - Parecer go/no-go (formato canonico)

```
PARECER DE OPORTUNIDADE
Edital: [orgao + n° processo + objeto + valor estimado + UF/esfera]
Data-base: [DD/MM/AAAA] · Selo: [referencia]

EIXO 1 - Compatibilidade tecnica: [match / parcial / nao] - [3 linhas]
EIXO 2 - Exequibilidade do preco-teto: [sim / marginal / nao] - [linhas]
EIXO 3 - Viabilidade economico-financeira: [sim / marginal / nao]
EIXO 4 - Regularidade atual: [regular / sanavel / nao]
EIXO 5 - Capacidade economica (indices): [atende / marginal / nao]
EIXO 6 - Prazos e cronograma: [factivel / marginal / nao]
EIXO 7 - Clausulas exorbitantes e riscos: [baixo / medio / alto]
EIXO 8 - Vicios oportunos (impugnacao): [N vicios identificados]

PROBABILIDADE TECNICA DE ADJUDICACAO (PA-02 - sem promessa):
- Baixa / Media / Alta - **fundamentar com numeros, nao prometer**

RECOMENDACAO: [PARTICIPAR / PARTICIPAR COM RESSALVA / IMPUGNAR ANTES / NAO PARTICIPAR]
- Justificativa: [vinculacao a eixos]
- Acoes propostas: [lista]
- Pontos de atencao: [3-5]

PROXIMOS PASSOS:
- [ ] Selo confirmado
- [ ] Se IMPUGNAR: acionar `impugnacao-edital` no prazo art. 164 Lei 14.133
- [ ] Se PARTICIPAR: acionar `planejamento-proposta`, `analise-matriz-risco`, `habilitacao-documentos`
- [ ] `calendario-licitatorio` atualizado com prazos do certame

[VERIFICAR]: [pontos em alvo movel - IN SEGES, regulamento local, sumula TCU em revisao]

---
[Ressalva OAB - PA-07]
```

## 5. Vedacoes especificas

- **PA-02** - vedada promessa de adjudicacao. Probabilidade tecnica fundamentada em numeros.
- **PA-09 + PA-22** - dados sigilosos da PJ (proposta, custos, segredo industrial) ficam em `<cwd>/licitacoes/casos/<slug>/arquivos/` (gitignored); jamais no estado distribuido.
- **PA-15** - eixo 8 ancorado na vinculacao ao edital (vicios sao desvios do principio).
- **PA-17** - vedado opinar sobre discricionariedade do agente (criterio de julgamento, parcelamento) - so vicio de legalidade.
- **PA-18** - regularidade fiscal/tributaria contenciosa = "encaminhar a especialista" sem citar produto irmao.
- **PA-04** - Selo emitido antes do parecer.

## 6. Protocolos acionados

- **P1** - exigir Selo via `validador-legislacao-vigente` antes de produzir o parecer.
- **P2** - conferencia de integridade do edital + anexos (completude, marca direcionada, criterio de julgamento, prazo de validade).
- **P5** - esfera do ente (federal/estadual/municipal/estatal) define TCU/TCE/TCM aplicavel (relevante quando ha decisao TCU paradigma do orgao).

## 7. Localizacao

A esfera do ente licitante (informada pelo `licitacoes-master`/triagem) afeta o parecer: ente federal -> jurisprudencia TCU paradigma; estadual -> TCE estadual + jurisprudencia STJ; municipal -> TCE/TCM. Regulamento local complementar Lei 14.133 (SP, RJ, MG, BH, Recife) -> `[VERIFICAR - regulamento UF/Municipio]` (PA-11) quando regra nao confirmada.

## 8. Integracao

**Chamada por:** `licitacoes-master`, `/triagem`. **Pre-requisito:** Selo P1.

**Entrega para:** operador (parecer go/no-go) + `CASO.md` atualizado. Se go -> aciona `planejamento-proposta`, `analise-matriz-risco`, `habilitacao-documentos`. Se impugnar -> aciona `deteccao-vicios-edital` + `impugnacao-edital`. Entrega final passa por `revisao-final-licitacoes` (R1-R4).

**Sem esta skill:** decisao de participacao sem fundamentacao tecnica - risco operacional elevado para a empresa licitante (proposta inexequivel, capacidade tecnica insuficiente, garantia desproporcional descoberta tarde).
