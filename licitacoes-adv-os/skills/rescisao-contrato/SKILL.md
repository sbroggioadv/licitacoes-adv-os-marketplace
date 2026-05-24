---
name: rescisao-contrato
description: >
  Rescisao do contrato administrativo (arts. 137-139 Lei 14.133/2021). 4 hipoteses: (1) POR INADIMPLEMENTO DA CONTRATADA art. 137 I-XII (atraso, descumprimento, dolo, etc.) - defesa do contratado em rito sancionatorio; (2) POR INADIMPLEMENTO DA ADMINISTRACAO art. 137 §4º - atraso de pagamento >90 dias da direito da contratada a rescisao + indenizacao integral; (3) POR INTERESSE PUBLICO art. 137 §5º - indenizacao do contratado de boa-fé; (4) POR FORCA MAIOR/CASO FORTUITO art. 137 IX. Efeitos: devolucao de garantia, pagamento de obras/servicos executados, indenizacao cabivel (art. 138). Estrategia: rescisao por inadimplemento da Administracao com cobranca cumulada (P4 - via judicial). Aciona: rescisao contratual, art. 137, atraso de pagamento 90 dias, inadimplemento Administracao, interesse publico, distrato, indenizacao por rescisao.
---

# RESCISAO DO CONTRATO ADMINISTRATIVO

> Skill **Tier 4** - rescisao em 4 hipoteses (arts. 137-139 Lei 14.133/2021). Foco na defesa do contratado e na rescisao por inadimplemento da Administracao. Implementa P1, P2, P3, P4, P5, P6; respeita PA-15, PA-13, PA-09.

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `contrato-administrativo`, `gestao-cronograma-fiscalizacao` (apos notificacao de inadimplemento), ou diretamente em demanda de rescisao. Recebe: contrato + historico de execucao + atos relevantes (notificacoes, atrasos, decisao da Administracao).

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `contrato-administrativo`, `gestao-cronograma-fiscalizacao`, `defesa-apenamento-art-156` (interface com sancao).
- **Pre-requisito:** Selo (PA-04); contrato + provas documentais.
- **Aciona em sequencia:** `acao-cobranca-administracao` (rescisao por inadimplemento da Administracao -> cobranca em paralelo P4); `acao-anulatoria-licitacao` (anulacao do ato rescisorio se ilegal); `ms-licitacao-contrato` (urgencia para suspender efeitos).
- **Entrega para:** peca defensiva (se rescisao por inadimplemento da contratada) OU peca proativa (se inadimplemento da Administracao art. 137 §4º).

## 2. Marco normativo

- **Lei 14.133/2021:**
  - **art. 137** - hipoteses de rescisao:
    - **I-XII** - **inadimplemento da contratada** (atraso reiterado, descumprimento, sub-rogacao indevida, paralisacao, fraude, irregularidade fiscal nao sanada, etc.).
    - **IX** - caso fortuito ou forca maior (sem culpa).
    - **§4º** - **atraso de pagamento superior a 90 dias** da direito da contratada a rescindir.
    - **§5º** - **rescisao por interesse publico** com **indenizacao integral** do contratado de boa-fé (custos + lucros cessantes razoaveis + danos diretos).
  - **art. 138** - **efeitos da rescisao**: devolucao de garantia (proporcional ao executado); pagamento de obras/servicos executados; indenizacao cabivel; transferencia de bens (em certos casos).
  - **art. 139** - rito procedimental da rescisao.
  - **art. 158** - rito sancionatorio (interface quando rescisao com penalidade).
  - **art. 156** - sancoes (advertencia, multa, impedimento, inidoneidade).
- **CF art. 5º LV** - ampla defesa.
- **CF art. 37 §6º** - responsabilidade objetiva da Administracao.
- **Lei 9.784/1999** - processo administrativo federal (subsidiaria).
- **CC arts. 421-422** - boa-fé objetiva.
- **Sumulas TCU:** jurisprudencia sobre rescisao por interesse publico + indenizacao.

## 3. As 4 hipoteses de rescisao

### 3.1 - Rescisao por inadimplemento da CONTRATADA (art. 137 I-XII)

**Defesa do contratado:**
- **Rito procedimental** (art. 139 + art. 158): notificacao + prazo de defesa + decisao motivada (Lei 9.784).
- **Ampla defesa** (CF art. 5º LV) - peca defensiva com:
  - Refutacao especifica de cada acusacao.
  - Demonstracao de cumprimento (ou de causa nao imputavel).
  - Invocacao de fato da Administracao quando aplicavel (atraso de projeto, demora em fiscalizacao, alteracao do local - PA-15 vinculacao ao edital).
  - Caso fortuito / forca maior (art. 137 IX) quando aplicavel.
- **Coordenacao com sancao** (art. 156) - rescisao + sancao = duplicidade defensiva (`defesa-apenamento-art-156`).
- **Recurso administrativo** apos decisao rescisoria (interface com `recurso-administrativo`).

### 3.2 - Rescisao por inadimplemento da ADMINISTRACAO (art. 137 §4º)

**Direito da contratada:** atraso de pagamento superior a **90 dias** da direito a rescindir + indenizacao.

**Estrategia proativa:**
1. **Documentar o atraso:** notificacoes formais a cada vencimento nao pago (`gestao-cronograma-fiscalizacao` - preservacao de prova).
2. **Apos 90 dias:** peca formal de rescisao com fundamentacao no art. 137 §4º + cobranca dos valores em atraso.
3. **Cobranca cumulativa** (`acao-cobranca-administracao`) - Tema 905 STJ (Selic combinada) + ordem cronologica (art. 141).
4. **Indenizacao por lucros cessantes** se a rescisao causa prejuizo direto.

### 3.3 - Rescisao por INTERESSE PUBLICO (art. 137 §5º)

**Direito da contratada:**
- **Indenizacao integral** do contratado de boa-fé: custos incorridos + lucros cessantes razoaveis + danos diretos.
- **Devolucao de garantia** integral (art. 138).
- **Pagamento de obras/servicos executados** ate a rescisao.

**Estrategia:**
1. **Memoria de quantum** (P3) com tabela auditavel: custos + investimentos + lucros cessantes razoaveis + Selic.
2. **Pedido administrativo de indenizacao** ate o orgao licitante.
3. **Se denegado** -> `acao-cobranca-administracao` (judicial - Tema 905 STJ).

### 3.4 - Rescisao por CASO FORTUITO / FORCA MAIOR (art. 137 IX)

**Caracterizacao:** evento inevitavel e imprevisivel (CC art. 393); paralisia generalizada por pandemia, desastre natural, ato de guerra.

**Efeitos:**
- Rescisao sem culpa de qualquer das partes.
- Pagamento do executado + devolucao de garantia.
- Sem indenizacao por lucros cessantes (regra), salvo previsao especifica.

## 4. Estrutura - Peca de rescisao por inadimplemento da Administracao (art. 137 §4º)

```
EXMO. [AUTORIDADE COMPETENTE / GESTOR DO CONTRATO]
PROCESSO ADMINISTRATIVO N° [n°]
CONTRATO N° [n°] - EDITAL N° [n°]

REQUERIMENTO DE RESCISAO POR INADIMPLEMENTO DA ADMINISTRACAO
(art. 137 §4º Lei 14.133/2021)

I - QUALIFICACAO E LEGITIMIDADE
[Razao social - CNPJ - contratada do contrato n° X]

II - DOS FATOS
- Contrato n° X assinado em [DD/MM/AAAA]
- Cronograma de pagamento previsto: [tabela]
- Atrasos verificados:
  | Parcela | Valor | Vencimento | Status (DD/MM/AAAA) |
  | 5/12    | R$ X  | DD/MM      | atrasada DD dias    |
  | ...     | ...   | ...        | ...                  |
- Notificacoes formais enviadas em [DD/MM, DD/MM, DD/MM]
- Atraso medio supera 90 dias - configura art. 137 §4º Lei 14.133

III - DO DIREITO
- **Art. 137 §4º Lei 14.133/2021** - atraso superior a 90 dias -> direito a rescindir
- Art. 141 Lei 14.133 - ordem cronologica de pagamentos (quebrada)
- CF art. 37 XXI - manutencao da equacao
- CC arts. 421-422 - boa-fé objetiva (quebrada pela Administracao)

IV - DA MEMORIA DE QUANTUM (P3)
| Item | Base legal | Valor |
| Parcelas em atraso + Selic Tema 905 STJ | art. 141 | R$ X |
| Lucros cessantes pelo restante do contrato | art. 138 + art. 137 §4º analogia §5º | R$ Y |
| Devolucao de garantia | art. 138 | R$ Z |
| Total pleiteado | - | R$ TOTAL |

V - DOS PEDIDOS
a) Acolhimento do requerimento de rescisao pelo inadimplemento da Administracao;
b) Pagamento integral dos valores em atraso + Selic (Tema 905 STJ);
c) Indenizacao por lucros cessantes razoaveis;
d) Devolucao da garantia integral;
e) Em caso de denegacao -> reserva de via judicial (`acao-cobranca-administracao`).

VI - DOCUMENTOS
- Contrato + cronograma
- Notificacoes formais de cada atraso
- Memoria de quantum
- Procuracao OAB ativa (PA-05, PA-07)

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}} - OAB/{{OAB_UF}} {{OAB_NUMERO}}

---
[Ressalva OAB - PA-07]
```

## 5. Estrutura - Peca defensiva (rescisao por inadimplemento da contratada)

```
EXMO. [AUTORIDADE]
PROCESSO ADMINISTRATIVO N° [n°]

DEFESA EM PROCESSO DE RESCISAO
(arts. 137 + 139 + 158 Lei 14.133/2021 + CF art. 5º LV)

I - PRELIMINAR DE TEMPESTIVIDADE E AMPLA DEFESA
[...]

II - REFUTACAO DOS FATOS IMPUTADOS
- Imputacao 1: [...]
  Refutacao: [demonstracao de cumprimento ou de causa nao imputavel]
  Documento: [...]
- Imputacao 2: [...]

III - DAS CAUSAS NAO IMPUTAVEIS
- Fato da Administracao: [atraso de projeto, demora em fiscalizacao, alteracao]
- Caso fortuito / forca maior (CC art. 393 + art. 137 IX Lei 14.133)

IV - DA AUSENCIA DE DOLO OU CULPA GRAVE
[CC art. 422 - boa-fé objetiva; CF art. 5º XXXVI - irretroatividade]

V - DA EVENTUAL DOSIMETRIA (se aplicavel interface com art. 156)
[Proporcionalidade; atenuantes]

VI - DOS PEDIDOS
a) Acolhimento da defesa;
b) Improcedencia do processo de rescisao;
c) Subsidiariamente, rescisao bilateral sem culpa + pagamento do executado.

[Ressalva OAB - PA-07]
```

## 6. Vedacoes especificas

- **PA-04** Selo. **PA-13** citacao precisa. **PA-15** vinculacao ao instrumento (clausulas e prazos contratuais).
- **PA-09** sigilo de valores e dados internos.
- **PA-02** vedada promessa.
- **PA-07** ressalva OAB. **PA-08** sem critica pessoal a fiscal/gestor.
- **PA-12** independencia relativa das esferas - rescisao administrativa + cobranca judicial sao vias distintas.

## 7. Protocolos acionados

- **P1** Selo. **P2** integridade do contrato + provas. **P3** memoria de quantum. **P4** coordenacao com judicial. **P5** competencia (administrativa primeiro; judicial paralelo). **P6** R1-R4.

## 8. Localizacao

Federal -> orgao + TCU + JF (Vara da Fazenda Publica). Estadual/municipal -> orgao + TCE/TCM + JE local.

## 9. Integracao

**Chamada por:** `licitacoes-master`, `contrato-administrativo`, `gestao-cronograma-fiscalizacao`, `defesa-apenamento-art-156`.

**Entrega para:** peca + memoria + `CASO.md`. Aciona `acao-cobranca-administracao` (cobranca cumulada se atraso da Administracao); `acao-anulatoria-licitacao` (se rescisao ilegal); `ms-licitacao-contrato` (urgencia). Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** rescisao por inadimplemento da contratada sem defesa estruturada (perda + sancao); ou contratada absorve atraso da Administracao acima de 90 dias sem exercer o direito de rescindir + cobrar.
