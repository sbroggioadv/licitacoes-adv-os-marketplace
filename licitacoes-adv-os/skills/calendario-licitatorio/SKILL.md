---
name: calendario-licitatorio
description: >
  Skill ancora do roteamento por fase - mapeia prazos do procedimento licitatorio brasileiro: impugnacao ao edital (3 dias uteis art. 164 Lei 14.133/2021); esclarecimento; intencao de recurso na sessao (motivada - art. 165); razoes de recurso (3 dias uteis); contrarrazoes (3 dias uteis); prazo de validade da proposta (60 dias regra); prazos sancionatorios (15 dias uteis defesa - art. 158); prescricao (5 anos Decreto 20.910/1932 contra Fazenda); decadencia MS (120 dias art. 23 Lei 12.016/2009); prescricao PAR (5 anos art. 25 Lei 12.846); ME/EPP regularizacao fiscal (5 dias uteis prorrogaveis - art. 43 §1º LC 123). Configura alertas no CASO.md. Acionada por toda demanda que dependa de prazo. Aciona: prazos do edital, prazo de impugnacao, prazo de recurso, prazo de defesa, prazo de MS, prescricao, decadencia, intencao de recurso, validade da proposta.
---

# CALENDARIO LICITATORIO

> Skill **Tier 1** - âncora do roteamento por fase e gestor de prazos do procedimento. Pre-requisito operacional de toda peca cujo prazo seja critico. Implementa P5 (foro/competencia define base de prazo); auxilia PA-19 (preclusao administrativa) e PA-20 (prescricao).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master` no inicio de qualquer caso e por toda skill cujo output dependa de prazo (impugnacao, recurso, contrarrazoes, defesa em apenamento, MS, anulatoria, cobranca). Recebe: data do edital, data da publicacao no DOU/PNCP, data da sessao, data da decisao administrativa, data da notificacao sancionatoria, data do ato coator. Entrega: linha do tempo + proximos prazos + alertas configurados no `CASO.md`.

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `analise-oportunidade`, `impugnacao-edital`, `recurso-administrativo`, `defesa-apenamento-art-156`, `ms-licitacao-contrato`, `representacao-tcu-tce`, `acao-cobranca-administracao`.
- **Pre-requisito:** Selo emitido (PA-04) - regime aplicavel define base de prazo.
- **Entrega para:** `CASO.md` (timeline + proximos prazos + alertas) + skill solicitante (prazo certo do ato).

## 2. Marco normativo - mapa de prazos

### 2.1 - Fase Interna (F1) e Edital (F2)

| Ato | Prazo | Base legal |
|-----|-------|-----------|
| Publicacao do edital ate abertura | minimo conforme modalidade (variavel) | Lei 14.133/2021 art. 55 |
| **Impugnacao ao edital** | **ate 3 dias uteis antes da abertura** | **art. 164 Lei 14.133/2021** |
| **Esclarecimento** | mesmo prazo da impugnacao | art. 164 §1º Lei 14.133 |
| Resposta da Administracao | ate o dia anterior a abertura | art. 164 §3º |
| **Validade da proposta** | minimo 60 dias regra | art. 50 §3º (ou prazo do edital) |

### 2.2 - Sessao Publica + Habilitacao + Recurso (F3)

| Ato | Prazo | Base legal |
|-----|-------|-----------|
| **Intencao de recurso** (motivada) | **na sessao** (regra Lei 14.133 e regulamentos sucessores) | **art. 165 Lei 14.133/2021** |
| **Razoes de recurso** | **3 dias uteis** apos manifestacao da intencao | art. 165 §3º Lei 14.133/2021 |
| **Contrarrazoes** | **3 dias uteis** apos abertura do prazo | art. 165 §3º |
| **Regularizacao fiscal ME/EPP** | **5 dias uteis prorrogaveis** apos declaracao de vencedora | **art. 43 §1º LC 123/2006** |
| Diligencia (saneamento) | conforme decisao do agente | art. 64 Lei 14.133 |

### 2.3 - Contrato (F4)

| Ato | Prazo | Base legal |
|-----|-------|-----------|
| Assinatura do contrato | conforme edital (60 dias da homologacao - regra) | art. 90 Lei 14.133 |
| Validade da garantia | conforme contrato; 90 dias apos termo | arts. 96-100 |
| **Inadimplemento Administracao -> direito a rescisao** | **>90 dias de atraso de pagamento** | **art. 137 §4º Lei 14.133/2021** |
| Notificacao formal de inadimplemento | conforme contrato; razoavel | art. 137 + boa-fé |

### 2.4 - Sancao + PAR (F5)

| Ato | Prazo | Base legal |
|-----|-------|-----------|
| **Defesa em apenamento (art. 156)** | **15 dias uteis** | **art. 158 §2º Lei 14.133/2021** |
| Recurso da sancao | conforme regulamento + Lei 9.784/1999 | art. 158 + Lei 9.784 |
| **Defesa em PAR** | **30 dias uteis** | **art. 11 Lei 12.846/2013 + Decreto 11.129/2022 art. 13** |
| **Prescricao PAR** | **5 anos da ciencia** | **art. 25 Lei 12.846/2013** |
| Prescricao sancao Lei 14.133 | regulamento + jurisprudencia (regra 5 anos analogica Decreto 20.910/1932) | `[VERIFICAR - regulamento]` |

### 2.5 - Controle Externo (F6)

| Ato | Prazo | Base legal |
|-----|-------|-----------|
| Representacao ao TCU | sem prazo decadencial; cabe enquanto haja interesse e ato impugnavel | Lei 8.443/1992 art. 113 §1º + Lei 14.133/2021 art. 174 §1º |
| Pedido de cautelar TCU | imediato (urgencia da decisao) | art. 276 RI TCU |
| Recurso interno no TCU | conforme RI TCU (Embargos, Pedido de Reexame, Recurso de Reconsideracao) | RI TCU |

### 2.6 - Judicial (F7)

| Ato | Prazo | Base legal |
|-----|-------|-----------|
| **Mandado de seguranca - decadencia** | **120 dias da ciencia do ato coator** | **art. 23 Lei 12.016/2009** |
| Acao anulatoria - prazo | sem decadencia legal; prescricao quinquenal contra Fazenda | Decreto 20.910/1932 art. 1º |
| **Acao de cobranca contra Fazenda** | **5 anos da exigibilidade** | **Decreto 20.910/1932 art. 1º** |
| Liminar/tutela de urgencia | imediato (urgencia + fumus + periculum) | CPC art. 300; Lei 12.016 art. 7º III |

### 2.7 - Casos especiais

- **Improbidade Lei 8.429/1992 reformada pela Lei 14.230/2021** - prescricao 8 anos para ato doloso (art. 23 c/c) + prescricao intercorrente (art. 23 §5º). Tema STF 1.199 - retroatividade benefica pendente -> `[VERIFICAR]`.
- **Acao penal pelos crimes da Lei 14.133/2021 (arts. 337-A a 337-O CP)** - prescricao conforme CP arts. 109-117.
- **Reequilibrio (art. 124-125)** - sem prazo decadencial expresso; estrategia: pedir tempestivamente (proximidade do fato) para evitar arguicao de extinção da pretensão pela boa-fé objetiva (CC art. 422).
- **Repactuacao** - **anual** para mao-de-obra exclusiva (IN SEGES MP 5/2017 art. 53 - residual).

## 3. Tabela cronologica padrao do CASO.md

```
TIMELINE DO CASO
| Marco | Data | Prazo seguinte | Skill responsavel |
|-------|------|----------------|-------------------|
| Edital publicado | [DD/MM/AAAA] | impugnacao ate [data + 3 dias uteis prazo final art. 164] | impugnacao-edital |
| Abertura da sessao | [DD/MM/AAAA] | intencao + razoes em 3 dias uteis | recurso-administrativo |
| Decisao de habilitacao | [DD/MM/AAAA] | recurso 3 dias uteis | recurso-administrativo |
| Adjudicacao | [DD/MM/AAAA] | impugnacao 3 dias / MS 120 dias da ciencia | recurso / ms-licitacao |
| Assinatura do contrato | [DD/MM/AAAA] | execucao - prazo do contrato | contrato-administrativo |
| Inadimplemento Administracao | [DD/MM/AAAA] | rescisao apos 90 dias | rescisao-contrato |
| Notificacao sancao | [DD/MM/AAAA] | defesa 15 dias uteis art. 158 | defesa-apenamento-art-156 |
| Notificacao PAR | [DD/MM/AAAA] | defesa 30 dias uteis | par-lei-12846 |
| Ato coator MS | [DD/MM/AAAA] | impetracao em 120 dias art. 23 | ms-licitacao-contrato |
| Acordao TCU | [DD/MM/AAAA] | recurso interno conforme RI | representacao-tcu-tce |
```

## 4. Calculo de dias uteis

Lei 14.133/2021 art. 183 + CPC art. 219 (subsidiario): **prazos administrativos contam em dias uteis** (excluem sabados, domingos, feriados federais/estaduais/municipais). Feriado local do orgao licitante conta - `[VERIFICAR - calendario do orgao]` (PA-11).

## 5. Alertas configurados no CASO.md

```
ALERTAS ATIVOS
- [PRAZO CRITICO] Impugnacao ate [DD/MM/AAAA] - 3 dias uteis (art. 164 Lei 14.133)
- [PRAZO CRITICO] Razoes de recurso ate [DD/MM/AAAA] - 3 dias uteis (art. 165)
- [PRAZO CRITICO] Defesa em apenamento ate [DD/MM/AAAA] - 15 dias uteis (art. 158)
- [PRAZO CRITICO] MS ate [DD/MM/AAAA] - 120 dias (art. 23 Lei 12.016)
- [VERIFICAR] Feriado local em [data] pode afetar contagem
```

## 6. Vedacoes especificas

- **PA-04** - Selo antes da gestao de prazos (regime aplicavel = base do prazo).
- **PA-11** - feriado local nao confirmado -> `[VERIFICAR]`. Prazos em alvo movel (sancao Lei 14.133 sem regulamento) -> `[VERIFICAR]`.
- **PA-19** - preclusao administrativa: silencio em momento procedimental oportuno preclui. Esta skill marca prazos justamente para evitar preclusao.
- **PA-20** - prescricao alvo movel (Tema STF 1.199 pendente; Decreto 20.910/1932 vs Lei 12.846 art. 25 vs Lei 14.230/2021).

## 7. Protocolos acionados

- **P1** - Selo (regime aplicavel define base do prazo - Lei 14.133 vs Lei 8.666 residual).
- **P4** - prazos cruzados entre vias (administrativa 3 dias x TCU sem prazo x MS 120 dias).
- **P5** - foro/regulamento local pode alterar base de contagem.

## 8. Localizacao

Esfera federal -> calendario do orgao federal (feriados nacionais + estaduais aplicaveis a unidade). Estadual/municipal -> calendario local. Feriado bancario nao e feriado processual. `[VERIFICAR - calendario do orgao]` quando duvida.

## 9. Integracao

**Chamada por:** `licitacoes-master`, e por toda skill cujo output dependa de prazo critico.

**Entrega para:** `CASO.md` (timeline + alertas) + skill solicitante (prazo exato para a peca).

**Sem esta skill:** prazos perdidos (preclusao art. 164/165 - Sum. TCU 274) ou peca extemporanea (extincao). E gatekeeper temporal do plugin.
