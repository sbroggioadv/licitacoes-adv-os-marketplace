---
name: deteccao-vicios-edital
description: >
  Catalogo dos 15 vicios mais comuns em editais - cada um com base legal + sumula TCU + estrategia: (1) restricao a competitividade Sum. TCU 247, 274; (2) capacidade tecnica excessiva Sum. 222, 251; (3) atestados especificos demais; (4) marca direcionada art. 7º Lei 14.133; (5) pesquisa de precos fraca IN SEGES 65/2021; (6) prazo exiguo; (7) visita tecnica obrigatoria abusiva; (8) limitacao indevida a ME/EPP - LC 123; (9) garantia desproporcional art. 96; (10) profissional do quadro permanente desnecessario; (11) reajuste/repactuacao vedados; (12) prazo de validade <60 dias; (13) sem criterio objetivo art. 33; (14) clausulas exorbitantes sem contrapartida; (15) indices economico-financeiros sem justificativa art. 69 + Sum. 251. Aciona: vicios do edital, restricao a competitividade, atestados desproporcionais, marca direcionada, garantia abusiva, indices financeiros, ME/EPP cota.
---

# DETECCAO DE VICIOS DO EDITAL

> Skill **Tier 2** - catalogo dos 15 vicios mais comuns + fundamentacao + estrategia de impugnacao. Pre-requisito de `impugnacao-edital`. Implementa P1, P2; respeita PA-15 (vinculacao), PA-13 (citacao precisa), PA-11 (alvo movel).

---

## 0. Escopo e acionamento

Acionada por `analise-edital` ou `licitacoes-master` quando ha suspeita de vicio. Recebe: edital + anexos + apontamentos preliminares (de `analise-edital`, `analise-etp-tr`, `analise-matriz-risco`). Entrega: catalogo dos vicios encontrados, com fundamentacao tripla (lei + sumula TCU + jurisprudencia) e recomendacao de impugnacao/esclarecimento/aceite.

## 1. Posicao na orquestra

- **Chamada por:** `analise-edital`, `licitacoes-master`, `analise-oportunidade`.
- **Pre-requisito:** Selo emitido (PA-04); idealmente `analise-edital` ja concluida.
- **Aciona em sequencia:** `impugnacao-edital` (peca) ou `esclarecimento-edital` (diligencia preparatoria).
- **Entrega para:** parecer + `CASO.md` + roteiro para a peca de impugnacao.

## 2. Marco normativo

- **Lei 14.133/2021:** arts. 7º (restritiva), 12 (vinculacao), 22 (matriz), 23 (estimativa), 33 (criterios), 50 §3º, 55-56 (prazos), 66-70 (habilitacao), 96 (garantia), 156 (sancao), 164-165 (impugnacao + recurso).
- **LC 123/2006 + LC 147/2014:** arts. 43-48 (ME/EPP).
- **IN SEGES 65/2021** (pesquisa de precos); **Lei 12.527/2011** (LAI).
- **Sumulas TCU:** 222, 247, 248, 251, 269, 274, 277, 287.

## 3. Catalogo dos 15 vicios

### Bloco I - Restricao a competitividade (vicios 1-3)

**Vicio 1 - Restricao a competitividade injustificada**
- **Base:** art. 12 Lei 14.133 (principio da competitividade); Sum. TCU **247** (parcelamento ampliando competitividade) e **274** (parcelamento + preclusao).
- **Detectar:** condicao que restringe inadequadamente potenciais participantes (subcontratacao vedada quando admissivel - Sum. 248; especificacao tecnica que so um fornece; nao parcelamento sem justificativa robusta).
- **Estrategia:** impugnacao com pedido de retificacao (parcelamento, abertura da subcontratacao, ajuste de especificacao).

**Vicio 2 - Capacidade tecnica desproporcional**
- **Base:** art. 67 Lei 14.133; Sum. TCU **222** (capacidade tecnico-operacional razoavel); Sum. **251** (clausulas tecnicas justificadas).
- **Detectar:** atestados com quantitativo proximo a 100% do objeto (regra: 50% e razoavel para grandes); exigencia de atestado de mesmo orgao licitante (vies); exigencia de capacidade simultanea de varios objetos.
- **Estrategia:** impugnacao com pedido de ajuste para padrao razoavel (50%-60% do objeto).

**Vicio 3 - Atestados especificos demais (objeto + quantitativo + local)**
- **Base:** art. 67 + Sum. TCU 222, 251.
- **Detectar:** combinacao restritiva (mesmo objeto + mesmo quantitativo + mesma regiao); afasta concorrencia sem justificativa.
- **Estrategia:** impugnacao + comprovacao tecnica (exemplos de fornecedores que atendem objeto sem atender combinacao).

### Bloco II - Especificacoes e referencias (vicios 4-5)

**Vicio 4 - Marca, modelo ou fornecedor direcionado**
- **Base:** **art. 7º Lei 14.133** (vedacao); art. 12 (impessoalidade).
- **Detectar:** marca/modelo expresso ou implicito (especificacao tao detalhada que so um fornecedor atende); ausencia de "ou equivalente".
- **Estrategia:** impugnacao com pedido de generalizacao + comprovacao de equivalentes no mercado.

**Vicio 5 - Pesquisa de precos fraca**
- **Base:** art. 23 Lei 14.133; **IN SEGES 65/2021** (parametros, fontes, metodos).
- **Detectar:** menos de 3 fontes; fontes nao representativas (preco unico de fornecedor); mediana fora do mercado; ausencia de justificativa para preco-teto.
- **Estrategia:** impugnacao + pedido de refazimento da pesquisa de precos.

### Bloco III - Prazos e procedimentos (vicios 6-7)

**Vicio 6 - Prazo exiguo para preparacao da proposta**
- **Base:** art. 55 Lei 14.133 (prazos minimos); arts. 28-32 (modalidades); principio da razoabilidade.
- **Detectar:** prazo entre publicacao e abertura abaixo do minimo (variavel por modalidade) ou irrazoavel para complexidade do objeto (obras de grande vulto com 20 dias - exiguo).
- **Estrategia:** impugnacao com pedido de prorrogacao.

**Vicio 7 - Visita tecnica obrigatoria sem justificativa**
- **Base:** art. 63 §2º Lei 14.133 (visita facultativa como regra); jurisprudencia TCU.
- **Detectar:** visita tecnica como pre-requisito de habilitacao sem necessidade pelo objeto (servico padronizado, fornecimento de bem comum); visita em horario unico restritivo; vies em favor de licitante local.
- **Estrategia:** impugnacao com pedido de tornar facultativa ou ampliar prazos/horarios.

### Bloco IV - Tratamento ME/EPP (vicio 8)

**Vicio 8 - Limitacao indevida a ME/EPP**
- **Base:** **LC 123/2006 art. 44** (empate ficto); **art. 48 III** (cota reservada ate 25%); **art. 43 §1º** (regularizacao fiscal 5 dias uteis); **LC 147/2014**.
- **Detectar:** ausencia de cota reservada quando obrigatoria; empate ficto vedado; regularizacao fiscal nao admitida.
- **Estrategia:** impugnacao com pedido de inclusao das clausulas obrigatorias.

### Bloco V - Habilitacao economico-financeira (vicios 9-10)

**Vicio 9 - Garantia desproporcional**
- **Base:** **arts. 96-100 Lei 14.133** (5% regra; ate 10% obras grande vulto justificadas).
- **Detectar:** garantia >5% sem ser obra de grande vulto; modalidade de garantia unica (so dinheiro - vedado, todas tres permitidas).
- **Estrategia:** impugnacao com pedido de reducao + abertura das 3 modalidades.

**Vicio 10 - Profissional do quadro permanente desnecessario**
- **Base:** art. 67 Lei 14.133; Sum. TCU 222.
- **Detectar:** exigencia de profissional do quadro permanente para servico que admite contratacao de subcontratado/temporario.
- **Estrategia:** impugnacao + alternativa de comprovacao (contrato de prestacao com profissional, declaracao de disponibilidade).

### Bloco VI - Contrato e proposta (vicios 11-13)

**Vicio 11 - Reajuste/repactuacao vedados**
- **Base:** **arts. 124-125 Lei 14.133** (reequilibrio + reajuste/repactuacao); **CF art. 37 XXI** (manutencao da equacao); IN SEGES MP 5/2017 (repactuacao mao-de-obra exclusiva).
- **Detectar:** clausula que veda reajuste, repactuacao ou revisao - nulidade por afronta a CF.
- **Estrategia:** impugnacao com pedido de retirada da vedacao + insercao de indice (IPCA, INCC, INPC).

**Vicio 12 - Prazo de validade da proposta inferior a 60 dias**
- **Base:** art. 50 §3º Lei 14.133 (60 dias regra).
- **Detectar:** prazo menor sem justificativa razoavel.
- **Estrategia:** impugnacao com pedido de adequacao.

**Vicio 13 - Ausencia de criterio objetivo de julgamento**
- **Base:** **art. 33 Lei 14.133** (criterios de julgamento); art. 12 (objetividade).
- **Detectar:** criterio impreciso ("melhor solucao"); ausencia de matriz de pontuacao em tecnica e preco; subjetivismo excessivo.
- **Estrategia:** impugnacao com pedido de matriz objetiva.

### Bloco VII - Clausulas e indices (vicios 14-15)

**Vicio 14 - Clausulas exorbitantes sem contrapartida razoavel**
- **Base:** art. 104 Lei 14.133 (clausulas exorbitantes); art. 124 §1º (reequilibrio).
- **Detectar:** modificacao unilateral sem limite (acima de 25%/50% - art. 124 I); rescisao unilateral facilitada; fiscalizacao desproporcional.
- **Estrategia:** impugnacao especifica + pedido de matriz de risco compensatoria.

**Vicio 15 - Indices economico-financeiros sem justificativa**
- **Base:** **art. 69 Lei 14.133**; **Sum. TCU 251** (clausulas tecnicas justificadas).
- **Detectar:** indices exigidos (liquidez corrente, geral, solvencia) sem fundamentacao tecnica para o objeto; patrimonio liquido minimo >10% do valor estimado (jurisprudencia TCU consolidada).
- **Estrategia:** impugnacao com pedido de reducao/justificativa.

## 4. Output - Catalogo de vicios identificados

```
CATALOGO DE VICIOS DO EDITAL
Edital: [orgao + n° processo + objeto]
Data-base: [DD/MM/AAAA] · Selo: [referencia]

VICIOS IDENTIFICADOS (de 15 possiveis):
1. [n°] [nome] - art. [lei + ano] + Sum. TCU [n°]
   Evidencia: [trecho do edital + local]
   Impacto: [restricao competitiva / desclassificacao indevida / sancao / etc.]
   Estrategia: [impugnacao art. 164 / esclarecimento art. 164 §1º / aceitar com ressalva]

ESTRATEGIA GLOBAL:
- Vicios criticos: [n°] - impugnacao obrigatoria
- Vicios menores: [n°] - esclarecimento preparatorio
- Total de pedidos sucessivos para impugnacao: [lista]

PROXIMO PASSO:
- Acionar `impugnacao-edital` no prazo art. 164 Lei 14.133 (3 dias uteis ate abertura).
- Esclarecimento estrategico em [vicio X] como preparatorio.

[VERIFICAR]: [IN SEGES atualizacao; jurisprudencia TCU 2024-2026]

---
[Ressalva OAB - PA-07]
```

## 5. Vedacoes especificas

- **PA-04** - Selo.
- **PA-13** - cada vicio com fundamentacao tripla precisa (lei+artigo+ano + sumula TCU + jurisprudencia).
- **PA-15** - cada vicio ancorado na vinculacao ao instrumento (desvio da regra do edital ou da norma).
- **PA-17** - vedado opinar sobre conveniencia (discricionariedade); apenas vicios de legalidade.
- **PA-08** - vedada critica pessoal ao agente de contratacao; foco no ato.

## 6. Protocolos acionados

- **P1** - Selo. **P2** - integridade do edital + anexos. **P5** - jurisprudencia TCU x TCE aplicavel.

## 7. Localizacao

Federal -> TCU + IN SEGES. Estadual/municipal -> TCE/TCM + regulamento local. `[VERIFICAR - regulamento UF/Municipio]`.

## 8. Integracao

**Chamada por:** `analise-edital`, `licitacoes-master`, `analise-oportunidade`.

**Entrega para:** catalogo + roteiro para `impugnacao-edital`. Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** vicios nao identificados ficam preclusos (Sum. TCU 274); proposta entra com gap de habilitacao por nao impugnar restricoes.
