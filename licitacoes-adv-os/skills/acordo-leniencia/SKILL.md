---
name: acordo-leniencia
description: >
  Acordo de leniencia (art. 16 Lei 12.846/2013 + Decreto 11.129/2022 arts. 22-29). COOPERACAO EFETIVA: (1) identificacao dos demais envolvidos; (2) informacoes que permitam apuracao celere; (3) obtencao de provas. REQUISITOS: PRIMEIRA a se manifestar; cessa envolvimento; admite participacao; coopera plenamente. BENEFICIOS: reducao de ate 2/3 da multa; ISENCAO de declaracao de inidoneidade; isencao de publicacao extraordinaria. Estrategia de negociacao com CGU/MPU/controladoria. Compatibilidade com colaboracao penal (Lei 12.850/2013). Decisao estrategica delicada - delineia se a PJ admite participacao em troca de beneficio ou enfrenta PAR/judicial. Aciona: acordo de leniencia, art. 16 Lei 12.846, colaboracao Anticorrupcao, CGU leniencia, beneficios leniencia, reducao de multa anticorrupcao.
---

# ACORDO DE LENIENCIA

> Skill **Tier 5** - acordo de leniencia da Lei Anticorrupcao. Decisao estrategica delicada. Lei 12.846/2013 art. 16 + Decreto 11.129/2022 arts. 22-29. Implementa P1, P3, P4, P5, P6; respeita PA-12 (independencia das esferas), PA-13, PA-09 (sigilo).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `/sancao`, ou `par-lei-12846` (quando defesa indica que cooperacao via leniencia pode ser mais vantajosa que confronto). Recebe: situacao concreta da PJ + fatos imputados + posicao da Administracao + risco de PAR/judicial.

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/sancao`, `par-lei-12846`, `programa-integridade-compliance`.
- **Pre-requisito:** Selo (PA-04); decisao estrategica do operador apos avaliacao com a PJ - **decisao da PJ em admitir participacao + cooperar** (PA-09 sigilo + PA-22 compartimentacao - **decisao irreversivel**).
- **Aciona em sequencia:** `revisao-final-licitacoes`; se acordo prospera -> integracao com `programa-integridade-compliance`; se nao prospera -> manter defesa em `par-lei-12846`.
- **Entrega para:** parecer estrategico + minuta de proposta + roteiro de negociacao com CGU/controladoria.

## 2. Marco normativo

- **Lei 12.846/2013:**
  - **art. 16** - acordo de leniencia - **requisitos cumulativos** (caput + §1º):
    - I - **primeira pessoa juridica** a se manifestar interesse em cooperar;
    - II - **cessa completamente o envolvimento** na infracao;
    - III - **admite participacao** no ilicito + coopera **plenamente** com as investigacoes (identificacao dos demais envolvidos + producao de provas);
  - **art. 16 §2º** - **beneficios** ao acordante:
    - **reducao da multa** ate **2/3** (art. 16 §2º I);
    - **isencao** da declaracao de inidoneidade (II);
    - **isencao** da publicacao extraordinaria (III);
  - **art. 16 §6º** - efeitos sobre demais penalidades.
  - **arts. 17-18** - rito + competencia (CGU federal; controladorias locais).
  - **arts. 19-20** - sancoes judiciais (acao judicial independente).
- **Decreto 11.129/2022:**
  - **arts. 22-29** - **acordo de leniencia federal** - rito procedimental detalhado;
  - art. 26 - **clausulas obrigatorias** do acordo (cooperacao + admissao + cessamento + compromissos de reparacao);
  - art. 27 - acompanhamento + verificacao do cumprimento;
  - art. 28 - hipoteses de rescisao do acordo (descumprimento, novos atos lesivos, omissao).
- **Lei 12.850/2013** - colaboracao penal (compatibilidade com leniencia administrativa - regimes paralelos, com beneficios distintos para PF dos representantes).
- **CF art. 5º LIV-LV** - devido processo + ampla defesa (a admissao em leniencia nao afasta direitos no rito subsequente).
- **Sumulas STJ/STF:** acordos administrativos + execucao + revisao judicial.

## 3. Quando a leniencia faz sentido estrategicamente

| Cenario | Recomendacao |
|---------|--------------|
| **Caso de pequena gravidade / sem prova robusta** | NAO leniencia (cooperar sem necessidade enfraquece a defesa) |
| **Provas em poder da Administracao razoaveis + risco de PAR maximo** | AVALIAR leniencia (reducao ate 2/3 + isencao de inidoneidade) |
| **Conluio com terceiros + investigacao em curso** | LENIENCIA pode ser vantajosa (primeira manifesta = melhor beneficio) |
| **PJ unica envolvida** | Leniencia menos vantajosa (nao ha "outros" para identificar) |
| **Risco judicial penal de representantes** | Articular com colaboracao penal Lei 12.850 - regime paralelo |

## 4. Os 4 requisitos cumulativos (art. 16)

### 4.1 - Primeira a se manifestar (I)
- Vantagem para quem inicia a cooperacao primeiro.
- Estrategia: avaliar se ha indicios de que concorrentes envolvidos vao iniciar tambem - pressao temporal.

### 4.2 - Cessacao completa do envolvimento (II)
- A PJ deve **demonstrar** que cessou qualquer participacao na conduta lesiva.
- Implica reorganizacao interna + medidas de compliance.

### 4.3 - Admissao da participacao (III)
- **Implicacao critica:** admitir formalmente a participacao no ilicito.
- Efeitos colaterais: pode ser usado em **outros processos** (penal contra representantes, civel de improbidade, etc.) - exigem articulacao paralela com defesa nessas frentes.

### 4.4 - Cooperacao plena
- Identificar **outros envolvidos** (PJs concorrentes, agentes publicos).
- Fornecer **documentos, comunicacoes, evidencias** que permitam apuracao.
- Comparecer a audiencias e prestar esclarecimentos.

## 5. Estrutura - proposta de acordo

```
EXMO. [AUTORIDADE COMPETENTE - CGU FEDERAL OU CONTROLADORIA ESTADUAL/MUNICIPAL]
PROCESSO ADMINISTRATIVO N° [n°] (PAR em curso ou processo investigatorio)

PROPOSTA DE ACORDO DE LENIENCIA
(art. 16 Lei 12.846/2013 + Decreto 11.129/2022 arts. 22-29)

I - QUALIFICACAO
[Razao social - CNPJ - representante legal devidamente qualificado]

II - DA INTENCAO DE COOPERAR
A Proponente manifesta interesse em **cooperar voluntariamente** com a apuracao
dos fatos relativos ao processo [n°] - mediante acordo de leniencia - pelo
preenchimento dos requisitos do art. 16 Lei 12.846/2013.

III - DO ATENDIMENTO DOS REQUISITOS

III.1 - Primeira a manifestar interesse (art. 16 I)
[A Proponente e a primeira PJ envolvida a manifestar interesse no presente caso,
conforme verificavel nos autos / certidao de cooperacao a ser emitida]

III.2 - Cessacao completa do envolvimento (II)
[A Proponente cessou em [DD/MM/AAAA] qualquer participacao na conduta;
medidas de compliance interno implementadas em [data]]

III.3 - Admissao da participacao (III) - condicional ao acordo
[A admissao formal da participacao fica condicionada a homologacao do acordo
nos termos propostos]

III.4 - Cooperacao plena (compromisso)
[A Proponente compromete-se a:
- Identificar os demais envolvidos (PJs, PFs, agentes)
- Fornecer documentos e evidencias (lista preliminar anexa, sob compromisso
  de sigilo - PA-09)
- Comparecer a audiencias e prestar esclarecimentos]

IV - DOS BENEFICIOS PRETENDIDOS (art. 16 §2º)
a) **Reducao de 2/3 da multa** prevista no art. 6º I Lei 12.846;
b) **Isencao** da declaracao de inidoneidade (art. 6º analogica);
c) **Isencao** da publicacao extraordinaria (art. 6º II);
d) Reflexo sobre eventuais sancoes do art. 156 Lei 14.133 (bis in idem).

V - DAS CLAUSULAS PROPOSTAS (sintese)
- Cooperacao continuada por [N] meses
- Programa de integridade reforcado (arts. 56-58 Decreto 11.129/2022)
- Reparacao integral de danos comprovados
- Pagamento da multa em parcelas (negociar)
- Acompanhamento por [CGU/Controladoria] por [N] anos

VI - DOS PEDIDOS
a) Acolhimento da proposta;
b) Abertura de negociacao formal nos termos do Decreto 11.129/2022;
c) Garantia de sigilo durante negociacao (art. 27 Decreto 11.129).

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}} - OAB/{{OAB_UF}} {{OAB_NUMERO}}

---
[Ressalva OAB - PA-07]
```

## 6. Compatibilidade com colaboracao penal (Lei 12.850/2013)

- **Regimes paralelos**: leniencia (administrativa - Lei 12.846) + colaboracao premiada (penal - Lei 12.850).
- **Negociacao integrada**: representantes PF da PJ podem precisar de colaboracao penal alem da leniencia administrativa.
- **Articulacao**: leniencia com CGU/controladoria + colaboracao com MPF/MPE - **escritorios penal e administrativo devem ser coordenados**.

## 7. Riscos do acordo de leniencia

1. **Admissao da participacao** vincula a PJ a confessar o ilicito - reflexo em outras frentes.
2. **Descumprimento do acordo** -> rescisao (Decreto 11.129/2022 art. 28) + perda dos beneficios + uso da admissao em desfavor.
3. **Cooperacao incompleta** -> Administracao pode considerar nao cumprida.
4. **Identificacao de terceiros** pode gerar acoes civis/criminais paralelas.
5. **Reputacional** - mesmo com isencao de publicacao extraordinaria, vazamento de acordo gera risco de imagem.

## 8. Vedacoes especificas

- **PA-04** Selo. **PA-13** citacao precisa.
- **PA-02** vedada promessa de homologacao do acordo; resultado depende de negociacao com CGU/controladoria.
- **PA-09** sigilo absoluto da negociacao (Decreto 11.129/2022 art. 27).
- **PA-22** compartimentacao - caso de leniencia e isolado de outros casos da PJ.
- **PA-07** ressalva OAB.
- **PA-18** - fronteira com colaboracao penal: sinalizar "encaminhar a especialista penal" sem citar produto irmao.

## 9. Protocolos acionados

- **P1** Selo. **P3** memoria de quantum (multa apos reducao + custos de cooperacao). **P4** coordenacao com penal (Lei 12.850). **P5** competencia (CGU federal / controladoria estadual). **P6** R1-R4.

## 10. Localizacao

Federal -> CGU. Estadual -> controladoria estadual. Municipal -> controladoria municipal ou CGU em caso de recurso federal envolvido. `[VERIFICAR]` regulamento de cada controladoria.

## 11. Integracao

**Chamada por:** `licitacoes-master`, `/sancao`, `par-lei-12846`, `programa-integridade-compliance`.

**Entrega para:** parecer estrategico + minuta da proposta + roteiro de negociacao + `CASO.md`. Se acordo prospera -> integracao com `programa-integridade-compliance` (atenuante + reforco de compliance). Se nao prospera -> mantem-se `par-lei-12846` + judicial subsequente. Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** PJ enfrenta PAR sem avaliar oportunidade de cooperacao - perde reducao de ate 2/3 + isencao de inidoneidade; ou aceita leniencia sem analise estrategica adequada (riscos colaterais subestimados).
