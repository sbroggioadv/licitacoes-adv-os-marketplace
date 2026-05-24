---
name: ms-licitacao-contrato
description: >
  Mandado de seguranca (Lei 12.016/2009 + CF art. 5º LXIX) - cabimento contra ato de autoridade publica (agente de contratacao, comissao, autoridade superior, conselheiro TCU/TCE). Ato coator concreto + direito liquido e certo. Prazo decadencial de 120 dias da ciencia (art. 23 Lei 12.016). MS PREVENTIVO (ameaca concreta - admitido sem esgotamento administrativo) x MS REPRESSIVO (ato ja praticado). Pedido LIMINAR (suspensao de adjudicacao, do procedimento, do contrato, da sancao, dos efeitos do acordao TCU). COMPETENCIA: JF se autoridade federal (CF art. 109 I); STJ se conselheiro TCE; STF se conselheiro TCU; JE municipal/estadual. Aciona: mandado de seguranca, MS preventivo, MS repressivo, art. 23 Lei 12.016, 120 dias, liminar de suspensao, direito liquido e certo, autoridade coatora.
---

# MANDADO DE SEGURANCA EM LICITACOES E CONTRATOS

> Skill **Tier 6** - acao constitucional para impugnar ato de autoridade publica em materia de licitacao/contrato. Lei 12.016/2009 + CF art. 5º LXIX. Prazo decadencial: 120 dias. Implementa P1, P2, P3, P4, P5, P6; respeita PA-13, PA-15, PA-17.

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `/judicial`, ou apos exaurimento administrativo (sem necessidade de esgotamento - PA-21). Recebe: ato coator + direito liquido e certo + autoridade coatora identificada + urgencia (para liminar).

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/judicial`, `recurso-administrativo` (apos improvido), `defesa-apenamento-art-156` (apos decisao final), `representacao-tcu-tce` (concomitante quando ha urgencia), `rescisao-contrato`.
- **Pre-requisito:** Selo (PA-04); ato coator + autoridade identificada; prazo de 120 dias nao decorrido (PA-20).
- **Aciona em sequencia:** `revisao-final-licitacoes`; em paralelo com `representacao-tcu-tce` quando estrategico; eventual conversao em ordinaria se direito nao for liquido e certo.
- **Entrega para:** peticao inicial de MS + pedido liminar + roteiro de acompanhamento processual.

## 2. Marco normativo

- **CF:**
  - **art. 5º LXIX** - mandado de seguranca para proteger direito liquido e certo de ato ilegal ou abusivo de autoridade publica.
  - **art. 5º XXXV** - inafastabilidade da jurisdicao.
  - **art. 109 I** - **JF competente** para autoridade federal.
  - **art. 102 I d** - **STF** para conselheiro do TCU.
  - **art. 105 I a, b** - **STJ** para conselheiro do TCE.
- **Lei 12.016/2009:**
  - **art. 1º** - cabimento + autoridade publica + ato ilegal/abusivo.
  - **art. 2º** - autoridade coatora.
  - **art. 5º** - vedacoes (decisao administrativa pendente de recurso com efeito suspensivo - exceto a Lei 14.133 art. 165 §5º).
  - **art. 6º** - peticao inicial.
  - **art. 7º** - **liminar** - requisitos: relevante fundamento + ineficacia da medida se concedida apos.
  - **art. 7º III** - liminar suspensiva.
  - **art. 12** - sentencas mandatorias.
  - **art. 14** - apelacao + duplo grau obrigatorio.
  - **art. 19** - cumulacao com pedido indenizatorio em acao ordinaria.
  - **art. 23** - **decadencia de 120 dias** da ciencia do ato impugnado.
- **CPC arts. 300, 311** - tutela de urgencia (subsidiaria); evidencia.
- **Lei 14.133/2021 art. 165 §5º** - efeito suspensivo do recurso administrativo NAO afasta MS preventivo.
- **Sumulas STF/STJ:** Sum. 266 STF (MS contra lei em tese vedado - cabivel contra ato administrativo individual); Sum. 271 STF (MS nao substitui acao de cobranca); Sum. 326 STF (MS contra ato coator); Sum. 624 STJ (MS preventivo + ameaca concreta); jurisprudencia consolidada sobre licitacoes.

## 3. Cabimento - 5 dimensoes

### 3.1 - Ato coator
- Ato individualizado de autoridade publica (agente de contratacao, comissao, gestor de contrato, autoridade superior, conselheiro de TC).
- Nao cabe contra lei em tese (Sum. 266 STF).

### 3.2 - Direito liquido e certo
- **Liquido**: precisao quanto ao alcance.
- **Certo**: comprovado **documentalmente** com a inicial (a instrucao probatoria e excepcional em MS - so prova pre-constituida).
- Se ha controversia fatica complexa -> ordinaria.

### 3.3 - Tempestividade
- **120 dias da ciencia** do ato (art. 23 Lei 12.016 - decadencia).
- MS preventivo: prazo conta-se do ato que **ameaca**.
- MS contra acordao TCU: 120 dias da publicacao.

### 3.4 - MS Preventivo vs Repressivo

| Modalidade | Quando | Requisitos |
|-----------|--------|-----------|
| **Preventivo** | Ameaca concreta + iminente | Sum. 624 STJ - ameaca demonstrada + recurso administrativo inocuo (Lei 14.133 art. 165) |
| **Repressivo** | Ato ja praticado | Ato individualizado + 120 dias |

### 3.5 - Vedacoes (art. 5º Lei 12.016)
- Decisao administrativa pendente de recurso com efeito suspensivo (excecao: nao cabe quando ha efeito suspensivo - mas o art. 165 §5º Lei 14.133 nao afasta MS preventivo concomitante - jurisprudencia consolida).

## 4. Estrutura canonica - Peticao inicial de MS

```
EXMO. JUIZ FEDERAL [OU DESEMBARGADOR / MINISTRO conforme competencia]
[Vara competente]

[Razao social da Impetrante] - CNPJ - representada por [advogado OAB ativo]

vem, com fundamento no art. 5º LXIX da CF + Lei 12.016/2009, impetrar

MANDADO DE SEGURANCA [PREVENTIVO / REPRESSIVO] COM PEDIDO DE LIMINAR
contra ato de [AUTORIDADE COATORA - cargo + orgao].

I - DOS FATOS
- [Edital n° X - orgao - objeto - valor]
- [Procedimento licitatorio + atos relevantes datados]
- [Ato coator: descricao precisa + data]
- [Recurso administrativo (se houve) + decisao denegatoria]

II - DA TEMPESTIVIDADE
Decadencia de 120 dias da ciencia (art. 23 Lei 12.016/2009).
- Ciencia do ato em [DD/MM/AAAA]
- Impetracao em [DD/MM/AAAA]
- Prazo decadencial: dentro dos 120 dias.

III - DA COMPETENCIA
[JF se autoridade federal (CF art. 109 I); STJ/STF para conselheiros; JE local
para autoridade estadual/municipal]

IV - DA AUTORIDADE COATORA
[Cargo + nome + orgao + endereco para notificacao]

V - DO DIREITO LIQUIDO E CERTO
[Demonstracao com documentos pre-constituidos:
- Inscricao no SICAF/PNCP
- Participacao no certame
- Vinculacao ao edital (PA-15)
- Comprovacao documental do direito violado]

VI - DA ILEGALIDADE / ABUSO DO ATO COATOR

VI.1 - Da base legal violada
- [Lei 14.133/2021 art. + redacao vigente] (PA-13)
- [Lei 8.666/1993 residual quando aplicavel]
- Sum. TCU [n°] - [tema]
- Jurisprudencia: [Tema STJ + REsp + ano + turma]

VI.2 - Da vinculacao ao instrumento (PA-15)
[O ato afastou-se do edital ao [...]]

VI.3 - Do desvio de finalidade / abuso (quando aplicavel)
[Lei 9.784/1999 art. 2º; CF art. 37 - moralidade]

VII - DO FUMUS BONI IURIS E PERICULUM IN MORA (para liminar)

VII.1 - Fumus boni iuris
[Demonstracao da relevancia juridica do pedido - vinculacao + sumula TCU +
jurisprudencia + vinculacao ao edital]

VII.2 - Periculum in mora
- Risco concreto e iminente: [adjudicacao em DD/MM / assinatura em DD/MM /
  execucao iminente / sancao com efeitos imediatos]
- Danos irreversiveis sem liminar: [perda do certame / consolidacao de
  pagamento indevido / sancao com publicidade danosa]

VIII - DOS PEDIDOS

VIII.1 - DE LIMINAR (art. 7º III Lei 12.016)
- Conceder liminar para SUSPENDER [imediatamente] [ato impugnado, seus
  efeitos, adjudicacao iminente, assinatura do contrato, execucao da sancao]
  ate decisao final.

VIII.2 - DE MERITO
a) Notificacao da Autoridade Coatora para apresentar informacoes;
b) Vista do MPF/MPE (Lei 12.016 art. 12);
c) Concessao definitiva da seguranca anulando o ato coator;
d) Determinacao a Autoridade para [conduta especifica - habilitar / classificar /
   restaurar contrato / cancelar sancao / suspender efeitos do acordao TCU];
e) Garantia da Impetrante quanto a participacao no certame em condicoes regulares.

IX - DO VALOR DA CAUSA
[Valor estimado do contrato / sancao impugnada]

X - DOCUMENTOS
- Procuracao OAB ativa (PA-05, PA-07)
- Contrato social + ata
- Edital + ato impugnado + decisao
- Recurso administrativo (se houve) + decisao denegatoria
- Provas documentais

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}} - OAB/{{OAB_UF}} {{OAB_NUMERO}}

---
[Ressalva OAB - PA-07]
```

## 5. Competencia (P5)

| Autoridade Coatora | Competencia |
|---------------------|-------------|
| Agente de contratacao / comissao federal | JF (CF art. 109 I) - vara federal local |
| Autoridade superior federal | JF - vara federal local |
| Ministro de Estado | STJ (CF art. 105 I b) |
| Conselheiro TCU | STF (CF art. 102 I d) |
| Conselheiro TCE | STJ (CF art. 105 I a) |
| Agente estadual / municipal | JE - vara da fazenda publica local |
| Governador / Secretario de Estado | TJ local (competencia originaria) |

## 6. Coordenacao P4 - vias paralelas

**MS + Representacao TCU (concomitantes):**
- MS na JF/JE para ato coator individualizado.
- Representacao no TCU para reformar acordao ou suspender procedimento.
- **Provas cruzadas** - mesma base.
- Acordao TCU favoravel reforca MS; concessao de liminar judicial reforca representacao.

**MS + Acao anulatoria:**
- MS para urgencia + suspensao imediata.
- Anulatoria para tutela definitiva (mais ampla quanto a instrucao + danos materiais).

## 7. Vedacoes especificas

- **PA-04** Selo. **PA-13** citacao precisa. **PA-15** ato impugnado articulado na vinculacao.
- **PA-17** vedado opinar sobre discricionariedade do agente; apenas vicios de legalidade.
- **PA-02** vedada promessa de liminar/concessao.
- **PA-07** ressalva OAB. **PA-08** sem critica pessoal a autoridade coatora; foco no ato.
- **PA-20** decadencia de 120 dias rigorosa.

## 8. Protocolos acionados

- **P1** Selo. **P2** integridade documental. **P3** memoria de fumus + periculum. **P4** coordenacao. **P5** competencia critica. **P6** R1-R4.

## 9. Localizacao

Federal -> JF. Estadual -> JE / TJ. Municipal -> JE local. Conselheiros TCs -> STF/STJ. `[VERIFICAR]` competencia em caso de duvida (jurisprudencia consolida-se caso a caso).

## 10. Integracao

**Chamada por:** `licitacoes-master`, `/judicial`, `recurso-administrativo`, `defesa-apenamento-art-156`, `representacao-tcu-tce`, `rescisao-contrato`.

**Entrega para:** peticao inicial + roteiro + `CASO.md`. Paralelo a `representacao-tcu-tce` + `acao-anulatoria-licitacao` quando estrategico. Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** ato administrativo ilegal consolida (perda do certame, sancao com publicidade, contrato com vicio); 120 dias passam (decadencia); resta apenas ordinaria (sem urgencia).
