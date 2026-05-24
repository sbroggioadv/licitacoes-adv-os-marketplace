---
name: tratamento-me-epp
description: >
  Aplicacao do tratamento favorecido a ME/EPP em licitacoes - LC 123/2006 + LC 147/2014: (1) EMPATE FICTO (art. 44 LC 123) - proposta de ME/EPP ate 5% superior a melhor classificada tem direito de cobrir; (2) COTA RESERVADA (art. 48 III LC 123) - ate 25% do objeto reservado a ME/EPP; (3) MARGEM DE PREFERENCIA (art. 26 Lei 14.133/2021); (4) DECLARACAO DE ENQUADRAMENTO necessaria no certame; (5) REGULARIZACAO FISCAL DE ME/EPP (art. 43 §1º LC 123) com 5 dias uteis prorrogaveis apos declaracao de vencedora. Estrategia: quando ME/EPP usa empate ficto vs cota reservada (decisao por certame). Defesa em caso de questionamento ao enquadramento. Aciona: ME, EPP, microempresa, empresa pequeno porte, LC 123, empate ficto, cota reservada, art. 48, art. 44, regularizacao fiscal ME, declaracao de enquadramento.
---

# TRATAMENTO ME/EPP

> Skill **Tier 3** - aplicacao integral do tratamento favorecido a ME/EPP (LC 123/2006 + LC 147/2014). 4 mecanismos: empate ficto, cota reservada, margem de preferencia, regularizacao fiscal especifica. Implementa P1, P2, P5; respeita PA-15 (vinculacao), PA-18 (fronteira sem cross-sell).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `planejamento-proposta` (quando ME/EPP), `habilitacao-documentos` (regularizacao fiscal), `recurso-administrativo` (defesa do enquadramento). Recebe: situacao da PJ-cliente (faturamento anual, atividade, regime tributario), edital (clausulas LC 123 obrigatorias).

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `planejamento-proposta`, `habilitacao-documentos`, `recurso-administrativo`, `analise-edital` (quando ha questao de cota reservada).
- **Pre-requisito:** Selo (PA-04); enquadramento confirmado pela PJ (responsabilidade do operador - PA-09 sigilo de receita).
- **Aciona em sequencia:** `recurso-administrativo` se enquadramento questionado; `contrarrazoes-recurso` se concorrente recorre contra aplicacao do tratamento.
- **Entrega para:** estrategia de aplicacao + checklist documental + roteiro de defesa.

## 2. Marco normativo

- **LC 123/2006 + LC 147/2014:**
  - **art. 3º** - definicao de ME (receita bruta anual <= R$ 360.000) e EPP (receita > R$ 360.000 e <= R$ 4.800.000) - **`[VERIFICAR - atualizacao valores ME/EPP]`** (alvo movel).
  - **art. 43 §1º** - regularizacao fiscal de ME/EPP com **5 dias uteis prorrogaveis** apos declaracao de vencedora.
  - **art. 44** - **empate ficto** - proposta de ME/EPP ate 5% superior a melhor classificada (10% no pregao) tem direito de cobrir.
  - **art. 45** - mecanismo do empate ficto (oferta de nova proposta no prazo).
  - **art. 48 I e III** - **cota reservada a ME/EPP** (ate 25% do objeto licitatorio quando divisivel).
  - **art. 49** - vedacoes (somente quando justificadas).
- **Lei 14.133/2021:**
  - **art. 4º** - aplicacao do regime LC 123 no ambito da lei.
  - **art. 26** - margem de preferencia para ME/EPP (alem de outros casos).
  - art. 48 - regimes especificos de aplicacao.
- **Lei Complementar 167/2019** - Inova Simples (versao especifica - `[VERIFICAR]` aplicabilidade).

## 3. Os 4 mecanismos do tratamento favorecido

### 3.1 - Empate ficto (art. 44 LC 123)

- **Quando incide:** criterio menor preco (incluindo pregao); houve proposta de ME/EPP classificada ate **5% superior** a melhor classificada nao-ME/EPP (10% nos certames presenciais classicos - aplicacao residual).
- **Direito:** a ME/EPP tem direito de apresentar **nova proposta inferior** a do primeiro colocado.
- **Prazo:** 5 minutos uteis em sessao presencial; conforme regulamento em pregao eletronico.
- **Estrategia:** ME/EPP deve estar pronta para reformular proposta no ato (planilha de custos pronta).

### 3.2 - Cota reservada (art. 48 III LC 123)

- **Quando incide:** objeto **divisivel** em lotes/itens; **ate 25% do objeto** reservado a ME/EPP.
- **Aplicacao:** edital deve prever cotas reservadas para itens especificos.
- **Estrategia:** ME/EPP participa **apenas dos itens da cota reservada** sem competir com grandes nesses itens; pode tambem participar dos itens livres em condicao de igualdade.

### 3.3 - Margem de preferencia (art. 26 Lei 14.133)

- **Quando incide:** previsto em edital - margem de preferencia para ME/EPP alem do empate ficto e da cota.
- **Aplicacao:** percentual (regulamento define) sobre a proposta de outras categorias - ME/EPP tem desconto fictico que torna sua proposta vencedora se houver empate ampliado.

### 3.4 - Regularizacao fiscal (art. 43 §1º LC 123)

- **Quando incide:** ME/EPP **declarada vencedora** apresenta restricao em regularidade fiscal (CND vencida, parcelamento) ou trabalhista (CNDT).
- **Direito:** **5 dias uteis prorrogaveis** para regularizar - sem inabilitacao automatica.
- **Estrategia:** nao usar como descuido; usar quando ha pendencia objetiva e regularizavel. **Habilitacao juridica, tecnica e economico-financeira** seguem o regime geral (art. 43 §1º refere-se a fiscal/trabalhista).

## 4. Declaracao de enquadramento

A PJ-cliente deve apresentar **declaracao de enquadramento como ME/EPP** no certame - via Junta Comercial (atestado de enquadramento atualizado) ou conforme regulamento do edital. Falsa declaracao gera responsabilidade administrativa e civel.

## 5. Estrategia - quando usar cada mecanismo

| Cenario | Mecanismo recomendado |
|---------|----------------------|
| Objeto unico, criterio menor preco | Empate ficto (art. 44) |
| Objeto divisivel em lotes | Cota reservada (art. 48 III) + participacao em itens livres |
| Edital com margem de preferencia | Combinar com empate ficto |
| Pendencia fiscal regularizavel | Regularizacao art. 43 §1º (5 dias prorrogaveis) |
| Enquadramento questionado por concorrente | Defesa em recurso/contrarrazoes + atestado de enquadramento |

## 6. Defesa em caso de questionamento

Cenarios tipicos:
1. **Concorrente recorre alegando que ME/EPP nao se enquadra** - contrarrazoes com atestado de enquadramento + declaracao + dados de receita (cuidado com sigilo PA-09).
2. **Agente desconsidera empate ficto / cota** - recurso administrativo art. 165 com fundamento na LC 123.
3. **Inabilitacao por nao-regularizacao fiscal sem oferecer prazo** - recurso fundamentado em art. 43 §1º LC 123.

## 7. Output - Plano de aplicacao (formato)

```
PLANO ME/EPP - CASO [slug]
Edital: [orgao + n° + objeto + valor estimado]
Data-base: [DD/MM/AAAA] · Selo: [referencia]

ENQUADRAMENTO DA PJ:
- Tipo: [ME / EPP]
- Atestado de enquadramento: [valido / a renovar]
- Declaracao especifica para o certame: [pronta]

MECANISMOS APLICAVEIS NESTE CERTAME:
[ ] Empate ficto (art. 44 LC 123) - se criterio menor preco
[ ] Cota reservada (art. 48 III) - se objeto divisivel; itens cotados: [lista]
[ ] Margem de preferencia (art. 26 Lei 14.133) - se edital prever
[ ] Regularizacao fiscal (art. 43 §1º) - status: [aplicavel / nao necessario]

ESTRATEGIA:
- Mecanismo principal: [empate ficto / cota / combinado]
- Justificativa: [vinculacao ao edital + LC 123 + Sum. TCU]
- Acoes:
  - [ ] Declaracao de enquadramento anexa
  - [ ] Planilha de custos pronta para reformulacao em empate ficto
  - [ ] Pendencia fiscal mapeada (se houver) - regularizacao em 5 dias

DEFESA (preparacao preventiva):
- Atestado de enquadramento valido em [DD/MM]
- Documentos de receita (sigiloso - PA-09) em `<cwd>/.../casos/<slug>/arquivos/`
- Argumentos para contrarrazoes se concorrente questionar enquadramento

ATENCAO PA-18:
- Mudanca de regime tributario (Simples / Lucro Presumido / Real) que afete
  enquadramento -> "encaminhar a especialista em direito tributario/contabilidade"
  sem citar produto irmao.

[VERIFICAR]: [atualizacao de valores ME/EPP; regulamento UF/Municipio]

---
[Ressalva OAB - PA-07]
```

## 8. Vedacoes especificas

- **PA-04** Selo.
- **PA-09** - sigilo de receita bruta da PJ (dado sigiloso comercial).
- **PA-15** - tratamento ancorado na vinculacao ao edital (cotas previstas, empate aplicavel ao criterio).
- **PA-18** - aspectos tributarios do regime ME/EPP (Simples) sao fronteira - encaminhar a especialista sem citar produto.
- **PA-11** - valores de enquadramento ME/EPP em alvo movel -> `[VERIFICAR]`.

## 9. Protocolos acionados

- **P1** Selo. **P2** integridade do atestado de enquadramento + declaracao. **P5** regulamento local pode prever cotas adicionais.

## 10. Localizacao

Federal -> aplicacao plena da LC 123. Estadual/municipal -> regulamento local pode definir percentuais de cota (ate o limite da LC). `[VERIFICAR - regulamento UF/Municipio]`. Atestado de enquadramento e emitido pela Junta Comercial do Estado de registro da PJ.

## 11. Integracao

**Chamada por:** `licitacoes-master`, `planejamento-proposta`, `habilitacao-documentos`, `recurso-administrativo`, `analise-edital`.

**Entrega para:** plano + checklist + `CASO.md`. Aciona `habilitacao-documentos` (regularizacao se aplicavel); `recurso-administrativo` ou `contrarrazoes-recurso` se enquadramento for objeto de disputa. Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** ME/EPP perde vantagem competitiva legal (empate ficto, cota, regularizacao); ou aplica indevidamente o tratamento (questionamento por concorrente).
