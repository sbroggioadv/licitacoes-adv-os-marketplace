---
name: defesa-apenamento-art-156
description: >
  Defesa em processo administrativo de apenamento (art. 158 Lei 14.133/2021 - rito procedimental + 15 dias uteis de defesa). 4 SANCOES do art. 156: (i) advertencia; (ii) multa; (iii) IMPEDIMENTO de licitar e contratar com a Administracao no ambito do ente ate 3 anos; (iv) DECLARACAO DE INIDONEIDADE para licitar ou contratar com toda a Administracao Publica ate 6 anos. Ampla defesa e contraditorio (CF art. 5º LV; Lei 9.784/1999). DOSIMETRIA (proporcionalidade, razoabilidade, atenuantes, agravantes - art. 156 §3º). Prescricao (5 anos analogica Decreto 20.910/1932). Coordenacao com PAR Lei 12.846 (bis in idem - PA-12). Aciona: defesa em sancao, art. 156, art. 158, advertencia, multa, impedimento, inidoneidade, dosimetria, ampla defesa administrativa.
---

# DEFESA EM APENAMENTO ART. 156

> Skill **Tier 5** - defesa no processo administrativo de aplicacao das 4 sancoes do art. 156 Lei 14.133/2021. Rito: art. 158 + Lei 9.784/1999. 15 dias uteis de defesa. Implementa P1, P2, P3, P4, P5, P6; respeita PA-12 (independencia das esferas), PA-13 (citacao precisa), PA-15.

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `/sancao`, ou demanda direta quando a PJ-cliente recebe **notificacao de instauracao de PAD sancionatorio** (art. 158). Recebe: notificacao + edital + contrato + provas relevantes (atos da execucao, fiscalizacao, justificativas).

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/sancao`, `gestao-cronograma-fiscalizacao` (apos notificacao), `rescisao-contrato` (quando ha sancao concomitante).
- **Pre-requisito:** Selo (PA-04); notificacao do PAD + prazo de defesa.
- **Aciona em sequencia:** `revisao-final-licitacoes` antes da entrega; se ha PAR concomitante -> `par-lei-12846` (bis in idem); se decisao desfavoravel -> `ms-licitacao-contrato` (P4) + `acao-anulatoria-licitacao`.
- **Entrega para:** peca defensiva administrativa (rascunho + R1-R4 + ressalva OAB).

## 2. Marco normativo

- **Lei 14.133/2021:**
  - **art. 156** - sancoes:
    - **I - advertencia** (atraso injustificado, falta tecnica menor).
    - **II - multa** (ate 30% do valor do contrato; gradacao no §3º).
    - **III - impedimento de licitar e contratar com a Administracao no ambito do ente** - **ate 3 anos**.
    - **IV - declaracao de inidoneidade** para licitar ou contratar com toda a Administracao Publica - **ate 6 anos**.
  - **art. 156 §3º** - **dosimetria** - graduacao conforme natureza/gravidade/extensao da infracao + repercussao social/economica + repeticao + atenuantes/agravantes.
  - **art. 158** - **rito** - notificacao + defesa em **15 dias uteis** + decisao motivada + recurso administrativo.
  - **art. 158 §2º** - intimacao pessoal ou postal + ciencia para inicio do prazo.
  - **art. 159** - prescricao da pretensao punitiva (regulamento define; aplicacao analogica do Decreto 20.910/1932 = 5 anos).
- **CF art. 5º LV** - ampla defesa e contraditorio.
- **CF art. 5º XXXIX-XL** - reserva legal + retroatividade benigna.
- **CF art. 8º Convencao Americana** - vedacao ao bis in idem (coordenacao com PAR).
- **Lei 9.784/1999** - PAD federal (subsidiaria) - direito a:
  - art. 2º - principios (proporcionalidade, razoabilidade, motivacao).
  - art. 50 - dever de fundamentacao motivada.
  - arts. 56-65 - ampla defesa procedimental.
- **Decreto 20.910/1932 art. 1º** - prescricao quinquenal aplicacao analogica.
- **Sumulas STF/STJ:** vedacao ao bis in idem; razoabilidade na dosimetria.

## 3. As 4 sancoes - hipoteses e graduacao

| Sancao | Hipoteses tipicas | Limite |
|--------|-------------------|--------|
| **Advertencia** | Falta menor, atraso pontual sem prejuizo significativo | Comunicada |
| **Multa** | Atraso reiterado, descumprimento parcial, inexecucao de obrigacao acessoria | Ate **30%** do valor do contrato (mas regulamento pode escalonar; jurisprudencia limita - razoabilidade) |
| **Impedimento (art. 156 III)** | Infracao grave (fraude em licitacao, descumprimento contratual substantivo, inadimplemento sem justificativa) | **Ate 3 anos** no ambito do ente licitante |
| **Inidoneidade (art. 156 IV)** | Infracao gravissima (fraude, conluio, corrupcao, dolo) | **Ate 6 anos** em toda Administracao Publica |

## 4. Estrutura canonica - peca defensiva

```
EXMO. [AUTORIDADE COMPETENTE - GESTOR / AUTORIDADE SUPERIOR]
PROCESSO ADMINISTRATIVO SANCIONATORIO N° [n°]
CONTRATO N° [n°] - EDITAL N° [n°]

DEFESA NO PROCESSO DE APENAMENTO
(art. 158 §2º Lei 14.133/2021 + CF art. 5º LV)

I - PRELIMINAR DE TEMPESTIVIDADE E REGULARIDADE PROCEDIMENTAL
- Notificacao recebida em [DD/MM/AAAA]; prazo de 15 dias uteis encerra em [DD/MM]
- Defesa apresentada em [DD/MM] - dentro do prazo legal (art. 158 §2º)
- Cumprimento dos requisitos formais da Lei 9.784/1999

II - QUALIFICACAO E LEGITIMIDADE
[Razao social - CNPJ - representante legal]

III - DOS FATOS
- Contrato n° [X] assinado em [DD/MM/AAAA]
- Imputacao: [descricao precisa - art. 156 I/II/III/IV pretendido]
- Versao da Defendente: [contraposicao com prova documental]

IV - PRELIMINARES (quando cabivel)

IV.1 - DA NULIDADE PROCEDIMENTAL
[Se aplicavel - notificacao deficiente, ausencia de motivacao do ato instaurador,
imputacao generica violando contraditorio]

IV.2 - DA PRESCRICAO (art. 159 + analogia Decreto 20.910/1932)
[Se prazo de 5 anos da infracao foi ultrapassado sem ato interruptivo]

IV.3 - DO BIS IN IDEM (PA-12)
[Se ha PAR concomitante - Lei 12.846/2013 + Decreto 11.129/2022 - arguir
coordenacao institucional ou impossibilidade de duplicidade]

V - DO MERITO

V.1 - Da ausencia de infracao
[Refutacao tecnica de cada imputacao]
- Imputacao 1: refutada por [...]
- Documento: [...]
- Vinculacao ao contrato (PA-15): obrigacao cumprida conforme [clausula X]

V.2 - Das causas excludentes (quando aplicaveis)
- Fato da Administracao: [atraso de projeto, demora em fiscalizacao, etc.]
- Caso fortuito / forca maior (CC art. 393)
- Ausencia de dolo ou culpa grave (CC art. 422)
- Cumprimento substancial (Sum. TCU 269 - formalismo moderado se vicio formal)

V.3 - Da ausencia de prejuizo
[Demonstrar que a conduta nao causou dano significativo - relevante para dosimetria]

VI - DA DOSIMETRIA (art. 156 §3º) - subsidiario

Caso a Administracao entenda pela aplicacao de sancao, devem ser considerados:
- **Natureza e gravidade**: [argumentar para o lado mais brando]
- **Extensao e repercussao social/economica**: [minimizar]
- **Repeticao**: [primeira infracao da contratada]
- **Atenuantes**: cumprimento substancial do contrato; cooperacao no PAD;
  ausencia de dolo; reparacao espontanea (se ocorreu)
- **Aplicacao da sancao mais branda** que cumpra a finalidade - **advertencia
  ou multa minima** ao inves de impedimento/inidoneidade
- **Proporcionalidade e razoabilidade** (CF art. 5º + Lei 9.784/1999 art. 2º)

VII - DOS PEDIDOS
a) Acolhimento da defesa por tempestiva e tecnicamente fundada;
b) Acolhimento das preliminares (nulidade / prescricao / bis in idem);
c) No merito, improcedencia do PAD - arquivamento sem aplicacao de sancao;
d) Subsidiariamente, dosimetria mais branda - advertencia (art. 156 I) ou
   multa minima (art. 156 II);
e) Em qualquer caso, reserva de via recursal administrativa + judicial (P4).

VIII - DOCUMENTOS
- Procuracao OAB ativa (PA-05, PA-07)
- Provas documentais (notificacoes do contrato, diario de obra, atas)
- Eventuais cotacoes / indices / certidoes

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}} - OAB/{{OAB_UF}} {{OAB_NUMERO}}

---
[Ressalva OAB - PA-07]
```

## 5. Dosimetria estrategica (art. 156 §3º)

Argumentos canônicos para sancao mais branda:
1. **Primeira infracao** (sem reincidencia).
2. **Cumprimento substancial** do contrato (proporcao do executado).
3. **Ausencia de dolo** (culpa leve ou sem culpa).
4. **Causa nao imputavel** (fato da Administracao, caso fortuito).
5. **Reparacao espontanea** (saneamento da falha).
6. **Cooperacao no PAD** (atende diligencias, fornece documentos).
7. **Impacto social/economico positivo** da continuidade da PJ no mercado.

## 6. Coordenacao P4 e bis in idem (PA-12)

**Se ha PAR concomitante (Lei 12.846/2013):** preliminar de **bis in idem** ou pelo menos coordenacao institucional (CF art. 8º Convencao Americana). Defesa estruturada em paralelo via `par-lei-12846`.

**Se aplicada sancao final (apos recurso administrativo):**
1. **MS** (`ms-licitacao-contrato`) - 120 dias da ciencia da decisao final (art. 23 Lei 12.016/2009) - ato coator individualizado.
2. **Acao anulatoria** (`acao-anulatoria-licitacao`) - CPC + tutela de urgencia para suspender efeitos.
3. **Representacao ao TCU/TCE** se houver irregularidade procedimental ou desvio de poder.

## 7. Vedacoes especificas

- **PA-04** Selo. **PA-13** citacao precisa.
- **PA-12** independencia relativa - articular bis in idem quando ha duplicidade com PAR.
- **PA-02** vedada promessa.
- **PA-07** ressalva OAB. **PA-08** sem critica pessoal a fiscal/gestor.
- **PA-15** vinculacao ao contrato + edital em cada refutacao.
- **PA-19** preclusao - tempestividade rigorosa.
- **PA-20** prescricao - sempre conferir (alvo movel).

## 8. Protocolos acionados

- **P1** Selo. **P2** integridade da notificacao + provas. **P3** memoria de quantum (multa e proporcionalidade). **P4** coordenacao bis in idem + via judicial. **P5** autoridade competente. **P6** R1-R4.

## 9. Localizacao

Federal -> autoridade do orgao + TCU paradigma + JF para MS subsequente. Estadual/municipal -> autoridade local + TCE/TCM + JE.

## 10. Integracao

**Chamada por:** `licitacoes-master`, `/sancao`, `gestao-cronograma-fiscalizacao`, `rescisao-contrato`.

**Entrega para:** peca defensiva + `CASO.md`. Aciona `par-lei-12846` em paralelo se ha PAR; `ms-licitacao-contrato` + `acao-anulatoria-licitacao` se decisao final desfavoravel. Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** PAD termina com sancao maxima sem defesa estruturada - impedimento/inidoneidade aplicada (perda de mercado por anos); ou perda de oportunidade de arguir bis in idem com PAR concomitante.
