---
name: recurso-administrativo
description: >
  Peca CRITICA da fase F3 - recurso administrativo (art. 165 Lei 14.133/2021 - 3 dias uteis). Pre-requisito: intencao de recurso na sessao motivada (art. 165 §1º - sob pena de preclusao). Efeito SUSPENSIVO AUTOMATICO sobre a fase recorrida. Estrutura FIRAC + 6 secoes; fundamentacao tripla (lei + sumula TCU + jurisprudencia STJ); vinculacao ao edital (PA-15); pedidos sucessivos (reforma + anulacao parcial + anulacao total). Coordenacao P4 com via TCU (representacao + cautelar art. 276 RI TCU se recurso improvido) e judicial (MS preventivo Lei 12.016 se urgencia). Aciona: recurso administrativo, art. 165, 3 dias uteis, intencao de recurso, razoes, efeito suspensivo, desclassificacao, inabilitacao, reforma de decisao.
---

# RECURSO ADMINISTRATIVO

> Skill **Tier 3 - CRITICA** - peca central da fase F3. Art. 165 Lei 14.133/2021. **Prazo: 3 dias uteis. Intencao previa na sessao motivada (preclusao Sum. TCU 274).** Implementa P1, P2, P3, P4, P5, P6; respeita PA-04, PA-13, PA-15, PA-19 (preclusao), PA-02 (sem promessa), PA-07, PA-08.

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `/recurso`, `habilitacao-documentos` (apos inabilitacao), `proposta-exequibilidade` (apos desclassificacao), por demanda direta de recurso. Recebe: decisao recorrida + intencao de recurso registrada na sessao + edital + provas (documentos, atos da sessao, dados de mercado).

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/recurso`, `habilitacao-documentos`, `proposta-exequibilidade`, `recurso-administrativo` (em caso multi-via P4).
- **Pre-requisito ABSOLUTO:** Selo (PA-04); **intencao de recurso na sessao motivada** (PA-19 + art. 165 §1º Lei 14.133); prazo confirmado (`calendario-licitatorio` - 3 dias uteis).
- **Aciona em sequencia:** `revisao-final-licitacoes` (R1-R4) - obrigatorio antes de devolver; se improvido -> `representacao-tcu-tce` + `ms-licitacao-contrato` (P4 - aproveitamento defensivo cruzado).
- **Entrega para:** operador (peca apos R1-R4 + ressalva OAB). Operador protocola sob OAB.

## 2. Marco normativo

- **Lei 14.133/2021:**
  - **art. 165** - recurso administrativo; **§1º** intencao previa motivada (na sessao); **§3º** prazo de **3 dias uteis** para razoes; **3 dias uteis** para contrarrazoes; **§5º** efeito suspensivo automatico sobre a fase recorrida.
  - art. 12 - vinculacao (PA-15).
  - art. 33 - criterio de julgamento.
  - art. 50 - desclassificacao.
  - art. 59 §4º - exequibilidade (70%).
  - art. 64 - diligencia saneadora.
  - arts. 66-70 - habilitacao.
  - art. 156 - sancao (se recurso de aplicacao de sancao).
  - art. 156 §3º + art. 158 - rito sancionatorio (defesa em 15 dias uteis - separado deste recurso, mas pode haver interface).
- **CF art. 5º LV** - contraditorio + ampla defesa.
- **Lei 9.784/1999** - processo administrativo federal (subsidiaria).
- **Sumulas TCU:** 222, 247, 251, 269 (formalismo moderado), 274 (preclusao).
- **Jurisprudencia STJ:** habilitacao, exequibilidade (REsps + Temas - `[VERIFICAR]` regime aplicavel).

## 3. Estrutura canonica - FIRAC + 6 secoes

```
EXMO. [AUTORIDADE COMPETENTE - AGENTE SUPERIOR / COMISSAO REVISORA]
PROCESSO [n°] - EDITAL [n°] - SESSAO DE [DD/MM/AAAA]

RAZOES DE RECURSO ADMINISTRATIVO
(art. 165 Lei 14.133/2021 - 3 dias uteis)

I - PRELIMINAR DE TEMPESTIVIDADE E ADMISSIBILIDADE
- Intencao de recurso motivada apresentada NA SESSAO de [DD/MM/AAAA] - termo
  consignado em ata (art. 165 §1º Lei 14.133) - **pre-requisito atendido** (PA-19).
- Razoes apresentadas em [DD/MM/AAAA] - dentro dos 3 dias uteis legais (art. 165).
- Efeito suspensivo automatico sobre a fase recorrida (art. 165 §5º).

II - QUALIFICACAO E LEGITIMIDADE
[Razao social - CNPJ - representante legal - licitante classificada/desclassificada
em [posicao] na sessao publica].

III - DOS FATOS
[Narrativa cronologica datada: publicacao do edital, abertura da sessao, ato
recorrido especifico (decisao de habilitacao/desclassificacao/julgamento), intencao
de recurso na sessao, presente recurso.]

IV - DO DIREITO

IV.1 - Da nulidade/reforma do ato [especifico]
- Trecho do ato recorrido: "[citacao]"
- Vicio juridico: [tipologia]
- Base legal violada: [Lei 14.133/2021 art. X + Lei 8.666 residual se aplicavel] (PA-13)
- Sumula TCU aplicavel: Sum. n° [Y] - [tema]
- Jurisprudencia STJ/STF: [Tema/REsp/RE + tribunal + turma + ano]
- Vinculacao ao instrumento (PA-15 + art. 12 Lei 14.133): o ato afastou-se
  do edital ao [descricao].
- Sum. TCU 269 - formalismo moderado (se vicio formal sanavel): falha sanavel
  e oportunidade de saneamento art. 64.

IV.2 - [Argumento subsidiario, se houver]

V - DOS PEDIDOS SUCESSIVOS
a) Conhecimento do recurso por tempestivo e admissivel;
b) Provimento - **reforma** da decisao impugnada com [efeito A];
c) Subsidiariamente, anulacao parcial do ato com determinacao de [efeito B];
d) Subsidiariamente, anulacao total da decisao;
e) Em qualquer hipotese, manutencao do efeito suspensivo (art. 165 §5º) ate
   decisao final.

VI - DOS DOCUMENTOS
- Procuracao OAB ativa (PA-05, PA-07)
- Ata da sessao com intencao de recurso registrada
- Documentos comprobatorios dos fatos narrados
- Eventuais cotacoes de mercado / planilhas / atestados

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}} - OAB/{{OAB_UF}} {{OAB_NUMERO}}
{{FIRM_NAME}}

---
[Ressalva OAB - PA-07]
Esta peça é rascunho técnico-operacional gerado por ferramenta de apoio. A
revisão final, conferência probatória e responsabilidade técnica pela versão
protocolada são do(a) advogado(a) com OAB ativa. Selo de Validação Legal
Prévia emitido em [data]. Pontos [VERIFICAR]: [lista].
```

## 4. Categorias de recurso mais comuns

### 4.1 - Recurso contra inabilitacao da PJ-cliente
- Argumentos: vinculacao ao edital (PA-15) + Sum. TCU 269 (formalismo moderado) + Sum. 222/251 (capacidade tecnica razoavel) + art. 64 (diligencia saneadora omitida).
- Pedido principal: habilitacao da Recorrente; pedido sucessivo: diligencia saneadora.

### 4.2 - Recurso contra desclassificacao por inexequibilidade
- Argumentos: art. 59 §4º (presuncao **relativa**) + planilha de custos detalhada + Sum. TCU sobre exequibilidade + art. 64 (diligencia obrigatoria).
- Coordenacao com `proposta-exequibilidade`.

### 4.3 - Recurso de habilitacao/classificacao contra concorrente
- Argumentos: vicio de habilitacao do concorrente (documento faltante, vencido, incompativel) ou inexequibilidade da proposta (art. 59 §4º).
- Pedido: desclassificacao/inabilitacao da concorrente.

### 4.4 - Recurso contra adjudicacao
- Argumentos: vicio do julgamento que precede a adjudicacao; nulidade da decisao.
- Pedido: anulacao da adjudicacao + repeticao do julgamento + manutencao do efeito suspensivo.

## 5. Coordenacao P4 - vias paralelas

**Se recurso improvido:**
1. **Representacao ao TCU/TCE** com pedido de **cautelar** (`representacao-tcu-tce`) - art. 174 §1º Lei 14.133 + art. 276 RI TCU - efeito imediato.
2. **MS** (`ms-licitacao-contrato`) - Lei 12.016/2009 - ato coator individualizado + direito liquido e certo + 120 dias (art. 23). Preventivo se ameaca; repressivo se ato consumado.
3. **Provas cruzadas:** mesma base do recurso administrativo (decisao recorrida + documentos + ata) reusada nas duas vias paralelas - principio da comunhao das provas.

**Acordao TCU vinculante** (CF art. 71 IX + Lei 8.443/1992) - decisao TCU acolhendo representacao obriga a Administracao a cumprir; e arma poderosa quando recurso administrativo nao prospera.

## 6. Estrategia de tempestividade (PA-19 - preclusao)

**Intencao de recurso na sessao = pre-requisito ABSOLUTO** (art. 165 §1º + Sum. TCU 274):
- Sem intencao registrada -> recurso inadmitido.
- **Motivacao da intencao:** breve (1-2 linhas) - suficiente para identificar materia. Razoes detalhadas vem em 3 dias.
- Intencao generica ("recorrerei sobre tudo") - risco de inadmissibilidade.

**Calendario:**
- Sessao publica - dia D - intencao motivada registrada em ata.
- D+1 ao D+3 (dias uteis) - razoes (peca formal protocolada).
- Resposta de contrarrazoes - 3 dias uteis (`contrarrazoes-recurso`).
- Decisao final - prazo razoavel do orgao (art. 165 §6º).

## 7. Vedacoes especificas

- **PA-04** - Selo emitido. **PA-13** - citacao precisa de norma+sumula+jurisprudencia.
- **PA-15** - cada argumento ancorado na vinculacao ao instrumento.
- **PA-19** - tempestividade rigorosa; intencao previa registrada.
- **PA-02** - vedada promessa de provimento; probabilidade tecnica.
- **PA-08** - vedada critica pessoal a agente de contratacao/membro de comissao; foco no ato.
- **PA-07** - ressalva OAB. **PA-05** - peca = rascunho; protocolo do advogado OAB ativo.
- **PA-11** - jurisprudencia TCU recente -> `[VERIFICAR]`.

## 8. Protocolos acionados

- **P1** Selo. **P2** integridade do ato recorrido + ata. **P3** memoria de decisao (rastreabilidade quadrupla). **P4** coordenacao com TCU + judicial. **P5** autoridade competente para julgar (em regra: autoridade superior). **P6** R1-R4 obrigatorio.

## 9. Localizacao

Federal -> recurso ao superior do agente; TCU paradigma. Estadual/municipal -> recurso ao superior; TCE/TCM paradigma. MS subsequente: JF se autoridade federal; JE se estadual/municipal. `[VERIFICAR]` regulamento UF/Municipio.

## 10. Integracao

**Chamada por:** `licitacoes-master`, `/recurso`, `habilitacao-documentos`, `proposta-exequibilidade`.

**Entrega para:** operador (peca apos R1-R4) + `CASO.md`. Se improvido -> `representacao-tcu-tce` + `ms-licitacao-contrato` (P4 multi-via). Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** decisao injusta vira definitiva administrativamente - perda do certame; necessidade de recorrer somente a judicial ja em desvantagem.
