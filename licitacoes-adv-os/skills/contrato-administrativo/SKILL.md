---
name: contrato-administrativo
description: >
  Analise e consultivo de contrato administrativo (arts. 89-116 Lei 14.133/2021). Clausulas necessarias art. 92, clausulas exorbitantes art. 104 (modificacao unilateral, rescisao unilateral, fiscalizacao, sancoes, ocupacao de bens), garantia arts. 96-100 (5% regra, ate 10% obras grande vulto, modalidades: caucao, seguro-garantia, fianca bancaria), prazo arts. 105-114 (execucao x vigencia; prorrogacao de continuos), regime de execucao (empreitada global/unitario/integral/contratacao por escopo), pagamento arts. 141-145 com ORDEM CRONOLOGICA principio art. 141. Analise de minuta com identificacao de riscos (consultivo). Negociacao limitada - regime vinculado ao edital (PA-15). Aciona: contrato administrativo, minuta contratual, art. 89, art. 92, art. 104, garantia contratual, fiscalizacao, ordem cronologica de pagamentos, clausulas exorbitantes.
---

# CONTRATO ADMINISTRATIVO

> Skill **Tier 4** - analise e consultivo do contrato administrativo da PJ-cliente (lado fornecedor). Cobre minuta no edital (pre-assinatura) e contrato assinado em execucao. Implementa P1, P2, P3, P5; respeita PA-15 (vinculacao ao edital), PA-09 (sigilo de valores).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `analise-edital` (quando edital traz minuta), apos adjudicacao (preparacao para assinatura), ou em execucao quando ha consulta sobre clausulas. Recebe: minuta ou contrato + edital + matriz de risco + dados internos da PJ.

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `analise-edital`, `planejamento-proposta`, `reequilibrio-economico-financeiro`, `aditivo-contratual`, `rescisao-contrato`, `gestao-cronograma-fiscalizacao`.
- **Pre-requisito:** Selo (PA-04); contrato/minuta + edital (vinculacao PA-15).
- **Aciona em sequencia:** `analise-matriz-risco` (preparacao para reequilibrio); `gestao-cronograma-fiscalizacao` (na execucao); `reequilibrio-economico-financeiro` quando ha desequilibrio.
- **Entrega para:** parecer/analise + lista de pontos criticos + sugestoes de blindagem operacional.

## 2. Marco normativo

- **Lei 14.133/2021 (Capitulo Contratos):**
  - **arts. 89-91** - formalizacao do contrato (instrumento escrito; vinculacao ao edital e a proposta; assinatura).
  - **art. 92** - **clausulas necessarias** (objeto + elementos; vinculacao ao edital + proposta; legislacao aplicada; regime de execucao; preco + condicoes de pagamento; prazo; garantia; sancoes; rescisao; foro; manutencao de habilitacao; outras).
  - **art. 93** - clausulas particulares conforme natureza do contrato.
  - **art. 94** - publicidade do contrato.
  - **arts. 96-100** - **garantia** (5% regra; ate 10% obras de grande vulto; 3 modalidades: caucao em dinheiro/titulos, seguro-garantia, fianca bancaria; devolucao com correcao; perdimento por inadimplemento).
  - **art. 104** - **clausulas exorbitantes** (modificacao unilateral; rescisao unilateral; fiscalizacao; aplicacao de sancoes; ocupacao provisoria).
  - **arts. 105-114** - **prazo** (regra: prazo de execucao definido; prorrogacao de continuos por ate 60 meses + indices).
  - **arts. 115-116** - subcontratacao (admitida com previsao).
  - **arts. 117-119** - **fiscalizacao e gestao** (fiscal tecnico + administrativo + gestor; diario de obra/servico).
  - **arts. 124-125** - alteracao + reequilibrio.
  - **arts. 137-139** - rescisao.
  - **art. 141** - **ordem cronologica de pagamentos** (principio - cada exercicio + cada fonte).
  - **arts. 141-145** - pagamento.
- **CC arts. 421-422** - boa-fé objetiva.
- **CF art. 37 XXI** - vinculacao + manutencao da equacao economico-financeira.
- **Lei 4.320/1964** - ordem cronologica + exercicio orcamentario.
- **Sumulas TCU:** 287 (consorcios); jurisprudencia consolidada sobre clausulas exorbitantes.

## 3. Checklist de clausulas necessarias (art. 92)

1. **Objeto e elementos** - precisa, vinculada ao edital (PA-15).
2. **Vinculacao ao edital e a proposta** - clausula explicita.
3. **Legislacao aplicada** - Lei 14.133/2021 (ou Lei 8.666/1993 residual).
4. **Regime de execucao** - empreitada por preco global / unitario / integral / contratacao por escopo.
5. **Preco e condicoes de pagamento** - valor total, parcelas, fluxo, indices de reajuste (IPCA, INCC, INPC).
6. **Prazo** - execucao + vigencia + termo de inicio.
7. **Garantia** - modalidade + percentual + validade.
8. **Direitos e responsabilidades das partes** - simetria + obrigacoes administrativas.
9. **Sancoes** - referencia ao art. 156 Lei 14.133.
10. **Casos de rescisao** - referencia ao art. 137.
11. **Foro** - Vara da Fazenda Publica da JE local (ou JF se ente federal).
12. **Manutencao de habilitacao** durante a execucao.
13. **Reajuste/repactuacao/revisao** (PA-15 - direito constitucional CF art. 37 XXI).

## 4. Clausulas exorbitantes (art. 104) - leitura defensiva

### 4.1 - Modificacao unilateral
- Limites: ate 25% acrescimo/supressao no comum; ate 50% reforma de edificio/equipamento (art. 124 I).
- Defesa do contratado: aceitar OU recusar (rescisao com indenizacao - art. 137 §5º).
- Compensacao: revisao para preservar equacao (art. 124 §2º).

### 4.2 - Rescisao unilateral
- Hipoteses: art. 137 I-XII (inadimplemento, dolo, etc.).
- Defesa: ampla defesa (Lei 9.784/1999 + CF art. 5º LV); peca defensiva (`rescisao-contrato`).

### 4.3 - Fiscalizacao
- Direito da Administracao mas com **dever de motivacao** (Lei 9.784/1999 art. 50).
- Defesa do contratado: notificacoes formais como prova pre-constituida (`gestao-cronograma-fiscalizacao`).

### 4.4 - Sancoes
- Art. 156 - 4 sancoes (advertencia, multa, impedimento, inidoneidade).
- Defesa: art. 158 - rito procedimental + 15 dias uteis (`defesa-apenamento-art-156`).

### 4.5 - Ocupacao provisoria
- Hipoteses excepcionais; dever de indenizacao por danos.

## 5. Garantia (arts. 96-100)

- **Percentual:** 5% regra; ate 10% **obras de grande vulto justificadas**.
- **Modalidades:** caucao em dinheiro/titulos publicos; seguro-garantia; fianca bancaria.
- **Validade:** durante a execucao + 90 dias apos recebimento definitivo.
- **Devolucao:** corrigida (caucao em dinheiro) + sem onus se cumprido o contrato.
- **Perdimento:** total ou parcial em caso de inadimplemento (art. 99).
- **Defesa do contratado:** vicio na clausula de garantia (>5% sem ser grande vulto + sem justificativa) -> impugnacao **antes** da assinatura ou em fase apropriada.

## 6. Ordem cronologica de pagamentos (art. 141)

**Principio:** pagamentos seguem ordem cronologica de cada exercicio + cada fonte de recurso. Quebra da ordem cronologica = vicio com possivel ressarcimento + responsabilidade do agente.

**Defesa do contratado:**
- Acompanhar fila de pagamento publicada.
- Notificacao formal em caso de quebra.
- Acionar `acao-cobranca-administracao` (Tier 6) se inadimplemento + acaberta de prazos (art. 137 §4º - 90 dias dao direito a rescisao).

## 7. Vinculacao ao edital (PA-15) - blindagem operacional

Toda clausula contratual deve refletir o edital. Divergencia entre contrato e edital = **vicio**; prevalece o edital (art. 89). Estrategia:
1. Conferir cada clausula do contrato com o edital.
2. Discrepancia -> exigir adequacao ou impugnacao.
3. Documentar em ata todas as ressalvas no momento da assinatura.

## 8. Output - Parecer (formato)

```
PARECER CONTRATO ADMINISTRATIVO - CASO [slug]
Edital: [orgao + n° + objeto + valor]
Modalidade contrato: [escrito + assinaturas + publicidade]
Data-base: [DD/MM/AAAA] · Selo: [referencia]

CHECKLIST CLAUSULAS NECESSARIAS (art. 92):
[ ] Objeto - [conforme / nao-conforme]
[continuar 13 itens]

CLAUSULAS EXORBITANTES (art. 104) - LEITURA DEFENSIVA:
- Modificacao unilateral: [limites + defesa]
- Rescisao unilateral: [hipoteses + ampla defesa]
- Fiscalizacao: [dever de motivacao]
- Sancoes: [referencia art. 156 + 158]
- Ocupacao: [excepcional + indenizacao]

GARANTIA (arts. 96-100):
- Modalidade exigida: [caucao / seguro / fianca]
- Percentual: [%] - [conforme / desproporcional - art. 96]

PRAZO E REGIME:
- Execucao: [X dias / meses]
- Vigencia: [X meses; prorrogacao se continuo]
- Regime: [empreitada / contratacao por escopo]

ORDEM CRONOLOGICA (art. 141):
- Acompanhamento da fila exigido
- Quebra = direito a notificacao + cobranca

VINCULACAO AO EDITAL (PA-15):
- Conferencia clausula a clausula: [discrepancias N]

PONTOS CRITICOS / RISCOS:
1. [risco] - [acao defensiva]

ESTRATEGIA:
- Pre-assinatura: [ressalvas em ata; impugnacao de vicios]
- Execucao: notificacoes formais; preservacao de provas; matriz de risco ativada
- Suporte: `gestao-cronograma-fiscalizacao` + `analise-matriz-risco`

[VERIFICAR]: [regulamento UF/Municipio; IN SEGES 73/2022]

---
[Ressalva OAB - PA-07]
```

## 9. Vedacoes especificas

- **PA-04** Selo. **PA-15** vinculacao ao edital em cada clausula.
- **PA-09** sigilo dos valores (proposta/planilha/aditivos sigilosos da PJ).
- **PA-17** vedado opinar sobre discricionariedade do orgao em fixar prazos ou regime; apenas vicios de legalidade.
- **PA-07** ressalva OAB. **PA-08** sem critica pessoal a fiscal/gestor.

## 10. Protocolos acionados

- **P1** Selo. **P2** integridade do contrato + edital. **P3** memoria de quantum (valor, garantia, multas). **P5** foro/competencia.

## 11. Localizacao

Federal -> JF + TCU; IN SEGES 73/2022. Estadual/municipal -> JE local + TCE/TCM. Estatal -> regulamento interno (Lei 13.303/2016).

## 12. Integracao

**Chamada por:** `licitacoes-master`, `analise-edital`, `planejamento-proposta`, `reequilibrio-economico-financeiro`, `aditivo-contratual`, `rescisao-contrato`, `gestao-cronograma-fiscalizacao`.

**Entrega para:** parecer + `CASO.md`. Aciona em sequencia as skills de Tier 4 conforme situacao. Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** assinatura de contrato com clausulas viciadas; execucao sem leitura defensiva das clausulas exorbitantes; ausencia de preparacao para reequilibrio/rescisao/cobranca.
