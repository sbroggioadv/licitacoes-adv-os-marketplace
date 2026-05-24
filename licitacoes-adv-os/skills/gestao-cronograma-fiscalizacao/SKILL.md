---
name: gestao-cronograma-fiscalizacao
description: >
  Gestao da execucao contratual e fiscalizacao - DIARIO DE OBRA/SERVICO (art. 119 Lei 14.133/2021), atos do FISCAL DE CONTRATO (art. 117), responsabilidades do GESTOR. NOTIFICACOES FORMAIS como PROVA PRE-CONSTITUIDA de inadimplemento da Administracao (atraso de pagamento, ausencia de fiscalizacao adequada, atraso em medicoes, falta de aprovacao tecnica). Formalizacao de pedidos via processo administrativo. Preservacao de provas para futura rescisao por inadimplemento da Administracao (art. 137 §4º - 90 dias), cobranca (Tier 6), reequilibrio retroativo, indenizacao. Suporte ao consultivo na execucao + preparacao do contencioso. Aciona: gestao do contrato, fiscalizacao, diario de obra, fiscal do contrato, gestor do contrato, art. 117, art. 119, notificacao formal, preservacao de prova, medicoes, recebimento provisorio, recebimento definitivo.
---

# GESTAO E FISCALIZACAO

> Skill **Tier 4** - acompanhamento da execucao contratual + preservacao de prova pre-constituida. Pre-requisito de toda acao de rescisao, cobranca, reequilibrio retroativo. Implementa P1, P2, P5; respeita PA-15 (vinculacao), PA-09 (sigilo).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `contrato-administrativo` (na fase de execucao), ou demanda direta quando ha **situacao de risco** durante a execucao (atraso, fiscalizacao deficiente, medicao indevida, problema operacional). Recebe: contrato + cronograma + historico de execucao + atos da fiscalizacao.

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `contrato-administrativo`, `reequilibrio-economico-financeiro` (quando fato superveniente requer registro), `rescisao-contrato` (preservacao de provas).
- **Pre-requisito:** Selo (PA-04); contrato em execucao.
- **Aciona em sequencia:** `reequilibrio-economico-financeiro` quando ha fato superveniente; `rescisao-contrato` quando ha inadimplemento da Administracao >90 dias (art. 137 §4º); `acao-cobranca-administracao` em paralelo (P4).
- **Entrega para:** roteiro de gestao + modelos de notificacao formal + checklist de preservacao de provas.

## 2. Marco normativo

- **Lei 14.133/2021:**
  - **art. 117** - **fiscalizacao do contrato** - fiscal tecnico + fiscal administrativo + gestor; designacao formal; responsabilidade individual.
  - **art. 118** - dever do fiscal de comunicar irregularidades a autoridade competente.
  - **art. 119** - **diario de obra/servico** - registro continuo e cronologico da execucao; obrigatorio em obras e servicos contínuos.
  - **arts. 140-145** - **recebimento** do objeto - provisorio + definitivo (art. 140); pagamento + ordem cronologica (art. 141).
  - **art. 137 §4º** - direito a rescisao por atraso >90 dias da Administracao.
  - **arts. 124-125** - reequilibrio (interface).
- **IN SEGES MGI 73/2022** - **gestao contratual** (detalhamento operacional).
- **Lei 9.784/1999** - processo administrativo (dever de motivacao + ampla defesa).
- **CC arts. 421-422** - boa-fé objetiva.

## 3. Estrutura da fiscalizacao (art. 117)

| Papel | Responsabilidade |
|-------|------------------|
| **Fiscal tecnico** | Acompanhamento tecnico-qualitativo + medicoes + recebimento provisorio |
| **Fiscal administrativo** | Documental (CNDs, faturas, garantias) + processual |
| **Gestor do contrato** | Coordenacao + decisoes superiores + interface com a contratada |
| **Autoridade superior** | Decisoes de rescisao, sancao, aditivos, reequilibrio |

## 4. Diario de obra/servico (art. 119) - prova nuclear

**Caracteristicas:**
- Registro **cronologico e contínuo** da execucao.
- Visado pela contratada **e** pelo fiscal tecnico.
- Inclui: atividades executadas, mao-de-obra alocada, equipamentos, intercorrencias, pedidos, paralisacoes, condicoes climaticas (em obras).
- **Forca probatoria:** documento publico-administrativo - presuncao de veracidade.

**Estrategia do contratado:**
1. **Insistir no registro diario** - mesmo se o fiscal omite, requerer formalmente o lancamento.
2. **Registrar todas as intercorrencias** - atraso de fornecimento de projeto/local pela Administracao, condicoes nao previstas, modificacoes solicitadas, atrasos de pagamento.
3. **Visar pessoalmente** + obter visto do fiscal.
4. **Copia paralela** em poder da contratada (PA-09 - sigiloso).

## 5. Notificacoes formais - prova pre-constituida

**Quando notificar formalmente** (em processo administrativo - protocolo + numero):
- **Atraso de pagamento** (cada vencimento nao pago).
- **Atraso da Administracao em fornecer** (projeto, local, licenca, aprovacao).
- **Demora em medicao** (fiscalizacao deficiente).
- **Demora em recebimento provisorio/definitivo** (art. 140).
- **Decisao operacional sem motivacao** (Lei 9.784/1999 art. 50).
- **Fato superveniente** que cause desequilibrio (preparacao para `reequilibrio-economico-financeiro`).
- **Modificacao operacional** imposta sem aditivo formal (preparacao para `aditivo-contratual`).

**Estrutura padrao da notificacao:**

```
[CONTRATADA] -> [GESTOR / AUTORIDADE]
PROCESSO ADMINISTRATIVO N° [n°]
CONTRATO N° [n°]

NOTIFICACAO FORMAL N° [seq/ano]

I - FATO
Em [DD/MM/AAAA], constatou-se [descricao precisa].

II - FUNDAMENTACAO
- Lei 14.133/2021 art. [X] - [direito/dever violado]
- Clausula contratual [Y] - [previsao]
- CC arts. 421-422 - boa-fé objetiva

III - PRAZO
A presente notificacao concede prazo de [N] dias para [acao].

IV - CONSEQUENCIAS
O nao atendimento implicara [acionamento de art. 137 §4º / pedido de reequilibrio /
suspensao de execucao com fundamento em fato da Administracao].

V - PEDIDOS
a) Resposta tempestiva motivada;
b) Adequacao da conduta;
c) Registro no Diario (art. 119).

[Cidade], [DD/MM/AAAA]
___________________________________
[Representante legal] - [Razao social]
{{ADVOGADO_NOME}} - OAB/{{OAB_UF}} {{OAB_NUMERO}}
```

## 6. Recebimento (arts. 140-141)

### 6.1 - Recebimento provisorio (art. 140)
- Apos conclusao da execucao - prazo razoavel (regulamento define).
- Atestacao de conformidade tecnica preliminar pelo fiscal tecnico.

### 6.2 - Recebimento definitivo
- Apos prazo de observacao - confirmacao de qualidade + funcionamento.
- Encerra o contrato (com excecao de garantias contratuais e legais - CC art. 618 obras de engenharia 5 anos).

### 6.3 - Estrategia
- **Demora em recebimento** = inadimplemento da Administracao (acionar notificacao).
- **Recusa injustificada** = vicio recorrivel (`recurso-administrativo`).
- **Recebimento com ressalva** = direito da contratada (registrar ressalva + sanear).

## 7. Ordem cronologica de pagamentos (art. 141)

**Suporte ao acompanhamento:**
- Solicitar publicacao da fila + posicao da PJ.
- Quebra da ordem = notificacao formal + acionamento futuro de cobranca (art. 141 + Tema 905 STJ).

## 8. Preservacao de provas - checklist

```
CHECKLIST DE PRESERVACAO - CASO [slug]
Contrato: [n°] - Data de assinatura: [DD/MM/AAAA]
Data-base do checklist: [DD/MM/AAAA] · Selo: [referencia]

DOCUMENTOS BASE:
[ ] Contrato original + aditivos
[ ] Edital + anexos (ETP, TR, matriz de risco, minuta)
[ ] Cronograma de execucao
[ ] Cronograma de pagamento
[ ] Designacao de fiscal tecnico + administrativo + gestor

REGISTROS DA EXECUCAO:
[ ] Diario de obra/servico (art. 119) - visado pelas partes - copia paralela
[ ] Atas de reuniao com a Administracao
[ ] Comunicados, emails formais, oficios

NOTIFICACOES FORMAIS (protocoladas):
[ ] Atrasos de pagamento - N notificacoes
[ ] Atrasos da Administracao em fornecer - N notificacoes
[ ] Demoras em medicao / recebimento - N notificacoes
[ ] Fato superveniente / desequilibrio - N notificacoes
[ ] Modificacoes impostas sem aditivo - N notificacoes

EVIDENCIAS COMPROBATORIAS:
[ ] Faturas + datas de vencimento + datas de pagamento
[ ] Cotacoes de mercado (variacoes de insumo)
[ ] Indices oficiais (IPCA, INCC, INPC)
[ ] CCTs e dissidios (mao-de-obra)

ATENCAO PA-09:
- Documentos sigilosos (planilha de custos, segredo industrial) em
  `<cwd>/licitacoes/casos/<slug>/arquivos/` (gitignored).

[VERIFICAR]: [calendario do orgao para feriados; IN SEGES 73/2022 atualizacao]

---
[Ressalva OAB - PA-07]
```

## 9. Vedacoes especificas

- **PA-04** Selo. **PA-15** vinculacao ao contrato + edital.
- **PA-09** sigilo de documentos da PJ (planilha, segredos, dados internos).
- **PA-08** sem critica pessoal ao fiscal/gestor; foco no ato.
- **PA-17** vedado opinar sobre discricionariedade do agente (cronograma, recebimento condicional); apenas vicios de legalidade ou inadimplemento.
- **PA-07** ressalva OAB.

## 10. Protocolos acionados

- **P1** Selo. **P2** integridade do contrato + provas. **P5** competencia.

## 11. Localizacao

Federal -> IN SEGES 73/2022 + jurisprudencia TCU. Estadual/municipal -> IN local + TCE/TCM. Estatais -> regulamento interno.

## 12. Integracao

**Chamada por:** `licitacoes-master`, `contrato-administrativo`, `reequilibrio-economico-financeiro`, `rescisao-contrato`.

**Entrega para:** roteiro + modelos de notificacao + checklist + `CASO.md`. Aciona `reequilibrio-economico-financeiro`, `rescisao-contrato`, `acao-cobranca-administracao` conforme situacao. Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** execucao sem registro formal; inadimplemento da Administracao nao documentado; impossibilidade de acionar art. 137 §4º; perda de provas para futuro contencioso (Tier 6).
