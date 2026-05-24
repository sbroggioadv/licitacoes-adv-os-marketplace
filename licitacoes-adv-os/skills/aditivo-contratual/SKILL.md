---
name: aditivo-contratual
description: >
  Alteracao contratual - termo aditivo vs apostilamento. UNILATERAL (art. 124 I Lei 14.133/2021 - acrescimo/supressao ate 25% do valor; 50% para reforma de edificio/equipamento) x BILATERAL (art. 124 II e III - alteracao de regime de execucao, substituicao de garantia, modificacao de clausulas, reequilibrio, prorrogacao de continuos). APOSTILAMENTO (art. 136 - reajuste, atualizacao contratual, retificacao de erro - sem alteracao substantiva) x TERMO ADITIVO (alteracao substantiva). Distincao critica - fronteira frequentemente impugnada pelo TCU. Limites legais (25%/50%) sao GARANTIA do contratado (CF art. 37 XXI). Aciona: aditivo contratual, apostilamento, alteracao contratual unilateral, alteracao bilateral, prorrogacao de contrato continuo, acrescimo de 25%.
---

# ADITIVO CONTRATUAL

> Skill **Tier 4** - alteracao contratual: aditivo (substantivo) vs apostilamento (acidental). Distincao critica - fronteira frequentemente impugnada pelo TCU. Implementa P1, P2, P5; respeita PA-15, PA-13, PA-09.

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `contrato-administrativo`, `reequilibrio-economico-financeiro` (quando reequilibrio se formaliza por aditivo), `gestao-cronograma-fiscalizacao` (quando ha necessidade de prorrogacao). Recebe: contrato + situacao concreta (necessidade de alteracao, motivo, percentual).

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `contrato-administrativo`, `reequilibrio-economico-financeiro`, `gestao-cronograma-fiscalizacao`.
- **Pre-requisito:** Selo (PA-04); contrato vigente; motivacao da alteracao documentada.
- **Aciona em sequencia:** `revisao-final-licitacoes`; se aditivo abusivo -> `recurso-administrativo` / `representacao-tcu-tce`.
- **Entrega para:** parecer + minuta de aditivo ou apostilamento + estrategia.

## 2. Marco normativo

- **Lei 14.133/2021:**
  - **art. 124 I** - **alteracao unilateral** (acrescimo ate **25%** do valor inicial atualizado; **50%** para reforma de edificio/equipamento).
  - **art. 124 II** - alteracoes **bilaterais**: substituicao da garantia (art. 124 II a); modificacao de regime de execucao (b); modificacao de forma de pagamento (c) com vedacao ao desequilibrio; **revisao** (d - § 1º para reequilibrio).
  - **art. 124 III** - prorrogacao - regra: contratos contínuos podem ser prorrogados ate 60 meses (art. 107) + ate 10 anos para servicos contínuos com mao-de-obra exclusiva quando vantajoso (com regulamento).
  - **art. 125** - aplicacao das alteracoes (procedimento).
  - **art. 136** - **apostilamento** - reajuste; atualizacao contratual; retificacao de erro material; mudanca de empenho.
  - **arts. 105-114** - prazos contratuais.
- **CF art. 37 XXI** - manutencao da equacao economico-financeira (limites de alteracao protegem o contratado).
- **CC arts. 421-422** - boa-fé objetiva.
- **Sumulas TCU:** jurisprudencia consolidada sobre limites de aditamento + distincao apostilamento x aditivo.

## 3. Distincao critica - aditivo vs apostilamento

| Criterio | **Termo aditivo** | **Apostilamento** |
|----------|-------------------|-------------------|
| **Natureza** | Alteracao substantiva | Anotacao acidental |
| **Base legal** | Art. 124 Lei 14.133 | Art. 136 Lei 14.133 |
| **Hipoteses** | Alteracao de objeto, valor, prazo, regime, clausulas, reequilibrio | Reajuste, atualizacao contratual, retificacao de erro material, mudanca de empenho |
| **Formalizacao** | Termo aditivo formal (assinatura) | Apostilamento simples (anotacao) |
| **Publicidade** | Publicacao no DOU/PNCP | Anotacao no contrato |
| **Aprovacao** | Autoridade superior | Gestor do contrato (geralmente) |
| **TCU red flag** | Apostilamento usado indevidamente para alteracao substantiva | - |

**Fronteira critica:** usar apostilamento para o que deveria ser aditivo = **vicio frequentemente impugnado pelo TCU**. Estrategia consultiva: orientar a formalizacao correta.

## 4. Limites de alteracao unilateral (art. 124 I)

- **Regra geral:** ate **25%** acrescimo ou supressao do valor inicial atualizado.
- **Reforma de edificio ou equipamento:** ate **50%** acrescimo.
- **Acima desses limites:** so com **anuencia do contratado** (alteracao bilateral); recusa do contratado nao gera sancao + indenizacao se houver prejuizo (art. 124 §3º analogica).
- **Compensacao da equacao:** alteracao quantitativa deve ser acompanhada de **revisao** quando altera o equilibrio (art. 124 §2º + CF art. 37 XXI).

### Estrategia defensiva do contratado:
1. **Recusar aditivo unilateral excessivo** (acima de 25%/50%) - direito ao **dialogo** com a Administracao.
2. Se Administracao impoe -> recusa formal + invocar art. 124 + ressalva de equilibrio.
3. Se Administracao rescinde unilateral por recusa -> defesa em `rescisao-contrato` (interesse publico + indenizacao - art. 138 + art. 137 §5º).

## 5. Alteracoes bilaterais comuns (art. 124 II)

### 5.1 - Substituicao de garantia (art. 124 II a)
- Modalidade de garantia trocada (caucao por seguro-garantia, p. ex.).
- Procedimento: aditivo simples + entrega da nova garantia + devolucao da anterior.

### 5.2 - Modificacao de regime de execucao (art. 124 II b)
- Empreitada global -> empreitada por unidade, p. ex.
- Procedimento: aditivo + justificativa + ressalva de impacto economico (revisao se cabivel).

### 5.3 - Modificacao de forma de pagamento (art. 124 II c)
- Cronograma de pagamento, parcelamento.
- **Vedacao:** alteracao que cause desequilibrio (art. 124 II c parte final) - garantia do contratado.

### 5.4 - Revisao (art. 124 II d + § 1º)
- Reequilibrio (objeto da skill `reequilibrio-economico-financeiro`); pode ser formalizado por aditivo.

### 5.5 - Prorrogacao
- Contratos contínuos: ate 60 meses (art. 107) ou ate 10 anos em hipoteses especificas com regulamento.
- Vantajosidade economica deve ser demonstrada na renovacao.

## 6. Apostilamento (art. 136) - 4 hipoteses

| Hipotese | Exemplo |
|---------|---------|
| Reajuste | Aplicacao do indice contratual (IPCA, INCC) anualmente |
| Atualizacao contratual | Mudanca de razao social do contratado; atualizacao de representante |
| Retificacao de erro material | Correcao de numero, data, valor sem alteracao do conteudo |
| Mudanca de empenho | Substituicao de empenho da fonte/exercicio orcamentario |

**Vicio TCU comum:** uso de apostilamento para alteracoes substantivas (mudanca de objeto, valor, prazo) - exige aditivo.

## 7. Output - Parecer (formato)

```
PARECER ALTERACAO CONTRATUAL - CASO [slug]
Contrato: [n° + objeto + valor inicial]
Data-base: [DD/MM/AAAA] · Selo: [referencia]

NECESSIDADE DA ALTERACAO:
- Motivo: [descricao]
- Natureza: [quantitativa / qualitativa / temporal / formal]

INSTRUMENTO CORRETO:
[ ] Apostilamento (art. 136) - quando: reajuste / atualizacao / retificacao
[ ] Termo aditivo (art. 124) - quando: alteracao substantiva
Justificativa da escolha: [vinculacao a hipotese legal]

LIMITES:
- Unilateral: 25% (50% reforma) - posicao atual: [%]
- Bilateral: anuencia do contratado - status: [obtida / pendente]

EQUACAO ECONOMICO-FINANCEIRA (CF art. 37 XXI):
- Impacto da alteracao: [%]
- Compensacao (revisao) cabivel: [sim / nao] - acionar `reequilibrio-economico-financeiro`

PRORROGACAO (se aplicavel):
- Limite: 60 meses regra art. 107
- Vantajosidade: [demonstrada / a demonstrar]

ESTRATEGIA:
- Aceitar / Recusar / Negociar revisao concomitante
- Riscos: [aditivo > 25% sem anuencia; apostilamento usado indevidamente]

[VERIFICAR]: [jurisprudencia TCU sobre apostilamento vs aditivo; IN SEGES]

---
[Ressalva OAB - PA-07]
```

## 8. Vedacoes especificas

- **PA-04** Selo. **PA-13** citacao precisa. **PA-15** vinculacao ao instrumento original.
- **PA-09** sigilo de valores e planilhas associadas.
- **PA-17** vedado opinar sobre escolha discricionaria da Administracao em ampliar/suprimir; apenas vicios de legalidade.
- **PA-07** ressalva OAB. **PA-11** jurisprudencia TCU recente -> `[VERIFICAR]`.

## 9. Protocolos acionados

- **P1** Selo. **P2** integridade do contrato + minuta de aditivo/apostilamento. **P3** memoria de quantum quando aplicavel. **P5** competencia.

## 10. Localizacao

Federal -> TCU paradigma + IN SEGES 73/2022. Estadual/municipal -> TCE/TCM + regulamento local. Estatal -> regulamento interno.

## 11. Integracao

**Chamada por:** `licitacoes-master`, `contrato-administrativo`, `reequilibrio-economico-financeiro`, `gestao-cronograma-fiscalizacao`.

**Entrega para:** parecer + minuta + `CASO.md`. Aciona `reequilibrio-economico-financeiro` se cabe revisao paralela. Se aditivo abusivo -> `recurso-administrativo` ou `representacao-tcu-tce` (P4). Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** apostilamento usado para alteracao substantiva (vicio TCU); aditivo unilateral acima de 25% sem ressalva (perda de equilibrio); prorrogacao sem demonstracao de vantajosidade (vicio impugnavel).
