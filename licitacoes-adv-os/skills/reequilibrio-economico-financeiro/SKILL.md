---
name: reequilibrio-economico-financeiro
description: >
  Pedido de reequilibrio economico-financeiro (arts. 124-125 Lei 14.133/2021). 3 especies: REVISAO (alea economica extraordinaria e extracontratual, fato do principe, fato da Administracao - art. 124 §1º); REAJUSTE (indices contratuais pre-fixados - IPCA, INCC, INPC); REPACTUACAO (mao-de-obra exclusiva - IN SEGES MP 5/2017 art. 53 residual). Requisitos: fato superveniente + imprevisivel ou previsivel mas de consequencias incalculaveis + nexo causal. Planilha demonstrativa do impacto economico (P3 - memoria de quantum auditavel; Tema 905 STJ Selic combinada). Jurisprudencia TCU 2020-2024 (pandemia + inflacao 2022-2023). Pedido administrativo previo (preservacao de prova) + acao judicial se denegado (CF art. 5º XXXV; CF art. 37 XXI - equacao economico-financeira). Aciona: reequilibrio, revisao contratual, reajuste, repactuacao, alea extraordinaria, fato do principe, fato da Administracao, art. 124, art. 125.
---

# REEQUILIBRIO ECONOMICO-FINANCEIRO

> Skill **Tier 4** - pedido de reequilibrio (arts. 124-125 Lei 14.133/2021). 3 especies. Base constitucional: **CF art. 37 XXI** (manutencao da equacao). Implementa P1, P2, P3, P4, P5, P6; respeita PA-15 (vinculacao), PA-13 (citacao), PA-09 (sigilo da planilha).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `contrato-administrativo`, ou demanda direta quando ha **desequilibrio** durante a execucao. Recebe: contrato + matriz de risco + dados financeiros da PJ (PA-09 sigilo) + comprovacao do fato superveniente. Entrega: pedido administrativo de reequilibrio + memoria de quantum + estrategia de via paralela (P4).

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `contrato-administrativo`, `analise-matriz-risco`, `gestao-cronograma-fiscalizacao` (quando notifica fato superveniente), `aditivo-contratual` (se reequilibrio gera aditivo).
- **Pre-requisito:** Selo (PA-04); contrato + matriz de risco mapeada; comprovacao do fato; planilha demonstrativa (P3).
- **Aciona em sequencia:** `revisao-final-licitacoes` antes da entrega; se negado -> `ms-licitacao-contrato` ou `acao-anulatoria-licitacao` (P4) + `representacao-tcu-tce`.
- **Entrega para:** operador (peca administrativa + memoria de quantum + roteiro judicial).

## 2. Marco normativo

- **Lei 14.133/2021:**
  - **arts. 124-125** - reequilibrio.
  - **art. 124 §1º** - **revisao** para preservar equacao quando fato superveniente, imprevisivel ou previsivel mas de consequencias incalculaveis, com nexo causal.
  - **art. 124 II d** - **reajuste por indice** previsto em edital/contrato.
  - **art. 124 II c** - **repactuacao** para mao-de-obra exclusiva.
  - **art. 25** - vinculacao ao edital.
  - **art. 22** - matriz de risco (base para reequilibrio).
- **CF art. 37 XXI** - manutencao da equacao economico-financeira como direito constitucional do contratado.
- **CC arts. 421-422, 478** - boa-fé objetiva + teoria da imprevisao.
- **IN SEGES MP 5/2017 art. 53** - repactuacao de mao-de-obra exclusiva (residual aplicavel a contratos sob Lei 14.133 conforme regulamento).
- **Tema 905 STJ** - Selic combinada para condenacoes contra Fazenda (juros + correcao).
- **Jurisprudencia TCU 2020-2024** - pandemia + inflacao 2022-2023 (referenciar com `[VERIFICAR - decisoes TCU 2024-2026]`).

## 3. Tres especies de reequilibrio

| Especie | Hipotese | Indice | Requisitos |
|---------|----------|--------|------------|
| **Revisao** (art. 124 §1º) | Fato superveniente imprevisivel/incalculavel + nexo causal: pandemia, inflacao excepcional, fato do principe, fato da Administracao | Variacao real demonstrada na planilha | Imprevisibilidade ou incalculabilidade + nexo + impacto economico relevante |
| **Reajuste** (art. 124 II d) | Decurso de tempo conforme periodicidade do contrato | Indice contratual (IPCA, INCC, INPC) | Periodicidade (anual regra) + indice especificado |
| **Repactuacao** (art. 124 II c + IN SEGES MP 5/2017) | Mao-de-obra exclusiva - convencao coletiva + dissidio | Variacao real de salarios + encargos | Anual + comprovacao por CCT/Dissidio |

## 4. Estrutura canonica - Pedido administrativo de revisao

```
EXMO. [AUTORIDADE COMPETENTE - GESTOR DO CONTRATO / AUTORIDADE SUPERIOR]
PROCESSO ADMINISTRATIVO N° [n°]
CONTRATO N° [n°] - EDITAL N° [n°] - OBJETO: [...]

PEDIDO DE REVISAO CONTRATUAL
(art. 124 §1º Lei 14.133/2021)

I - QUALIFICACAO E LEGITIMIDADE
[Razao social - CNPJ - representante legal - contratada do contrato n° X]

II - DOS FATOS
- Contrato assinado em [DD/MM/AAAA] no valor de R$ [V]
- Em [DD/MM/AAAA] ocorreu o fato superveniente: [descricao - pandemia, alta excepcional
  de insumo X, fato do principe Y, fato da Administracao Z]
- Impacto economico no contrato: [demonstracao na planilha anexa]
- Nexo causal: [vinculo entre fato e desequilibrio]

III - DOS FUNDAMENTOS DE DIREITO

III.1 - CF art. 37 XXI - manutencao da equacao economico-financeira
III.2 - **Lei 14.133/2021 art. 124 §1º** - revisao por fato superveniente
       (imprevisivel ou de consequencias incalculaveis)
III.3 - Lei 14.133/2021 art. 25 - vinculacao ao edital (matriz de risco
       no instrumento previa este tipo de risco como alea extraordinaria
       compartilhada / nao previa - PA-15)
III.4 - CC arts. 421-422, 478 - boa-fé objetiva + teoria da imprevisao
III.5 - Jurisprudencia TCU em casos analogos (2020-2024 - pandemia/inflacao)
       [referenciar com cautela - PA-11 [VERIFICAR]]

IV - DA MEMORIA DE QUANTUM (P3)
| Item | Base legal | Valor original | Variacao | Total revisado |
| Insumo X | art. 124 §1º + comprovante de mercado | R$ A | +Y% | R$ B |
| Mao-de-obra | CCT 2024 (anexo) | R$ C | +Z% | R$ D |
| Total | - | R$ E | +W% | R$ F |

Atualizacao: Selic acumulada desde [data] - Tema 905 STJ.

V - DOS PEDIDOS
a) Acolhimento do pedido de revisao;
b) Recomposicao do equilibrio economico-financeiro com aplicacao do novo
   valor R$ [F] a partir de [data];
c) Pagamento dos atrasados desde [data] com Selic (Tema 905 STJ);
d) Subsidiariamente, repactuacao/reajuste no que couber.

VI - DOCUMENTOS
- Contrato n° [n°]
- Planilha demonstrativa (P3)
- Comprovantes do fato superveniente (notas, indices oficiais, CCT)
- Procuracao OAB ativa (PA-05, PA-07)

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}} - OAB/{{OAB_UF}} {{OAB_NUMERO}}

---
[Ressalva OAB - PA-07]
```

## 5. Memoria de quantum (P3) - tabela auditavel

| Componente | Base legal | Valor original | Variacao | Total revisado |
|-----------|-----------|---------------|----------|----------------|
| Insumo X (material) | art. 124 §1º + cotacoes | R$ A | +Y% | R$ B |
| Mao-de-obra | CCT/Dissidio (anexo) | R$ C | +Z% | R$ D |
| Encargos sociais | conforme legislacao | R$ E | +W% | R$ F |
| BDI | matriz contratual | R$ G | mantida | R$ G |
| **Total revisado** | - | R$ ORIG | +%TOTAL | **R$ FINAL** |

**Atualizacao financeira:** Selic acumulada desde a exigibilidade - **Tema 905 STJ** (Selic combinada = juros + correcao).

**Origem dos dados:** PA-22 - dados reais do caso; nao presumir; nao inflar.

## 6. Coordenacao P4 - via paralela

**Se pedido administrativo negado:**
1. **Acao anulatoria do ato denegatorio** (`acao-anulatoria-licitacao`) - CPC + tutela de urgencia.
2. **Acao de cobranca cumulativa** (`acao-cobranca-administracao`) - valor revisado + Tema 905 STJ.
3. **Representacao ao TCU/TCE** (`representacao-tcu-tce`) - se houve violacao a principios da Administracao Publica (CF art. 37) ou descumprimento de jurisprudencia consolidada.

**Provas cruzadas:** contrato + planilha + comprovantes + decisao denegatoria reusam-se em todas as vias.

## 7. Vedacoes especificas

- **PA-04** Selo. **PA-13** citacao precisa. **PA-15** vinculacao a matriz contratual.
- **PA-09** sigilo de planilha de custos (em `<cwd>/.../casos/<slug>/arquivos/`).
- **PA-02** vedada promessa de provimento.
- **PA-11** decisoes TCU 2020-2024 -> `[VERIFICAR]`.
- **PA-07** ressalva OAB.
- **PA-14** onus da contratada em comprovar nexo + impacto; nao se inverte automaticamente.

## 8. Protocolos acionados

- **P1** Selo. **P2** integridade do contrato + matriz + planilha + comprovantes. **P3** memoria de quantum. **P4** coordenacao se negado. **P5** competencia (administrativa primeiro; judicial paralelo). **P6** R1-R4.

## 9. Localizacao

Federal -> orgao licitante + TCU paradigma. Estadual/municipal -> orgao + TCE/TCM. Estatal -> regulamento interno (Lei 13.303). Judicial subsequente: JF/JE conforme esfera.

## 10. Integracao

**Chamada por:** `licitacoes-master`, `contrato-administrativo`, `analise-matriz-risco`, `gestao-cronograma-fiscalizacao`, `aditivo-contratual`.

**Entrega para:** operador (pedido administrativo + memoria de quantum + roteiro judicial se denegado) + `CASO.md`. Se denegado -> acoes paralelas (P4). Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** contratada absorve desequilibrio (prejuizo); ou pleiteia sem base tecnica (denegacao certa); perde oportunidade de Tema 905 STJ na cobranca subsequente.
