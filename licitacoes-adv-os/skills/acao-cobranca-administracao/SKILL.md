---
name: acao-cobranca-administracao
description: >
  Acao de cobranca de pagamento atrasado contra a Administracao (CPC). Preservacao da ORDEM CRONOLOGICA de pagamentos (art. 141 Lei 14.133/2021 - principio). JUROS DE MORA (Selic) e correcao monetaria - TEMA 905 STJ (Selic combinada para condenacoes contra Fazenda Publica). PRECATORIO ou RPV (CF art. 100 - RPV ate 60 salarios-minimos no federal; valores variaveis em Estados/Municipios). Inviabilidade de penhora de bem publico (CPC art. 833). Rito ordinario x execucao de TITULO EXECUTIVO EXTRAJUDICIAL (contrato administrativo - CPC art. 784 III). Prescricao quinquenal contra Fazenda (Decreto 20.910/1932). Aciona: cobranca contra Administracao, art. 141, ordem cronologica, Tema 905 STJ, precatorio, RPV, contrato como titulo executivo, atraso de pagamento, indenizacao.
---

# ACAO DE COBRANCA CONTRA ADMINISTRACAO

> Skill **Tier 6** - cobranca de pagamento atrasado + indenizacoes contra a Fazenda Publica. CPC + Decreto 20.910/1932. Tema 905 STJ. Implementa P1, P2, P3, P4, P5, P6; respeita PA-13, PA-15, PA-20 (prescricao).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `/judicial`, `rescisao-contrato` (cobranca cumulada apos rescisao por inadimplemento da Administracao - art. 137 §4º), `acao-anulatoria-licitacao` (cumulacao com indenizacao art. 149), `reequilibrio-economico-financeiro` (cobranca de valores nao acolhidos administrativamente).

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/judicial`, `rescisao-contrato`, `acao-anulatoria-licitacao`, `reequilibrio-economico-financeiro`, `gestao-cronograma-fiscalizacao`.
- **Pre-requisito:** Selo (PA-04); contrato + provas de pagamento devido + notificacoes formais previas (preservadas por `gestao-cronograma-fiscalizacao`); analise de prescricao.
- **Aciona em sequencia:** `revisao-final-licitacoes`; eventual representacao TCU sobre quebra da ordem cronologica (P4).
- **Entrega para:** peticao inicial + memoria de quantum + roteiro de execucao.

## 2. Marco normativo

- **CPC:**
  - **arts. 318-322** - procedimento comum (acao de cobranca).
  - **art. 300** - tutela de urgencia (cumulavel quando urgencia financeira).
  - **arts. 783-805** - execucao por titulo extrajudicial.
  - **art. 784 III** - **contrato administrativo como TITULO EXECUTIVO EXTRAJUDICIAL** (somente se liquido, certo e exigivel).
  - **art. 798** - cautelar em geral.
  - **art. 833 IX** - **bens publicos sao impenhoraveis**.
  - **art. 910** - execucao contra a Fazenda Publica - rito proprio (precatorio/RPV).
- **CF:**
  - **art. 5º XXXV** - inafastabilidade da jurisdicao.
  - **art. 5º XXXVI** - irretroatividade.
  - **art. 100** - **regime de precatorios/RPV** para pagamento pela Fazenda.
- **Lei 14.133/2021:**
  - **art. 141** - **ordem cronologica de pagamentos** (principio - cada exercicio + cada fonte; quebra = vicio).
  - **art. 137 §4º** - atraso >90 dias da direito a rescisao + cobranca.
  - **art. 148** - efeitos da nulidade.
  - **art. 149** - indenizacao do contratado de boa-fé.
- **Decreto 20.910/1932 art. 1º** - **prescricao quinquenal** das pretensoes contra a Fazenda Publica federal, estadual e municipal.
- **Lei 4.320/1964** - ordem cronologica + exercicio orcamentario.
- **CC arts. 421-422** - boa-fé.
- **CC art. 944** - obrigacao de indenizar pelo dano efetivo.
- **Tema 905 STJ** - **Selic combinada** (juros + correcao) para condenacoes contra Fazenda Publica.
- **Sumulas STJ:** Sum. 188 STJ (correcao monetaria em contrato administrativo); jurisprudencia consolidada sobre precatorios.

## 3. Hipoteses de cobranca

| Hipotese | Base legal | Acao |
|----------|-----------|------|
| Pagamento de parcelas em atraso | art. 141 Lei 14.133 + CC art. 422 | Cobranca + Selic |
| Indenizacao por rescisao por inadimplemento da Administracao | art. 137 §4º + §5º | Lucros cessantes + custos + Selic |
| Indenizacao por anulacao do contrato (contratado de boa-fé) | art. 149 Lei 14.133 | Custos + lucros cessantes razoaveis + Selic |
| Reequilibrio negado | art. 124 §1º + CF art. 37 XXI | Valor revisado + Selic |
| Garantia indevidamente retida | arts. 96-100 Lei 14.133 | Valor da garantia + correcao |

## 4. Titulo executivo extrajudicial (CPC art. 784 III)

**Contrato administrativo** como **titulo executivo extrajudicial** - quando preenche:
- **Liquido** (valor determinado).
- **Certo** (existencia indubitavel).
- **Exigivel** (vencido e nao pago).

**Vantagem:** rito de **execucao** (mais rapido) em vez de **procedimento comum** (instrucao + sentenca + execucao).

**Quando aplicavel:** parcelas de pagamento ja faturadas e atestadas (sem controversia sobre o valor), apenas o pagamento atrasou.

## 5. Estrutura canonica - peticao inicial (cobranca)

```
EXMO. JUIZ FEDERAL [OU DA VARA DA FAZENDA PUBLICA]

[Razao social da Autora] - CNPJ - representada por [advogado OAB ativo]

ACAO DE COBRANCA COM PEDIDO DE TUTELA DE URGENCIA
em face de [UNIAO / Estado / Municipio / Autarquia / Estatal] - CNPJ

I - DOS FATOS
- [Contrato n° X - assinado em DD/MM/AAAA - valor R$ Y]
- [Parcelas em atraso conforme tabela abaixo]
- [Notificacoes formais protocoladas em DD/MM, DD/MM, DD/MM - sem resposta
  ou com resposta evasiva]
- [Quebra da ordem cronologica (art. 141 Lei 14.133) - se aplicavel]

II - DA TEMPESTIVIDADE
Prazo prescricional de 5 anos (Decreto 20.910/1932 art. 1º).
- Vencimento mais antigo: [DD/MM/AAAA]
- Demanda ajuizada em [DD/MM/AAAA] - dentro do prazo.

III - DA COMPETENCIA E LEGITIMIDADE
[JF (CF art. 109 I) se Uniao; JE Vara da Fazenda local se Estado/Municipio]

IV - DO DEVER DE PAGAMENTO
- Contrato n° X (art. 92 Lei 14.133) - clausulas vinculam (PA-15);
- Parcelas faturadas e atestadas pela Administracao (notas/documentos anexos);
- Quebra do dever de pagamento + ordem cronologica (art. 141 Lei 14.133);
- Boa-fé objetiva (CC art. 422) violada pela Administracao.

V - DA MEMORIA DE QUANTUM (P3)

| Parcela | Vencimento | Valor original | Selic acumulada | Total |
| 5/12    | DD/MM      | R$ A           | desde DD/MM     | R$ B  |
| 6/12    | DD/MM      | R$ C           | desde DD/MM     | R$ D  |
| [...]                                                        |
| **Subtotal parcelas em atraso**                  | R$ X |

Atualizacao: **Tema 905 STJ** - Selic combinada (juros + correcao) desde a
exigibilidade de cada parcela.

Eventual indenizacao por lucros cessantes (se rescisao por inadimplemento da
Administracao art. 137 §4º): R$ Y

**Total pleiteado: R$ TOTAL**

VI - DA TUTELA DE URGENCIA (quando aplicavel - CPC art. 300)
[Quando urgencia financeira concreta - empresa em dificuldade pela ausencia
de pagamento + risco de continuidade]
- Fumus: contrato + atestos + notas + notificacoes
- Periculum: prejuizo concreto pela falta de receita

VII - DOS PEDIDOS

a) Citacao da Re;
b) Procedencia da acao com condenacao da Re ao pagamento de:
   - Valores em atraso conforme memoria de quantum (R$ X)
   - Atualizacao pela Selic (Tema 905 STJ)
   - Eventual indenizacao por lucros cessantes (R$ Y - quando rescisao por
     art. 137 §4º)
   - Total: **R$ TOTAL**
c) Honorarios advocaticios (CPC art. 85);
d) Custas processuais;
e) Em sentenca, observancia do regime de precatorio/RPV (CF art. 100).

VIII - DO VALOR DA CAUSA
R$ [TOTAL pleiteado]

IX - DOCUMENTOS
- Procuracao OAB ativa (PA-05, PA-07)
- Contrato + aditivos
- Notas fiscais + atestos pelo fiscal/gestor
- Notificacoes formais previas
- Memoria detalhada de quantum
- Eventual representacao TCU sobre quebra da ordem cronologica

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}} - OAB/{{OAB_UF}} {{OAB_NUMERO}}

---
[Ressalva OAB - PA-07]
```

## 6. Precatorio x RPV (CF art. 100)

| Modalidade | Limite | Prazo de pagamento |
|-----------|--------|---------------------|
| **Precatorio** | Acima do limite RPV | Exercicio orcamentario seguinte (regra) + fila cronologica |
| **RPV (Requisicao de Pequeno Valor)** | Federal: ate **60 salarios-minimos** | 60 dias da requisicao |
| RPV estadual/municipal | Variavel por ente (lei propria) - geralmente menores | conforme regulamento |

**Estrategia:** quando o valor permite, fracionar com fundamento? **NAO** - vedacao constitucional (CF art. 100 §8º - vedacao de fracionamento de valor de execucao).

## 7. Execucao por titulo extrajudicial (contrato como CPC art. 784 III)

**Quando aplicavel:**
- Parcelas faturadas e atestadas sem controversia.
- Valor liquido + certo + exigivel.

**Estrutura:**
1. Acao de execucao (CPC arts. 783+).
2. Citacao para pagar em 3 dias (CPC art. 829).
3. Penhora **impossivel sobre bens publicos** (CPC art. 833 IX).
4. Conversao em rito de **precatorio/RPV** (CPC art. 910 + CF art. 100).

**Vantagem:** sem instrucao probatoria complexa; mais celere que o procedimento comum.

## 8. Coordenacao P4

- **Representacao ao TCU** (`representacao-tcu-tce`) sobre **quebra da ordem cronologica** (art. 141 Lei 14.133) - paralelo a cobranca judicial.
- **MS** (`ms-licitacao-contrato`) se ha ato coator individualizado em demora (raro - cobranca e ordinaria).
- **Acao anulatoria** (`acao-anulatoria-licitacao`) cumulativa se ha tambem vicio do contrato e indenizacao art. 149.

## 9. Vedacoes especificas

- **PA-04** Selo. **PA-13** citacao precisa. **PA-15** contrato como expressao da vinculacao ao edital.
- **PA-02** vedada promessa de procedencia/pagamento.
- **PA-09** sigilo de valores e dados internos.
- **PA-07** ressalva OAB. **PA-08** sem critica pessoal.
- **PA-20** **prescricao rigorosa** - 5 anos do vencimento de cada parcela.

## 10. Protocolos acionados

- **P1** Selo. **P2** integridade contrato + notas + atestos. **P3** memoria de quantum auditavel (Tema 905). **P4** coordenacao com TCU. **P5** competencia (JF/JE). **P6** R1-R4.

## 11. Localizacao

Uniao + autarquias federais -> JF. Estados/Municipios -> JE Vara da Fazenda Publica local. Precatorio - regra geral CF art. 100; valores de RPV estaduais/municipais variaveis.

## 12. Integracao

**Chamada por:** `licitacoes-master`, `/judicial`, `rescisao-contrato`, `acao-anulatoria-licitacao`, `reequilibrio-economico-financeiro`, `gestao-cronograma-fiscalizacao`.

**Entrega para:** peticao + memoria + `CASO.md`. Paralelo a `representacao-tcu-tce` (ordem cronologica). Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** contratada absorve atraso da Administracao + perde valores por prescricao (5 anos); ou pleiteia sem Tema 905 STJ (subutilizacao da Selic combinada).
