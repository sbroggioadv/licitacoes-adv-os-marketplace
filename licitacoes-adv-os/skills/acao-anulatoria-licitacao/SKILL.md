---
name: acao-anulatoria-licitacao
description: >
  Acao anulatoria do procedimento licitatorio ou do contrato (CPC procedimento comum). CAUSA DE PEDIR: vicio de legalidade, vicio de competencia, vicio de forma, vicio de motivacao, desvio de finalidade, ofensa a vinculacao ao instrumento convocatorio (PA-15). EFEITOS DA ANULACAO (art. 149 Lei 14.133/2021): indenizacao do contratado de BOA-FE (custos + lucros cessantes razoaveis + danos diretos); recuperacao de prestacao; impossibilidade de retorno ao status quo ante quando contrato ja executado. TUTELA DE URGENCIA (CPC art. 300 - fumus + periculum). Coordenacao com MS quando ha ato coator individualizado. Prescricao quinquenal (Decreto 20.910/1932). Aciona: acao anulatoria, anular procedimento, anular contrato, vicio de legalidade, art. 149 Lei 14.133, indenizacao do contratado de boa-fé, tutela de urgencia.
---

# ACAO ANULATORIA DE LICITACAO E CONTRATO

> Skill **Tier 6** - acao judicial ordinaria para anular procedimento licitatorio ou contrato. CPC procedimento comum. Prazo quinquenal contra Fazenda (Decreto 20.910/1932). Implementa P1, P2, P3, P4, P5, P6; respeita PA-13, PA-15, PA-17.

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `/judicial`, quando MS nao e cabivel (sem ato coator individualizado, ou prazo de 120 dias decorrido, ou complexidade fatica que demanda instrucao). Recebe: procedimento/contrato impugnado + provas + analise de tutela de urgencia.

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/judicial`, `representacao-tcu-tce` (alternativa/cumulativa), `ms-licitacao-contrato` (quando MS inadequado), `rescisao-contrato`, `defesa-apenamento-art-156`.
- **Pre-requisito:** Selo (PA-04); ato impugnavel + fundamentacao + analise de prescricao.
- **Aciona em sequencia:** `revisao-final-licitacoes`; paralelo a `representacao-tcu-tce`; cumulacao com `acao-cobranca-administracao` (indenizacao).
- **Entrega para:** peticao inicial + tutela de urgencia + roteiro processual.

## 2. Marco normativo

- **CPC:**
  - **arts. 318-322** - procedimento comum.
  - **art. 300** - tutela de urgencia (fumus + periculum + reversibilidade).
  - **art. 311** - tutela de evidencia.
  - **art. 798** - cautelar em geral.
- **Lei 14.133/2021:**
  - **art. 71** - homologacao/adjudicacao.
  - **art. 88** - anulacao do procedimento.
  - **art. 89** - assinatura/vinculacao.
  - **art. 124** - alteracao.
  - **art. 137** - rescisao.
  - **art. 148** - efeitos da nulidade do contrato.
  - **art. 149** - **indenizacao do contratado de BOA-FE** (custos + lucros cessantes razoaveis + danos diretos).
- **Lei 9.784/1999** - principios; art. 50 motivacao.
- **CF:**
  - **art. 5º XXXV** - inafastabilidade da jurisdicao.
  - **art. 5º XXXVI** - irretroatividade do ato juridico perfeito.
  - **art. 37** - principios da Administracao Publica.
  - **art. 109 I** - JF para Uniao.
- **Decreto 20.910/1932 art. 1º** - prescricao quinquenal contra Fazenda.
- **Lei 8.429/1992 + Lei 14.230/2021** - improbidade (interface).
- **Sumulas STJ/STF:** Sum. 473 STF (anulacao por ilegalidade); Sum. 346 STF (Administracao pode anular ato ilegal); jurisprudencia consolidada.

## 3. Vicios que fundamentam anulacao

| Vicio | Hipoteses |
|-------|----------|
| **Competencia** | Ato praticado por autoridade incompetente |
| **Forma** | Ato sem observancia da forma legal exigida (escrito, publicado, motivado) |
| **Motivacao** | Ato sem fundamentacao adequada (Lei 9.784 art. 50) |
| **Finalidade** | Desvio de poder (favorecimento, perseguicao) |
| **Objeto** | Conteudo ilegal (vinculacao ao edital violada - PA-15) |
| **Vinculacao ao instrumento** (PA-15) | Decisao contraria ao edital - art. 12 Lei 14.133 |

## 4. MS vs Anulatoria - quando usar cada

| Criterio | Mandado de Seguranca | Anulatoria |
|----------|---------------------|------------|
| **Direito** | Liquido e certo | Pode ser controvertido |
| **Instrucao** | Prova pre-constituida | Ampla (testemunhal, pericial) |
| **Prazo** | 120 dias decadencia | 5 anos prescricao |
| **Velocidade** | Mais rapido | Mais lento |
| **Liminar** | Padrao | Tutela de urgencia (CPC 300) |
| **Indenizacao** | Nao + ordinaria | Pode cumular (CPC + Lei 14.133 art. 149) |
| **Custas** | Sem | Custas judiciais |
| **Acao adequada** | Ato individualizado + urgencia | Complexidade fatica + indenizacao |

## 5. Efeitos da anulacao (art. 149 Lei 14.133)

- **Anulacao do procedimento** - restituicao das partes ao status quo ante quando possivel.
- **Anulacao do contrato:**
  - **Sem culpa do contratado de boa-fe**: indenizacao integral (custos + lucros cessantes razoaveis + danos diretos).
  - **Com culpa do contratado**: sem indenizacao + recuperacao das prestacoes recebidas indevidamente.
  - **Quando o contrato ja foi executado**: impossibilidade de retorno ao status quo ante - conversao em obrigacao de indenizar.
- **Garantia do contratado de boa-fe**: protecao constitucional (CF art. 5º XXXVI) + Lei 14.133 art. 149.

## 6. Estrutura canonica - peticao inicial

```
EXMO. JUIZ FEDERAL [OU JUIZ DE DIREITO da Vara da Fazenda Publica]

[Razao social da Autora] - CNPJ - representada por [advogado OAB ativo]

ACAO ANULATORIA COM PEDIDO DE TUTELA DE URGENCIA
em face de [UNIAO / Estado / Municipio / Autarquia / Estatal] - CNPJ

I - DOS FATOS
- [Edital n° X - orgao - objeto - valor]
- [Procedimento licitatorio + atos relevantes datados]
- [Ato/contrato impugnado: descricao precisa + data]
- [Vias administrativas exauridas (recurso/representacao TCU) ou hipoteses de
  esgotamento desnecessario (urgencia/legalidade pura)]

II - DA TEMPESTIVIDADE
Prazo prescricional de 5 anos (Decreto 20.910/1932 art. 1º) - ato em
[DD/MM/AAAA]; demanda ajuizada em [DD/MM/AAAA] - dentro do prazo.

III - DA COMPETENCIA
[JF (CF art. 109 I) se ente federal; JE Vara da Fazenda Publica se
estadual/municipal]

IV - DO INTERESSE PROCESSUAL E LEGITIMIDADE
[Licitante no certame + ato gera prejuizo direto + via judicial e
adequada (CF art. 5º XXXV)]

V - DAS CAUSAS DE PEDIR (vicios)

V.1 - Vicio de [competencia / forma / motivacao / finalidade / objeto /
vinculacao ao instrumento]
- Trecho do ato impugnado: [citacao]
- Base legal violada: [Lei 14.133/2021 art. + redacao] (PA-13)
- Sumula TCU [n°] + Jurisprudencia STJ/STF
- Vinculacao ao instrumento (PA-15 + art. 12 Lei 14.133)

V.2 - [Vicio adicional, se houver]

VI - DA TUTELA DE URGENCIA (CPC art. 300)

VI.1 - Probabilidade do direito (fumus boni iuris)
[Demonstracao com fundamentacao tripla + provas pre-constituidas]

VI.2 - Perigo de dano (periculum in mora)
- Risco concreto: [adjudicacao iminente / execucao em curso / sancao com efeitos]
- Danos irreversiveis sem tutela: [demonstrar]

VI.3 - Reversibilidade da medida (CPC art. 300 §3º)
[A tutela e reversivel - apenas suspende efeitos ate sentenca]

VII - DOS PEDIDOS

VII.1 - DE TUTELA DE URGENCIA
- Conceder tutela de urgencia (CPC 300) para SUSPENDER [ato/contrato/procedimento]
  ate sentenca final.

VII.2 - DE MERITO
a) Citacao da Re;
b) Procedencia da acao para ANULAR [procedimento / contrato / ato administrativo];
c) Condenacao da Re a:
   - Recuperacao das prestacoes (se anulacao retroativa)
   - INDENIZACAO INTEGRAL do contratado de boa-fé (art. 149 Lei 14.133):
     custos incorridos + lucros cessantes razoaveis + danos diretos
   - Atualizacao monetaria + juros (Tema 905 STJ - Selic combinada)
d) Honorarios advocaticios (CPC art. 85);
e) Custas processuais.

VIII - DO VALOR DA CAUSA
[Valor da pretensao economica]

IX - DAS PROVAS
- Documental (pre-constituida)
- Testemunhal (a especificar oportunamente)
- Pericial (a especificar oportunamente)

X - REQUERIMENTO FINAL
- Citacao da Re no endereco da Procuradoria competente
- Intervencao do MPF/MPE quando aplicavel

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}} - OAB/{{OAB_UF}} {{OAB_NUMERO}}

---
[Ressalva OAB - PA-07]
```

## 7. Memoria de quantum - indenizacao art. 149

| Componente | Base legal | Valor |
|-----------|-----------|-------|
| Custos efetivamente incorridos | art. 149 + planilha de custos | R$ X |
| Lucros cessantes razoaveis (proporcionais ao remanescente nao executado) | art. 149 | R$ Y |
| Danos diretos (perda de imagem, contratos perdidos com relacao causal) | CC art. 944 | R$ Z |
| Atualizacao monetaria | Tema 905 STJ (Selic combinada) | aplicavel desde [data] |
| **Total pleiteado** | - | **R$ TOTAL** |

**Conservadorismo (PA aplicavel)**: lucros cessantes razoaveis - jurisprudencia consolida em **percentual nao inflado** (regra geral: 5-10% do valor remanescente do contrato).

## 8. Vedacoes especificas

- **PA-04** Selo. **PA-13** citacao precisa. **PA-15** vinculacao ao instrumento.
- **PA-17** vedado opinar sobre discricionariedade do agente; apenas vicios de legalidade.
- **PA-02** vedada promessa.
- **PA-07** ressalva OAB. **PA-08** sem critica pessoal.
- **PA-20** prescricao quinquenal conferida.

## 9. Protocolos acionados

- **P1** Selo. **P2** integridade do ato/contrato + provas. **P3** memoria de quantum (indenizacao). **P4** coordenacao com TCU + MS. **P5** competencia JF/JE. **P6** R1-R4.

## 10. Localizacao

Uniao -> JF (CF art. 109 I). Autarquias federais -> JF. Estados/Municipios -> JE Vara da Fazenda Publica local. Estatais federais -> JF (em regra, conforme natureza).

## 11. Integracao

**Chamada por:** `licitacoes-master`, `/judicial`, `ms-licitacao-contrato` (alternativa), `representacao-tcu-tce` (cumulativa), `rescisao-contrato`, `defesa-apenamento-art-156`.

**Entrega para:** peticao + roteiro + `CASO.md`. Cumulacao tipica com `acao-cobranca-administracao` (indenizacao); paralela a `representacao-tcu-tce`. Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** ato/contrato com vicio consolida-se em ato juridico perfeito; perde-se janela quinquenal; indenizacao do art. 149 nao pleiteada.
