---
name: contrarrazoes-recurso
description: >
  Defesa contra recurso administrativo de concorrente (art. 165 Lei 14.133/2021 - 3 dias uteis para contrarrazoes). Objetivo: manutencao do julgamento favoravel ao licitante-cliente. Arguicao preliminar de intempestividade ou inadmissibilidade quando cabivel (intencao nao registrada na sessao motivada - art. 165 §1º; intempestividade do prazo de 3 dias uteis; ilegitimidade). Carencia de motivacao da intencao quando aplicavel. Merito ancorado em vinculacao ao edital (PA-15) + sumula TCU + jurisprudencia. Estrutura FIRAC + 6 secoes. Aciona: contrarrazoes, defesa de recurso, art. 165, defender julgamento, contraargumentar concorrente, intempestividade do recurso.
---

# CONTRARRAZOES DE RECURSO

> Skill **Tier 3** - peca defensiva quando concorrente recorre contra ato favoravel ao licitante-cliente (habilitacao, classificacao, adjudicacao). Prazo: 3 dias uteis. Implementa P1, P2, P3, P5, P6; respeita PA-15, PA-13, PA-08, PA-07.

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `/recurso` (modo contrario), ou diretamente quando o licitante-cliente recebe **notificacao** de que concorrente apresentou intencao de recurso e razoes contra ato favoravel. Recebe: razoes do concorrente + decisao recorrida + edital + provas relevantes.

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/recurso`, `proposta-exequibilidade`, `habilitacao-documentos`, `tratamento-me-epp`.
- **Pre-requisito:** Selo (PA-04); razoes do concorrente em mao; prazo confirmado (`calendario-licitatorio` - 3 dias uteis).
- **Aciona em sequencia:** `revisao-final-licitacoes` obrigatorio.
- **Entrega para:** operador (peca apos R1-R4 + ressalva OAB).

## 2. Marco normativo

- **Lei 14.133/2021:**
  - **art. 165** - recurso administrativo; **§1º** intencao previa motivada na sessao; **§3º** prazo de **3 dias uteis** para contrarrazoes; **§5º** efeito suspensivo do recurso.
  - art. 12 - vinculacao (PA-15).
  - art. 33 - criterio de julgamento; art. 50 - desclassificacao; art. 59 §4º - exequibilidade; arts. 66-70 - habilitacao.
- **CF art. 5º LV** - contraditorio e ampla defesa (do licitante-cliente em face do recurso do concorrente).
- **Lei 9.784/1999** subsidiaria.
- **Sumulas TCU:** 222, 247, 251, 269 (formalismo moderado), 274 (preclusao + intencao motivada como pre-requisito).

## 3. Estrutura canonica - 6 secoes

```
EXMO. [AUTORIDADE COMPETENTE - JULGADORA DO RECURSO]
PROCESSO [n°] - EDITAL [n°] - SESSAO DE [DD/MM/AAAA]
RAZOES DE RECURSO PROTOCOLADAS POR [CONCORRENTE] EM [DD/MM]

CONTRARRAZOES DE RECURSO ADMINISTRATIVO
(art. 165 Lei 14.133/2021 - 3 dias uteis)

I - PRELIMINAR DE TEMPESTIVIDADE
Contrarrazoes apresentadas em [DD/MM/AAAA] - dentro dos 3 dias uteis (art. 165).

II - QUALIFICACAO DO RECORRIDO E LEGITIMIDADE
[Razao social - CNPJ - representante legal - licitante atingida pelo recurso
(classificada, adjudicataria, habilitada)].

III - DAS PRELIMINARES (quando cabivel)

III.1 - DA INTEMPESTIVIDADE DO RECURSO
[Se aplicavel] - O Recorrente apresentou as razoes em [DD/MM], quando o prazo
de 3 dias uteis (art. 165 Lei 14.133) havia expirado em [DD/MM]. A intempestividade
e flagrante e impede o conhecimento.

III.2 - DA INADMISSIBILIDADE POR FALTA DE INTENCAO MOTIVADA NA SESSAO
[Se aplicavel] - O art. 165 §1º Lei 14.133 + Sum. TCU 274 exigem **intencao motivada
na sessao** (PA-19 - preclusao). A ata da sessao de [DD/MM] nao registra intencao
do Recorrente OU a registra de forma generica/sem motivacao especifica. O recurso
e inadmissivel por preclusao da via.

III.3 - DA ILEGITIMIDADE (quando cabivel)
[Se aplicavel] - O Recorrente nao foi parte da fase recorrida / nao se enquadra
no rol do art. 165 / nao apresenta interesse processual concreto.

IV - DOS FATOS
[Narrativa cronologica datada: edital, sessao publica, ato favoravel ao Recorrido,
recurso do Recorrente.]

V - DO MERITO - REFUTACAO DAS RAZOES DO RECURSO

V.1 - Da regularidade do ato recorrido
- Trecho do ato favoravel: [citacao]
- Fundamento legal: [Lei 14.133/2021 art. + redacao] (PA-13)
- Vinculacao ao edital (PA-15 + art. 12 Lei 14.133): o ato cumpre integralmente
  o instrumento convocatorio.

V.2 - Das alegacoes do Recorrente - refutacao item a item
[Ponto 1 do recurso]:
- Argumento do Recorrente: [...]
- Resposta tecnica: [...]
- Base legal contraria: [norma + sumula TCU + jurisprudencia]

[Ponto 2 do recurso]: [...]

V.3 - Da Sum. TCU 269 - formalismo moderado (quando aplicavel)
[Se ato recorrido envolveu saneamento documental]: Sum. TCU 269 - formalismo
moderado autoriza o saneamento; a decisao foi tecnicamente correta.

VI - DOS PEDIDOS
Pelo exposto, requer:
a) Conhecimento das presentes contrarrazoes por tempestivas;
b) Acolhimento das preliminares de [intempestividade / inadmissibilidade /
   ilegitimidade] - extincao do recurso sem julgamento de merito;
c) Subsidiariamente, **NEGATIVA DE PROVIMENTO** do recurso - manutencao do ato
   recorrido (habilitacao / classificacao / adjudicacao em favor da Recorrida);
d) Cessacao do efeito suspensivo (art. 165 §5º) tao logo decidida a improcedencia.

VII - DOS DOCUMENTOS
- Procuracao OAB ativa (PA-05, PA-07)
- Ata da sessao com registro (ou ausencia de registro) da intencao do Recorrente
- Documentos comprobatorios

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}} - OAB/{{OAB_UF}} {{OAB_NUMERO}}

---
[Ressalva OAB - PA-07]
```

## 4. Estrategia - preliminares como primeiro filtro

**Antes de entrar no merito**, esgotar preliminares:

### 4.1 - Intempestividade
- Prazo de **3 dias uteis** (art. 165 §3º).
- Contagem rigorosa - feriado local conta - `[VERIFICAR - calendario do orgao]`.
- Protocolo eletronico com data/hora exatos.

### 4.2 - Inadmissibilidade por falta de intencao motivada (PA-19)
- Sum. TCU 274: matéria não recorrida no momento oportuno preclui.
- Art. 165 §1º exige intencao **motivada na sessao**. Intencao generica = nao atende.
- Ata da sessao e prova decisiva - solicitar copia se necessário.

### 4.3 - Ilegitimidade
- Recorrente deve ter sido **parte do certame e ter sofrido gravame**.
- Concorrente nao classificado para a fase questionada = sem interesse.

### 4.4 - Carencia de fundamentacao
- Razoes genericas, sem fundamentacao tecnica especifica = nao atendem dever de motivacao (Lei 9.784/1999 art. 50 subsidiaria).

## 5. Merito - refutacao item a item

Estrutura ideal: cada ponto do recurso refutado individualmente com:
1. Citacao literal do ponto do Recorrente.
2. Resposta tecnica fundamentada.
3. Base legal contraria (Lei 14.133 + sumula TCU + jurisprudencia).
4. Vinculacao ao edital (PA-15) reforcando regularidade do ato.

## 6. Vedacoes especificas

- **PA-04** Selo emitido. **PA-13** citacao precisa.
- **PA-15** ato favoravel ancorado na vinculacao ao instrumento.
- **PA-19** explorar preclusao em favor do Recorrido quando aplicavel.
- **PA-02** vedada promessa de improvimento.
- **PA-08** vedada critica pessoal ao Recorrente ou advogado; foco no ato/argumento.
- **PA-07** ressalva OAB. **PA-05** rascunho.
- **PA-11** jurisprudencia TCU recente -> `[VERIFICAR]`.

## 7. Protocolos acionados

- **P1** Selo. **P2** integridade da ata + razoes do recorrente. **P3** memoria de decisao. **P5** autoridade competente. **P6** R1-R4 obrigatorio.

## 8. Localizacao

Federal -> TCU paradigma. Estadual/municipal -> TCE/TCM. `[VERIFICAR]` regulamento local.

## 9. Integracao

**Chamada por:** `licitacoes-master`, `/recurso`, `proposta-exequibilidade`, `habilitacao-documentos`, `tratamento-me-epp`.

**Entrega para:** operador + `CASO.md`. Apos decisao final administrativa: se o licitante-cliente perde, pode acionar `representacao-tcu-tce` + `ms-licitacao-contrato` (P4). Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** recurso do concorrente pode prosperar por falta de defesa estruturada - perda do ato favoravel (habilitacao, classificacao, adjudicacao).
