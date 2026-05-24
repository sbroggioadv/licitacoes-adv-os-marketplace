---
name: impugnacao-edital
description: >
  Peca administrativa de impugnacao ao edital (art. 164 Lei 14.133/2021 - 3 dias uteis antes da abertura). Estrutura FIRAC + 6 secoes; fundamentacao tripla obrigatoria (lei + sumula TCU + jurisprudencia STJ/STF); vinculacao ao instrumento articulada (PA-15); pedidos sucessivos (correcao + retificacao + republicacao com prazo + anulacao total). Estrategia de tempestividade rigorosa (preclusao art. 164 + Sum. TCU 274). Coordenacao com via TCU (P4) caso impugnacao nao acolhida. Trata vicio de competitividade Sum. TCU 247, capacidade tecnica Sum. TCU 222/251, marca direcionada art. 7º, garantia desproporcional art. 96, ME/EPP LC 123, indices economico-financeiros art. 69 + Sum. 251. Aciona: redigir impugnacao, peca de impugnacao, impugnar edital, art. 164, 3 dias uteis antes da abertura, vicios edital.
---

# IMPUGNACAO AO EDITAL

> Skill **Tier 2** - peca administrativa que questiona vicio de legalidade do edital. Prazo critico: **3 dias uteis antes da abertura** (art. 164 Lei 14.133/2021). Implementa P1, P2, P3, P5, P6; respeita PA-04 (Selo), PA-13 (citacao precisa), PA-15 (vinculacao), PA-19 (preclusao), PA-02 (sem promessa de resultado), PA-07 (ressalva OAB), PA-08 (sem critica pessoal).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `/impugnacao`, `analise-edital`, `deteccao-vicios-edital` quando ha vicio passivel + tempestividade. Recebe: vicios identificados + edital + anexos + qualificacao da PJ-cliente. Entrega: peca administrativa formal pronta para protocolo (rascunho - PA-05, PA-07).

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/impugnacao`, `analise-edital`, `deteccao-vicios-edital`, `analise-oportunidade` (se decisao = "impugnar antes").
- **Pre-requisito:** Selo emitido (PA-04); vicios identificados (`deteccao-vicios-edital`); prazo confirmado (`calendario-licitatorio`).
- **Aciona em sequencia:** `revisao-final-licitacoes` (R1-R4) obrigatoriamente antes de devolver; se impugnacao nao acolhida -> `representacao-tcu-tce` + `ms-licitacao-contrato` (P4).
- **Entrega para:** operador apos R1-R4 + ressalva OAB. Operador protocola sob sua OAB ativa.

## 2. Marco normativo

- **Lei 14.133/2021:**
  - **art. 164** - prazo de impugnacao **ate 3 dias uteis antes da data prevista para abertura do certame**; §1º esclarecimento mesmo prazo; §3º resposta ate o dia anterior a abertura; §4º se acolhida e altera proposta -> nova publicacao + reabertura de prazo.
  - art. 12 - **principio da vinculacao** (PA-15).
  - arts. 7º, 18, 22, 23, 33, 50, 55-56, 66-70, 96, 124-125 - dispositivos materiais.
- **CF art. 5º LV** - contraditorio e ampla defesa.
- **CF art. 37 caput** - moralidade, publicidade, eficiencia.
- **CF art. 37 XXI** - vinculacao ao edital (sentido constitucional).
- **Lei 8.666/1993** - regime residual.
- **Lei 9.784/1999** - processo administrativo federal.
- **Sumulas TCU:** 222, 247, 248, 251, 269, 274, 277, 287.

## 3. Estrutura canonica da peca - FIRAC + 6 secoes

```
EXMO. [AUTORIDADE COMPETENTE - AGENTE DE CONTRATACAO / COMISSAO / AUTORIDADE SUPERIOR]
PROCESSO ADMINISTRATIVO N° [n°]
EDITAL N° [n°] - [MODALIDADE] - [OBJETO]

I - PRELIMINAR DE TEMPESTIVIDADE
A presente impugnacao e tempestiva. O edital foi publicado em [DD/MM/AAAA];
a abertura prevista para [DD/MM/AAAA]; o prazo do art. 164 Lei 14.133/2021
(3 dias uteis antes) encerra em [DD/MM/AAAA]; protocolada em [DD/MM/AAAA] -
dentro do prazo legal.

II - QUALIFICACAO DO IMPUGNANTE E LEGITIMIDADE
[Razao social - CNPJ - endereco - representante legal devidamente qualificado -
inscrita no SICAF/PNCP - interessada em participar do certame]. Legitimidade
fundada em sua condicao de potencial licitante (art. 164 Lei 14.133/2021 +
jurisprudencia consolidada).

III - DOS FATOS
[Narrativa cronologica datada: publicacao do edital, identificacao do(s)
vicio(s), interesse legitimo na competitividade ampla.]

IV - DO DIREITO

IV.1 - Vicio 1: [nome]
- Trecho impugnado do edital: "[citacao literal do trecho]"
- Base legal violada: [Lei 14.133/2021 art. X + redacao] (PA-13)
- Sumula TCU aplicavel: Sum. TCU n° [Y] - [tema]
- Jurisprudencia STJ/STF: [Tema/REsp/RE + tribunal + turma + ano]
- Vinculacao ao instrumento (PA-15): o edital, ao prever [X], desvia-se
  do principio da vinculacao porque [...]
- Impacto na competitividade: [demonstrar]

IV.2 - Vicio 2: [...]

V - DA ESTRATEGIA DE PEDIDOS SUCESSIVOS
Pedidos formulados em escala crescente (do mais brando ao mais radical):
- Principal: correcao pontual do trecho viciado
- Sucessivo 1: retificacao com nova publicacao e reabertura de prazo (art. 164 §4º)
- Sucessivo 2: republicacao integral do edital
- Sucessivo 3: anulacao total

VI - DOS PEDIDOS
Pelo exposto, requer:
a) Conhecimento da presente impugnacao por tempestiva e tecnicamente fundada;
b) Acolhimento do pedido principal (correcao do trecho [X]);
c) Subsidiariamente, retificacao com nova publicacao e reabertura de prazo
   (art. 164 §4º Lei 14.133/2021);
d) Subsidiariamente, republicacao integral do edital;
e) Subsidiariamente, anulacao total do procedimento.

VII - DOCUMENTOS ANEXOS
- Procuracao OAB ativa (PA-05, PA-07)
- Documentos societarios da Impugnante
- Trechos impugnados destacados
- Eventual comprovacao de fato narrado

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}}
OAB/{{OAB_UF}} {{OAB_NUMERO}}
{{FIRM_NAME}}

---
[Ressalva OAB - PA-07]
Esta peça é rascunho técnico-operacional gerado por ferramenta de apoio. A
revisão final, conferência probatória e responsabilidade técnica pela versão
protocolada são do(a) advogado(a) com OAB ativa. Selo de Validação Legal
Prévia emitido em [data]. Pontos [VERIFICAR]: [lista].
```

## 4. Estrategia de tempestividade

- Prazo do **art. 164 Lei 14.133/2021**: 3 dias uteis **antes** da abertura. Conta-se em dias uteis (art. 183 Lei 14.133 + CPC art. 219 subsidiario).
- **Feriado local** do orgao licitante conta - `[VERIFICAR - calendario do orgao]` (PA-11).
- **Falta de tempestividade preclui matéria na via administrativa direta** (Sum. TCU 274) - **mas** representacao ao TCU permanece aberta (P4) + MS preventivo na JF se ato coator individualizado (P4).
- **Esclarecimento previo** (art. 164 §1º) - usar quando duvida; provoca pronunciamento da Administracao que pode embasar impugnacao subsequente.

## 5. Fundamentacao tripla (canon)

Cada vicio articulado com **3 ancoras** (PA-13):

1. **Norma legal** - Lei 14.133/2021 art. + redacao vigente (ou Lei 8.666 residual).
2. **Sumula TCU** - n° + tema literal.
3. **Jurisprudencia STJ/STF** - Tema, REsp, RE, ADI quando aplicavel.

Vinculacao ao instrumento (PA-15) e o **vetor comum** - articular como o trecho impugnado desvia da norma ou da regra do edital.

## 6. Coordenacao com via paralela (P4)

Se impugnacao **nao acolhida** e prazos abertos:
- **Representacao ao TCU/TCE** com pedido de cautelar (`representacao-tcu-tce`) - art. 174 §1º Lei 14.133 + art. 276 RI TCU.
- **MS preventivo** se ato coator individualizado e urgencia (`ms-licitacao-contrato`) - Lei 12.016/2009.

Articular **provas cruzadas**: trecho impugnado + decisao denegatoria + dados de mercado para TCU; mesma base + ato coator para MS.

## 7. Vedacoes especificas

- **PA-04** - Selo emitido antes da peca.
- **PA-13** - citacao precisa (lei+artigo+ano; sumula TCU n° + tema; jurisprudencia tribunal+turma+n°+ano).
- **PA-15** - cada vicio ancorado na vinculacao ao instrumento.
- **PA-19** - estrategia de tempestividade rigorosa (preclusao).
- **PA-02** - vedada promessa de acolhimento; probabilidade tecnica fundamentada.
- **PA-08** - vedada critica pessoal a agente de contratacao/membro de comissao; foco no ato.
- **PA-07** - ressalva OAB obrigatoria no fechamento.
- **PA-05** - peca e rascunho; protocolo e do advogado OAB ativo.
- **PA-11** - feriado local + jurisprudencia TCU recente -> `[VERIFICAR]`.

## 8. Protocolos acionados

- **P1** - Selo. **P2** - integridade do edital + anexos. **P3** - memoria de decisao (rastreabilidade quadrupla). **P4** - coordenacao se denegada. **P5** - foro/competencia interna do orgao. **P6** - R1-R4 obrigatorio antes da entrega.

## 9. Localizacao

Autoridade competente para receber impugnacao = a definida no edital (em regra: a mesma que assina o edital ou o agente de contratacao). Federal -> TCU. Estadual/municipal -> TCE/TCM. Esfera afeta tambem o foro do MS subsequente. `[VERIFICAR]` quando regulamento local nao confirmado.

## 10. Integracao

**Chamada por:** `licitacoes-master`, `/impugnacao`, `analise-edital`, `deteccao-vicios-edital`, `analise-oportunidade`.

**Entrega para:** operador (peca apos R1-R4 + ressalva OAB) + `CASO.md`. Acompanhamento: se denegada -> `representacao-tcu-tce` + `ms-licitacao-contrato`. Entrega final passa por `revisao-final-licitacoes` (P6 - APROVADO/REVISAR/BLOQUEADO).

**Sem esta skill:** vicios identificados ficam preclusos; participacao no certame sem questionamento de exigencias restritivas; risco de inabilitacao/desclassificacao subsequente sem direito a recorrer da clausula original.
