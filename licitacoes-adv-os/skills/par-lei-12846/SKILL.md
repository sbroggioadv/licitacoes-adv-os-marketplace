---
name: par-lei-12846
description: >
  Processo Administrativo de Responsabilizacao - PAR (arts. 8-15 Lei 12.846/2013 + Decreto 11.129/2022). Atos lesivos art. 5º (fraude em licitacao, conluio, corrupcao, embaraco a fiscalizacao, vantagem indevida). SANCOES ADMINISTRATIVAS art. 6º: MULTA de 0,1% a 20% do faturamento bruto + PUBLICACAO EXTRAORDINARIA da decisao. Sancoes judiciais art. 19. Rito procedimental Decreto 11.129/2022 (defesa em 30 dias uteis). Ampla defesa CF art. 5º LV. Coordenacao com sancoes art. 156 Lei 14.133 (defesa preliminar de bis in idem onde aplicavel - PA-12). Prescricao 5 anos da ciencia art. 25. Programa de integridade como atenuante (ate 4% da pena base - integracao com programa-integridade-compliance). Aciona: PAR, Lei 12.846, Lei Anticorrupcao, fraude em licitacao, conluio, ato lesivo, multa anticorrupcao, Decreto 11.129.
---

# PAR - LEI 12.846 (ANTICORRUPCAO)

> Skill **Tier 5** - defesa em Processo Administrativo de Responsabilizacao da Lei Anticorrupcao. Lei 12.846/2013 + Decreto 11.129/2022. Defesa em 30 dias uteis. Implementa P1, P2, P3, P4, P5, P6; respeita PA-12 (bis in idem), PA-13, PA-15.

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `/sancao`, ou demanda direta quando a PJ-cliente recebe **notificacao de instauracao de PAR** (Lei 12.846/2013 + Decreto 11.129/2022). Recebe: notificacao + atos imputados + contratos relevantes + provas.

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/sancao`, `defesa-apenamento-art-156` (PAR concomitante), `programa-integridade-compliance` (atenuante).
- **Pre-requisito:** Selo (PA-04); notificacao do PAR + prazo de defesa.
- **Aciona em sequencia:** `revisao-final-licitacoes`; `acordo-leniencia` se aplicavel (estrategia alternativa); `ms-licitacao-contrato` ou `acao-anulatoria-licitacao` se decisao desfavoravel (P4).
- **Entrega para:** peca defensiva + estrategia integrada (PAR + art. 156 se concomitante + leniencia se aplicavel).

## 2. Marco normativo

- **Lei 12.846/2013:**
  - **art. 5º** - atos lesivos:
    - I - prometer, oferecer, dar vantagem indevida (corrupcao);
    - II - financiar, custear pratica ilicita;
    - III - utilizar interposta pessoa para ocultar reais beneficiarios;
    - IV - especificamente em **licitacao** (4 modalidades): fraudar, frustrar, dificultar; manipular; afastar concorrente por fraude/violencia/grave ameaca; obter vantagem indevida.
    - V - dificultar atividade de investigacao/fiscalizacao.
  - **art. 6º** - **sancoes administrativas**:
    - **I - multa** de **0,1% a 20% do faturamento bruto** do ultimo exercicio (excluidos os tributos);
    - **II - publicacao extraordinaria** da decisao em meio de grande circulacao.
  - **arts. 7º-15** - **rito do PAR** + criterios de dosimetria + atenuantes/agravantes + programa de integridade.
  - **art. 16** - acordo de leniencia (cooperacao para reducao).
  - **art. 19** - **sancoes judiciais** (acao judicial pode aplicar: perdimento de bens; suspensao de atividades; dissolucao; proibicao de receber incentivos por 1-5 anos).
  - **art. 25** - **prescricao**: 5 anos da ciencia ou cessacao do ato lesivo.
- **Decreto 11.129/2022** - regulamenta:
  - **arts. 1-20** - PAR no ambito federal;
  - art. 13 - **defesa em 30 dias uteis** apos notificacao;
  - **arts. 56-58** - **programa de integridade** como atenuante (integracao com `programa-integridade-compliance`);
  - **arts. 22-29** - acordo de leniencia.
- **CF art. 5º LV + XLVI + XLIX** - ampla defesa, individualizacao da pena.
- **CF art. 8º Convencao Americana** - vedacao ao bis in idem.
- **Sumulas STF/STJ:** dosimetria; razoabilidade.

## 3. Atos lesivos especificos em licitacao (art. 5º IV)

| Modalidade | Hipoteses |
|-----------|----------|
| Fraudar a licitacao | Apresentar documento falso, simular concorrencia |
| Frustrar/dificultar | Combinar precos com concorrentes (conluio); apresentar proposta com objetivo de prejudicar; obstruir o curso normal |
| Afastar concorrente | Por fraude, oferecimento de vantagem, violencia/ameaca |
| Obter vantagem indevida | Suborno do agente; manipulacao do julgamento |

## 4. Dosimetria (art. 7º Lei 12.846 + Decreto 11.129/2022)

**Criterios:**
- Gravidade da infracao.
- Vantagem auferida.
- Consumacao ou tentativa.
- Grau de cooperacao.
- **Programa de integridade** efetivo (atenuante - art. 7º VIII + Decreto arts. 56-58 - **ate 4% da pena base**).
- Valor do contrato afetado.
- Continuidade ou repeticao.

**Faixa da multa:** 0,1% a 20% do faturamento bruto.

## 5. Estrutura canonica - peca defensiva

```
EXMO. [AUTORIDADE COMPETENTE - GERALMENTE CGU FEDERAL OU CONTROLADORIA LOCAL]
PROCESSO ADMINISTRATIVO DE RESPONSABILIZACAO N° [n°]

DEFESA EM PAR - LEI 12.846/2013
(art. 11 + Decreto 11.129/2022 art. 13 - 30 dias uteis)

I - PRELIMINAR DE TEMPESTIVIDADE
Notificacao recebida em [DD/MM/AAAA]; prazo de 30 dias uteis encerra em [DD/MM];
defesa apresentada em [DD/MM] - dentro do prazo legal.

II - QUALIFICACAO E LEGITIMIDADE
[Razao social - CNPJ - representante legal]

III - DOS FATOS IMPUTADOS
- Imputacao: ato lesivo do art. 5º [I/II/III/IV] - [descricao]
- Sancao pretendida: multa [%] + publicacao extraordinaria art. 6º

IV - PRELIMINARES

IV.1 - DA PRESCRICAO (art. 25 Lei 12.846)
[Se prazo de 5 anos da ciencia/cessacao do ato foi ultrapassado sem ato interruptivo]

IV.2 - DO BIS IN IDEM (PA-12 - CF art. 8º Convencao Americana)
[Se ha sancao do art. 156 Lei 14.133 concomitante - arguir coordenacao
institucional + impossibilidade de duplicidade pela mesma infracao]

IV.3 - DA INDIVIDUALIZACAO DA PENA (CF art. 5º XLVI, XLIX)
[Se ha multiplos envolvidos, exigir individualizacao]

V - DO MERITO

V.1 - DA AUSENCIA DE ATO LESIVO (CF art. 5º XXXIX - reserva legal)
[Refutacao do enquadramento - o fato narrado nao se subsume ao art. 5º
Lei 12.846 pelas razoes [...]]

V.2 - DA AUSENCIA DE DOLO ESPECIFICO
[Lei 12.846 exige conduta dolosa especifica - se ausente, descabe sancao
administrativa. CC art. 422 - boa-fé objetiva.]

V.3 - DA AUSENCIA DE VANTAGEM AUFERIDA
[Se nao houve resultado economico, faixa minima da multa]

V.4 - DO CUMPRIMENTO DO PROGRAMA DE INTEGRIDADE (Decreto 11.129/2022 arts. 56-58)
[Se a PJ tem programa de integridade efetivo - **atenuante de ate 4% da pena base**.
Detalhamento dos 16 parametros do programa - integracao com
`programa-integridade-compliance`]

V.5 - DA COOPERACAO DA EMPRESA NO PROCEDIMENTO
[Atendimento a diligencias, fornecimento de documentos, audiencias presenciais]

VI - DA DOSIMETRIA (subsidiario)
Caso a Administracao entenda pela aplicacao de sancao:
- Faixa minima da multa (proxima a 0,1% do faturamento bruto)
- Ausencia de publicacao extraordinaria (art. 6º II) - reservada a casos graves
- Aplicacao do programa de integridade como atenuante - reducao ate 4%

VII - DOS PEDIDOS
a) Acolhimento da defesa por tempestiva e tecnicamente fundada;
b) Acolhimento das preliminares (prescricao / bis in idem / individualizacao);
c) No merito, **arquivamento do PAR** pela ausencia de ato lesivo;
d) Subsidiariamente, dosimetria minima + aplicacao da atenuante do programa
   de integridade (Decreto 11.129/2022 arts. 56-58);
e) Em qualquer caso, **avaliacao da pertinencia de acordo de leniencia**
   (Lei 12.846 art. 16 + Decreto 11.129 arts. 22-29) - reservada a possibilidade
   de cooperacao por meio de leniencia se Administracao mantiver imputacao;
f) Reserva de via recursal administrativa + judicial.

VIII - DOCUMENTOS
- Procuracao OAB ativa (PA-05, PA-07)
- Documentos comprobatorios da defesa
- Atestado de programa de integridade (se aplicavel)
- Documentacao de cooperacao no PAD

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}} - OAB/{{OAB_UF}} {{OAB_NUMERO}}

---
[Ressalva OAB - PA-07]
```

## 6. Coordenacao - PAR vs art. 156 Lei 14.133 (PA-12 - bis in idem)

| Aspecto | Art. 156 Lei 14.133 | PAR Lei 12.846 |
|---------|---------------------|----------------|
| **Natureza** | Sancao por inadimplemento contratual/licitatorio | Sancao por ato lesivo a Administracao Publica |
| **Base de calculo** | Valor do contrato | Faturamento bruto da PJ |
| **Maximo** | 30% do valor do contrato; impedimento 3a; inidoneidade 6a | 20% do faturamento bruto + publicacao extraordinaria |
| **Rito** | art. 158 + Lei 9.784 (15 dias) | Lei 12.846 + Decreto 11.129 (30 dias) |
| **Autoridade** | Orgao licitante / autoridade superior | CGU (federal) / Controladoria local |
| **Prescricao** | 5 anos analogica Decreto 20.910 | 5 anos da ciencia art. 25 |

**Estrategia bis in idem:** quando a mesma infracao gera dupla acusacao, arguir CF art. 8º Convencao Americana. Caracteristicamente, conluio em licitacao pode gerar PAR (Lei 12.846 art. 5º IV) **e** art. 156 III (impedimento) - articulacao defensiva integrada.

## 7. Vedacoes especificas

- **PA-04** Selo. **PA-13** citacao precisa.
- **PA-12** independencia relativa - articular bis in idem.
- **PA-02** vedada promessa.
- **PA-07** ressalva OAB. **PA-08** sem critica pessoal.
- **PA-15** vinculacao ao edital + contrato quando aplicavel.
- **PA-19** preclusao - tempestividade. **PA-20** prescricao.

## 8. Protocolos acionados

- **P1** Selo. **P2** integridade da notificacao + provas. **P3** memoria de quantum (multa e dosimetria). **P4** coordenacao bis in idem. **P5** competencia (CGU/controladoria). **P6** R1-R4.

## 9. Localizacao

PAR federal -> CGU. Estadual -> controladoria estadual. Municipal -> controladoria municipal. Acao judicial subsequente -> JF/JE conforme esfera.

## 10. Integracao

**Chamada por:** `licitacoes-master`, `/sancao`, `defesa-apenamento-art-156`, `programa-integridade-compliance`.

**Entrega para:** peca + `CASO.md`. Aciona `programa-integridade-compliance` para fundamentar atenuante; `acordo-leniencia` se estrategia alternativa; `ms-licitacao-contrato` + `acao-anulatoria-licitacao` se decisao desfavoravel. Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** PAR avanca com multa maxima (20% do faturamento bruto) sem defesa - impacto financeiro devastador; perda da atenuante do programa de integridade.
