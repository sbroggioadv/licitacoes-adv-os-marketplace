---
name: representacao-tcu-tce
description: >
  Representacao ao TCU (Lei 8.443/1992 art. 113 §1º + Lei 14.133/2021 art. 174 §1º) ou TCE/TCM (lei organica do respectivo TC). LEGITIMIDADE do licitante consolidada (art. 174 §1º Lei 14.133 + jurisprudencia). Pedido de MEDIDA CAUTELAR (art. 276 RI TCU + analogos nos TCEs) - EFEITO IMEDIATO suspendendo procedimento, contrato ou acordao. Requisitos: fumus boni iuris + periculum in mora. Estrutura da peca: identificacao do ente + ato impugnado + fumus + periculum + pedido cautelar + pedido de merito. Coordenacao com via judicial (P4 - pedido alternativo se TCU nao concede cautelar; representacao concomitante a MS quando estrategico). Acordao TCU vincula Administracao (CF art. 71 IX). Aciona: representacao TCU, representacao TCE, art. 113 §1º Lei 8.443, art. 174 §1º Lei 14.133, art. 276 RI TCU, cautelar TCU, fumus periculum.
---

# REPRESENTACAO AO TCU/TCE

> Skill **Tier 6** - representacao com pedido de cautelar a tribunal de contas. Lei 8.443/1992 art. 113 §1º + Lei 14.133/2021 art. 174 §1º + art. 276 RI TCU. Implementa P1, P2, P3, P4, P5, P6; respeita PA-12 (independencia das esferas), PA-13, PA-15.

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `/judicial`, ou apos exaurimento de via administrativa (recurso improvido) - sem necessidade de esgotamento (PA-21 - estrategia). Recebe: ato impugnado + fundamentacao + provas + analise de urgencia (periculum).

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/judicial`, `recurso-administrativo` (apos denegacao), `impugnacao-edital` (concomitante quando estrategico).
- **Pre-requisito:** Selo (PA-04); ato impugnavel identificado; fundamentacao tripla preparada.
- **Aciona em sequencia:** `revisao-final-licitacoes`; em paralelo com `ms-licitacao-contrato` quando ha urgencia adicional (P4).
- **Entrega para:** peca de representacao + pedido cautelar + roteiro de acompanhamento.

## 2. Marco normativo

- **Lei 8.443/1992 (LOTCU):**
  - **art. 113 §1º** - **representacao** ao TCU: qualquer cidadao, partido politico, associacao ou sindicato; aplicacao analogica para licitante (consolidada).
  - **art. 71** - decisao do TCU vincula a Administracao.
- **Lei 14.133/2021:**
  - **art. 174 §1º** - **legitimidade do licitante** para representar irregularidades a tribunais de contas - **consolidada legalmente**.
  - art. 12 - principios.
- **CF:**
  - **art. 71 IX** - decisao TCU = norma de conformidade obrigatoria para Administracao.
  - art. 75 - simetria - tribunais de contas estaduais e municipais.
- **RI TCU (Regimento Interno):**
  - **art. 276** - **medida cautelar** - efeito imediato; suspende procedimento ou contrato.
  - art. 277 - pre-requisitos: fumus + periculum.
- **TCEs estaduais + TCMs (onde existir):** SP capital, RJ, BA, GO, CE. Cada TC tem seu RI proprio - `[VERIFICAR - RI do TC competente]`.
- **Sumulas TCU vivas:** 222, 247, 248, 251, 269, 274, 277, 287.
- **CF art. 5º XXXIV a** - direito de peticao.

## 3. Quando representar ao TCU/TCE

| Cenario | Vantagem |
|---------|----------|
| Recurso administrativo improvido | TCU pode reformar decisao + suspender |
| Impugnacao denegada | Cautelar TCU suspende abertura/sessao |
| Sancao desproporcional aplicada | TCU revisa dosimetria + suspende efeitos |
| Adjudicacao a concorrente em pregao com vicio | Cautelar suspende contrato |
| Aditivo contratual ilegal | Cautelar suspende aditivo |
| Inadimplemento da Administracao reiterado | Determinacao para regularizar pagamento |

**Vantagem do TCU vs judicial:**
- **Velocidade** - cautelares rapidas (dias/semanas).
- **Tecnicidade** - colegio especializado em contas publicas.
- **Vinculacao a Administracao** - decisao tem forca normativa imediata.
- **Custos** - sem custas judiciais.

## 4. Estrutura canonica - peca de representacao

```
EXMO. PRESIDENTE / RELATOR DO TRIBUNAL DE CONTAS DA [UNIAO / ESTADO / MUNICIPIO]
PROCESSO ADMINISTRATIVO N° [n°] (a ser autuado)

REPRESENTACAO COM PEDIDO DE MEDIDA CAUTELAR
(Lei 8.443/1992 art. 113 §1º + Lei 14.133/2021 art. 174 §1º + RI TCU art. 276)

I - QUALIFICACAO E LEGITIMIDADE
[Razao social - CNPJ - representante legal] - licitante no processo
[n° - orgao - objeto] - legitimidade consolidada (art. 174 §1º Lei 14.133).

II - DOS FATOS
[Narrativa cronologica datada: edital, ato impugnado, recurso administrativo
denegado, urgencia configurada.]

III - DO ATO IMPUGNADO
[Trecho literal do ato + identificacao precisa: numero, data, autoridade emissora]

IV - DA ADMISSIBILIDADE
- Legitimidade: licitante no certame (art. 174 §1º Lei 14.133)
- Interesse: ato gera prejuizo direto a Recorrente
- Materia de competencia do TCU: irregularidade em licitacao/contrato com
  recurso publico federal (art. 71 CF)

V - DO FUMUS BONI IURIS (probabilidade do direito)

V.1 - Da ilegalidade do ato
- Base legal violada: [Lei 14.133/2021 art. + redacao] (PA-13)
- Sumula TCU aplicavel: Sum. n° [Y] - [tema]
- Jurisprudencia STJ/STF/TCU: [Tema/REsp/Acordao TCU n° + ano]
- Vinculacao ao instrumento (PA-15 + art. 12 Lei 14.133): o ato desvia-se
  do edital ao [...].

V.2 - Da incidencia das Sumulas TCU [222/247/251/269/274/277/287]
[Articulacao com a sumula aplicavel]

VI - DO PERICULUM IN MORA (perigo na demora)

- Risco concreto: [adjudicacao iminente / abertura de proposta em DD/MM /
  assinatura do contrato em DD/MM / inicio de execucao com contrato viciado]
- Danos irreversiveis: [perda do certame / consolidacao de contrato ilegal /
  pagamentos indevidos]

VII - DA MEDIDA CAUTELAR PRETENDIDA
Pelo exposto, requer-se concessao de MEDIDA CAUTELAR (art. 276 RI TCU):

a) **SUSPENSAO IMEDIATA** de [procedimento / abertura da sessao / adjudicacao /
   assinatura do contrato / execucao do contrato / efeitos do acordao impugnado]
   ate decisao final desta representacao;
b) Determinacao a [orgao licitante] para [conduta especifica];
c) Comunicacao a [orgao + autoridade superior] sobre a cautelar.

VIII - DOS PEDIDOS DE MERITO
a) Conhecimento da representacao por admissivel;
b) **Procedencia** com determinacao de:
   - Anulacao do ato impugnado
   - Refacao do procedimento conforme a lei
   - Eventual responsabilizacao do agente publico (representacao a autoridade
     competente)
c) Subsidiariamente, providencias menos invasivas;
d) Manutencao da cautelar ate decisao final.

IX - DOCUMENTOS
- Procuracao OAB ativa (PA-05, PA-07)
- Edital + ato impugnado
- Recurso administrativo + decisao denegatoria
- Provas documentais (atas, decisoes, dados de mercado)
- Sumulas TCU + jurisprudencia citadas

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}} - OAB/{{OAB_UF}} {{OAB_NUMERO}}

---
[Ressalva OAB - PA-07]
```

## 5. Coordenacao P4 - via paralela

Representacao **simultanea** ou **subsequente** a:

| Via | Quando |
|-----|--------|
| **MS preventivo na JF/JE** (`ms-licitacao-contrato`) | Adicional ao TCU - urgencia + ato coator individualizado |
| **Acao anulatoria** (`acao-anulatoria-licitacao`) | Sem necessidade de cautelar - prazo de 5 anos contra Fazenda |
| **Acao de cobranca** (`acao-cobranca-administracao`) | Quando ha valores devidos + TCU determinou pagamento |

**Provas cruzadas:** mesma base do recurso administrativo reusada na representacao + MS + anulatoria (principio da economia processual + comunhao das provas).

**Acordao TCU favoravel:** vincula Administracao (CF art. 71 IX) - **executar** administrativamente ou em juizo se houver resistencia.

## 6. TCE/TCM - especificidades

| TC | Esfera + RI |
|----|-------------|
| TCU | Federal + recursos federais transferidos. RI proprio. |
| TCE estadual | Estado + autarquias + estatais estaduais. RI da Lei Organica do Estado. |
| TCM (SP capital, RJ, BA, GO, CE) | Municipio onde existe. RI proprio. |
| TCE municipal (onde nao ha TCM) | Municipios sao fiscalizados pelo TCE estadual. |

`[VERIFICAR - RI do TC competente]` (PA-11) - cada TC tem regras proprias de admissibilidade e prazo.

## 7. Vedacoes especificas

- **PA-04** Selo. **PA-13** citacao precisa (lei+artigo+ano; sumula TCU n° + tema; acordao TCU n° + ano).
- **PA-12** independencia relativa - articular complementariedade entre TCU e judicial.
- **PA-15** ato impugnado articulado na vinculacao ao instrumento.
- **PA-02** vedada promessa de concessao de cautelar.
- **PA-07** ressalva OAB. **PA-08** sem critica pessoal a conselheiro / agente.
- **PA-11** -> `[VERIFICAR]` em RI especifico + jurisprudencia recente.

## 8. Protocolos acionados

- **P1** Selo. **P2** integridade do ato impugnado + provas. **P3** memoria de fumus + periculum. **P4** coordenacao com judicial. **P5** competencia do TC. **P6** R1-R4 obrigatorio.

## 9. Localizacao

TCU - federal. TCE - estadual (de acordo com lei organica do Estado). TCM - SP capital, RJ, BA, GO, CE. Recurso federal transferido a Estado/Municipio -> TCU competente (CF art. 71 VI).

## 10. Integracao

**Chamada por:** `licitacoes-master`, `/judicial`, `recurso-administrativo` (apos denegacao), `impugnacao-edital` (concomitante).

**Entrega para:** peca + roteiro + `CASO.md`. Aciona `ms-licitacao-contrato` se urgencia adicional; `acao-anulatoria-licitacao` em paralelo; aproveitamento defensivo cruzado (P4). Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** via administrativa esgotada -> licitante depende exclusivamente do judicial (lento, custoso) sem mobilizar TCU (rapido, gratuito, tecnicidade especializada).
