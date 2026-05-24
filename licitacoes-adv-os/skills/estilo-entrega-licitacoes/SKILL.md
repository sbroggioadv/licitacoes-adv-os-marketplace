---
name: estilo-entrega-licitacoes
description: >
  Camada 3 - estrutura canonica de peca administrativa/judicial em licitacoes. FIRAC + 6 SECOES: (1) Fato - narrativa cronologica datada do procedimento; (2) Issue - questao controvertida; (3) Regra - lei+artigo+ano + decreto/IN + sumula TCU + jurisprudencia STJ/STF (fundamentacao tripla canonica); (4) Analise - subsuncao + vinculacao ao instrumento (PA-15); (5) Conclusao - pedido principal + sucessivos + tutela; (6) Bloco final padronizado - RESSALVA OAB obrigatoria (PA-07) + lista [VERIFICAR]. Memoria de quantum auditavel (P3) + Tema 905 STJ. Templates de fechamento padronizados. Garante fundamentacao tripla (lei + sumula TCU + jurisprudencia) em toda peca aplicavel + vinculacao ao edital em toda tese (PA-15). Aciona: estilo, FIRAC, formato da peca, ressalva OAB, bloco final, memoria de quantum, fundamentacao tripla.
---

# ESTILO E ENTREGA - CAMADA 3

> Skill **transversal invariante** - Camada 3 da Hierarquia Operacional. Estrutura canonica de peca/parecer + memoria de quantum + ressalva OAB. Implementa P3, PA-07, PA-13, PA-15.

---

## 0. Escopo e acionamento

Acionada por **toda** skill de producao (Tier 2-6) durante a elaboracao da peca - garantindo aderencia ao formato canonico. Tambem chamada pelo `revisao-final-licitacoes` em R4 (entrega e clareza). Recebe: rascunho da peca + contexto do caso. Entrega: peca formatada no padrao canonico + ressalva OAB + memoria de quantum quando aplicavel.

## 1. Posicao na orquestra

- **Chamada por:** **toda skill de producao** (impugnacao-edital, recurso-administrativo, contrarrazoes-recurso, defesa-apenamento-art-156, par-lei-12846, acordo-leniencia, representacao-tcu-tce, ms-licitacao-contrato, acao-anulatoria-licitacao, acao-cobranca-administracao, reequilibrio-economico-financeiro, rescisao-contrato).
- Tambem chamada por: `revisao-final-licitacoes` para verificar R4.
- **Entrega para:** skill chamadora (peca formatada).

## 2. Marco normativo

- **PA-07** - **ressalva OAB obrigatoria** em toda saida.
- **PA-13** - citacao precisa: lei+artigo+ano; sumula TCU n°+tema; jurisprudencia tribunal+turma+n°+ano.
- **PA-15** - vinculacao ao instrumento articulada em todo argumento.
- **P3** - memoria de decisao + quantum auditavel.
- **EAOAB art. 1º** - privatividade da advocacia (rascunho = nao substitui o advogado OAB ativo).
- **Tema 905 STJ** - Selic combinada para condenacoes contra Fazenda.

## 3. Estrutura canonica - FIRAC + 6 secoes (peca administrativa/judicial)

```
[CABECALHO]
EXMO. [AUTORIDADE COMPETENTE]
PROCESSO N° [n°] - [identificacao]

[Nome do tipo de peca: IMPUGNACAO / RECURSO / CONTRARRAZOES / DEFESA / REPRESENTACAO / MS / ANULATORIA / COBRANCA]
(art. [N°] [Lei] - prazo + base legal)

[SECAO 1 - F: Fato]
I - DOS FATOS
[Narrativa cronologica datada: edital + sessao + ato + recurso/decisao;
todos os marcos relevantes com data + base documental]

[SECAO 2 - I: Issue]
II - DA QUESTAO CONTROVERTIDA / DO INTERESSE LEGITIMO
[Definicao precisa da questao impugnavel - qual ato + qual vicio + qual
direito violado]

[SECAO 3 - R: Regra (fundamentacao tripla)]
III - DO DIREITO
III.1 - Da base legal (PA-13)
- [Lei 14.133/2021 art. X §Y - redacao vigente]
- [Lei 8.666/1993 residual quando aplicavel]
- [Decreto 11.246/2022 / IN SEGES 65/67/73/81/89 quando aplicavel]

III.2 - Das sumulas TCU (PA-13)
- Sum. TCU [n°] - [tema literal]
- Sum. TCU [n°] - [tema literal]

III.3 - Da jurisprudencia STJ/STF (PA-13)
- [Tema [n°] STJ - ementa] / [REsp [n°]/[ano] - turma - relator]
- [RE [n°]/[ano] - STF / ADI [n°] - ano]

III.4 - Da vinculacao ao instrumento (PA-15 + art. 12 Lei 14.133)
[Articulacao do principio + como o ato impugnado afasta-se do edital]

[SECAO 4 - A: Analise]
IV - DA APLICACAO DO DIREITO AOS FATOS
IV.1 - Subsuncao
[Fato narrado -> norma + sumula + jurisprudencia]

IV.2 - Vinculacao ao instrumento (reforco PA-15)

IV.3 - Refutacao de contra-argumentos previsiveis

IV.4 - Sum. TCU 269 (formalismo moderado) quando aplicavel

[SECAO 5 - C: Conclusao]
V - DOS PEDIDOS

a) [Conhecimento + admissibilidade];
b) [Pedido principal - mais brando / vinculado ao fato];
c) [Pedidos sucessivos - escala crescente]:
   - Sucessivo 1: [retificacao / correcao]
   - Sucessivo 2: [anulacao parcial]
   - Sucessivo 3: [anulacao total]
d) [Tutela cautelar / liminar quando aplicavel - fumus + periculum];
e) [Coordenacao com via paralela P4 quando estrategico];
f) [Quantum quando aplicavel - cumulacao].

[SECAO 6 - Bloco final padronizado]
VI - DOCUMENTOS ANEXOS
- Procuracao OAB ativa (PA-05, PA-07)
- [Documentos especificos]

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}}
OAB/{{OAB_UF}} {{OAB_NUMERO}}
{{FIRM_NAME}}

---
[Ressalva OAB obrigatoria - PA-07]
Esta peça é rascunho técnico-operacional gerado por ferramenta de apoio à
advocacia. A revisão final, conferência probatória e responsabilidade técnica
pela versão entregue à Administração, ao TCU/TCE, ao juízo ou ao cliente é
do(a) advogado(a) inscrito(a) na OAB com situação ativa.

Selo de Validação Legal Prévia emitido em [DD/MM/AAAA] - ver CASO.md.
Pontos sinalizados [VERIFICAR]: [lista pontual de pontos em alvo movel
ou em dependencia de regulamento local].
---
```

## 4. Estrutura para parecer/diagnostico (consultivo)

```
[CABECALHO]
PARECER [TIPO]
Caso: [slug]
Data-base: [DD/MM/AAAA] · Selo: [referencia]

I - OBJETO DO PARECER
[Pergunta consultiva especifica]

II - CONTEXTO FATICO
[Narrativa cronologica datada]

III - ANALISE JURIDICA
III.1 - Base normativa (PA-13)
III.2 - Sumulas TCU aplicaveis (PA-13)
III.3 - Jurisprudencia consolidada (PA-13)
III.4 - Vinculacao ao instrumento (PA-15)

IV - CENARIOS / RECOMENDACOES
IV.1 - Cenario A: [descricao + probabilidade tecnica - PA-02 sem promessa]
IV.2 - Cenario B: [...]
IV.3 - Cenario C: [...]

V - PONTOS DE ATENCAO
- [risco] - [mitigacao]
[lista]

VI - RECOMENDACAO
[Posicao tecnica - sem promessa de resultado - PA-02]
[Eventualmente apresenta opcoes - conforme MODO_MELHOR_SAIDA]

---
[Ressalva OAB - PA-07]

[VERIFICAR]: [pontos em alvo movel]
```

## 5. Memoria de quantum (P3) - estrutura padrao

```
MEMORIA DE QUANTUM
Caso: [slug] · Selo: [referencia]

| Item | Base legal | Valor original | Atualizacao | Total |
|------|-----------|----------------|-------------|-------|
| Pagamento atrasado | art. 141 Lei 14.133 + CC | R$ A | Selic Tema 905 STJ desde [data] | R$ B |
| Reequilibrio (revisao) | art. 124 §1º Lei 14.133 | R$ C | Selic desde [data] | R$ D |
| Indenizacao (anulacao) | art. 149 Lei 14.133 (boa-fé) | R$ E | Selic | R$ F |
| Multa (defesa de) | art. 156 §3º Lei 14.133 | R$ G | conforme decisao | R$ H |
| Perdas e danos | CC art. 944 + art. 402 | R$ I | Selic | R$ J |
| **Total pleiteado** | - | - | - | **R$ TOTAL** |

PRINCIPIOS APLICADOS:
- Conservadorismo (P3): valores ancorados em parametros consolidados
- Selic combinada (Tema 905 STJ): atualizacao para condenacoes contra Fazenda
- Origem real dos dados (PA-22): nao presumir; dado faltante = solicitar
- Sigilo da planilha (PA-09): em `<cwd>/.../casos/<slug>/arquivos/` gitignored
```

## 6. Bloco final padronizado - ressalva OAB (PA-07)

```
---
Esta peça/parecer/contrato/defesa é rascunho técnico-operacional gerado por
ferramenta de apoio à advocacia. A revisão final, conferência probatória e
responsabilidade técnica pela versão entregue à Administração, ao TCU/TCE, ao
juízo ou ao cliente é do(a) advogado(a) inscrito(a) na OAB com situação ativa.

Selo de Validação Legal Prévia emitido em [data] — ver CASO.md.
Pontos sinalizados [VERIFICAR]: [lista].
---
```

**Obrigatoriedade absoluta** (PA-07). Sem este bloco -> BLOQUEADO em R3 da `revisao-final-licitacoes`.

## 7. Fundamentacao tripla (PA-13) - canon

Toda tese articulada com **3 ancoras**:

1. **Norma legal** - Lei 14.133/2021 (ou Lei 8.666 residual) com **art. + redacao vigente no regime aplicavel**.
2. **Sumula TCU** - **numero + tema literal** (das vivas: 222, 247, 248, 251, 269, 274, 277, 287).
3. **Jurisprudencia STJ/STF** - **Tema/REsp/RE/ADI** + tribunal + turma + ano.

Genericismo ("a lei diz", "o TCU entende") = vedado (PA-13). Cada afirmacao tem ancoras precisas.

## 8. Vinculacao ao instrumento (PA-15) - vetor comum

Em toda peca, articular como o ato impugnado / a clausula contratual desvia-se ou cumpre a vinculacao ao edital. **Vetor comum** que conecta fato + norma + tese.

## 9. Vedacoes especificas

- **PA-07** - ressalva OAB obrigatoria. **PA-13** - citacao precisa. **PA-15** - vinculacao.
- **PA-02** - sem promessa de resultado.
- **PA-08** - sem critica pessoal a agente/conselheiro/magistrado.
- **PA-17** - sem juizo sobre discricionariedade.
- **PA-11** - `[VERIFICAR]` explicito em alvo movel.

## 10. Protocolos acionados

- **P3** - esta skill **estrutura** a memoria de decisao + quantum.
- Verifica integracao com **P1** (Selo), **P2** (documentos), **P5** (foro), **P6** (R1-R4).

## 11. Localizacao

A estrutura e nacional, mas:
- Esfera federal -> cita Lei 14.133 + Decreto 11.246 + IN SEGES + TCU.
- Estadual/municipal -> cita Lei 14.133 + regulamento local + TCE/TCM.
- Estatais (Lei 13.303/2016) -> cita regulamento interno.

## 12. Integracao

**Chamada por:** todas as skills de producao (Tier 2-6); `revisao-final-licitacoes` em R4.

**Entrega para:** skill chamadora (peca formatada) ou diretamente ao operador apos R1-R4.

**Sem esta skill:** entregas sem padronizacao - perda de qualidade tecnica; ressalva OAB ausente (violacao PA-07); fundamentacao generica (violacao PA-13); memoria de quantum sem rastreabilidade.

**Esta skill e INVARIANTE** (state-schema `skills.invariants`) - nao removivel.
