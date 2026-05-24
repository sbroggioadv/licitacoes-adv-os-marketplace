---
name: programa-integridade-compliance
description: >
  Programa de integridade (art. 7º VIII Lei 12.846/2013 + Decreto 11.129/2022 arts. 56-58) - atenuante de sancao em PAR ate 4% da pena base. 16 PARAMETROS DE AVALIACAO: compromisso da alta direcao; codigo de etica; treinamentos periodicos; canais de denuncia; due diligence de terceiros; controles internos contabeis; investigacoes internas; monitoramento; risk assessment; procedimentos de prevencao especificos para contratacoes publicas; medidas em razao de novos arranjos societarios (M&A); transparencia em doacoes politicas; mecanismos de remediacao; clareza de papeis e responsabilidades; medidas disciplinares; verificacoes periodicas. Compliance PREVENTIVO da empresa contratada + preparacao para defesa em PAR. Aciona: programa de integridade, compliance publico, 16 parametros, atenuante PAR, Decreto 11.129/2022, codigo de etica, canal de denuncia, due diligence.
---

# PROGRAMA DE INTEGRIDADE E COMPLIANCE

> Skill **Tier 5** - construcao + avaliacao do programa de integridade da PJ. Atenuante de PAR (Decreto 11.129/2022 arts. 56-58 - ate 4% da pena base). Compliance preventivo + defesa. Implementa P1, P3, P5; respeita PA-15, PA-18 (fronteira sem cross-sell).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `/sancao`, `par-lei-12846` (para fundamentar atenuante), ou demanda consultiva (preparacao preventiva de PJ que pretende contratar com Administracao). Recebe: situacao atual de compliance da PJ + objetivos + risco de PAR.

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/sancao`, `par-lei-12846`, `acordo-leniencia`, `analise-oportunidade` (preparacao para participar de certame).
- **Pre-requisito:** Selo (PA-04); dados internos da PJ (sigilo PA-09).
- **Aciona em sequencia:** `par-lei-12846` para fundamentar atenuante em defesa; `acordo-leniencia` integrado a programa como compromisso futuro.
- **Entrega para:** diagnostico do programa + plano de implementacao/aprimoramento + documentacao para usar em PAR.

## 2. Marco normativo

- **Lei 12.846/2013:**
  - **art. 7º VIII** - programa de integridade efetivo como **atenuante** na dosimetria.
- **Decreto 11.129/2022:**
  - **art. 56** - definicao de programa de integridade.
  - **art. 57** - **16 parametros de avaliacao** (criterios de efetividade).
  - **art. 58** - **atenuante de ate 4% da pena base** quando programa atende parametros.
- **CGU - Programa Pro-Etica** - reconhecimento publico de PJs com programa efetivo (atestado).
- **Lei 14.133/2021 art. 25 §4º** - exigencia de programa de integridade em contratos de grande vulto.
- **LGPD (Lei 13.709/2018)** - integracao com tratamento de dados (interface).
- **Sumulas TCU:** programa de integridade na fase preparatoria + dosimetria sancionatoria.

## 3. Os 16 parametros (Decreto 11.129/2022 art. 57)

### Bloco A - Governanca (1-4)

1. **Compromisso da alta direcao** - declaracao formal + acoes concretas + recursos alocados.
2. **Codigo de etica e de conduta** - aplicavel a todos os colaboradores + terceiros; pratica + revisao periodica.
3. **Politicas e procedimentos especificos de integridade** - especialmente para contratacoes publicas.
4. **Treinamentos periodicos** - todos os niveis hierarquicos; documentados; com avaliacao de aprendizagem.

### Bloco B - Riscos e controles (5-8)

5. **Identificacao e analise de riscos de integridade** - risk assessment formal + atualizacao periodica.
6. **Registros contabeis confiaveis e completos** - controles internos efetivos.
7. **Controles internos** que garantam confiabilidade dos relatorios financeiros + da execucao contratual.
8. **Medidas de prevencao** especificas para **contratacoes publicas** - segregacao de funcoes, dupla aprovacao, registros.

### Bloco C - Terceiros e M&A (9-10)

9. **Due diligence de terceiros** (fornecedores, parceiros, intermediarios) + integracao em contratos privados (clausulas anticorrupcao).
10. **Diligencia em arranjos societarios** (fusoes, aquisicoes, joint ventures, consorcios) - avaliacao de risco do parceiro + clausulas de protecao.

### Bloco D - Denuncia, investigacao, monitoramento (11-14)

11. **Canais de denuncia** - acessibilidade + sigilo + protecao ao denunciante (Lei 13.608/2018).
12. **Investigacoes internas** estruturadas - mecanismos formais + relatorios independentes.
13. **Monitoramento continuo** do programa - indicadores + relatorios periodicos a alta direcao.
14. **Medidas disciplinares** - aplicacao consistente; documentadas.

### Bloco E - Transparencia + remediacao (15-16)

15. **Transparencia em doacoes politicas** (interface com Lei 9.504/1997 - doacoes empresariais vedadas em campanha desde EC + decisoes STF; doacoes a fundacoes/causas com transparencia).
16. **Mecanismos de remediacao** - reparacao + medidas corretivas + cooperacao com autoridades.

## 4. Avaliacao do programa - matriz de maturidade

```
MATRIZ DE MATURIDADE DO PROGRAMA - CASO [slug PJ]

| Parametro | Existe? | Implementado? | Documentado? | Eficaz? | Nivel |
| 1. Alta direcao | sim/nao | sim/nao | sim/nao | sim/nao | inicial/intermediario/avancado |
| 2. Codigo de etica | ... | ... | ... | ... | ... |
| [continuar 16 itens]

CLASSIFICACAO GLOBAL:
- Inicial: 0-5 parametros efetivos
- Intermediario: 6-10
- Avancado: 11-16 (eligivel ao programa Pro-Etica CGU)
```

## 5. Estrategia - 3 cenarios

### 5.1 - Implementacao preventiva (consultivo)
- PJ pretende contratar com Administracao -> implementar programa antes de eventual PAR.
- Beneficios: atenuante futura; participacao em editais que exijam programa (Lei 14.133 art. 25 §4º); reputacional.

### 5.2 - Atenuante em PAR ja instaurado
- PJ tem programa preexistente -> documentar em defesa do PAR.
- Decreto 11.129/2022 arts. 56-58 - **atenuante de ate 4% da pena base** dependendo da efetividade.
- Integracao com `par-lei-12846`.

### 5.3 - Compromisso em acordo de leniencia
- Programa **reforcado** como contrapartida em acordo de leniencia.
- Monitoramento por CGU/controladoria.
- Integracao com `acordo-leniencia`.

## 6. Estrutura - parecer/diagnostico

```
PARECER DE PROGRAMA DE INTEGRIDADE - CASO [slug PJ]
Data-base: [DD/MM/AAAA] · Selo: [referencia]

CENARIO: [preventivo / atenuante em PAR n° X / compromisso em leniencia]

DIAGNOSTICO DOS 16 PARAMETROS (Decreto 11.129/2022 art. 57):

Bloco A - Governanca:
1. Alta direcao: [nivel + acoes]
2. Codigo de etica: [...]
3. Politicas: [...]
4. Treinamentos: [...]

Bloco B - Riscos e controles: [5-8]
Bloco C - Terceiros e M&A: [9-10]
Bloco D - Denuncia/investigacao/monitoramento: [11-14]
Bloco E - Transparencia/remediacao: [15-16]

NIVEL GLOBAL: [inicial / intermediario / avancado]

GAPS IDENTIFICADOS:
1. [parametro] - acao corretiva: [...]
[lista priorizada]

PLANO DE ACAO (6-12 meses):
- Fase 1 (1-3m): [acoes prioritarias]
- Fase 2 (3-6m): [implementacao]
- Fase 3 (6-12m): [monitoramento + revisao]

ATENUANTE EM PAR (se aplicavel):
- Documentacao dos parametros para defesa em `par-lei-12846`
- Estimativa de atenuante: [0-4% da pena base]

INTEGRACAO COM LENIENCIA (se aplicavel):
- Programa reforcado como compromisso (`acordo-leniencia`)

ATENCAO PA-18:
- Aspectos trabalhistas (regulamento interno + relacoes CLT) -> "encaminhar
  a especialista trabalhista" sem citar produto irmao.
- Aspectos LGPD (Lei 13.709/2018) -> integracao com programa de protecao de dados;
  fronteira com plugin de protecao de dados (futuro) - slot generico.

[VERIFICAR]: [atualizacoes Decreto 11.129/2022; Programa Pro-Etica CGU]

---
[Ressalva OAB - PA-07]
```

## 7. Vedacoes especificas

- **PA-04** Selo. **PA-09** sigilo de dados internos da PJ (politicas, treinamentos, denuncias).
- **PA-15** integracao com clausulas anticorrupcao em contratos privados + clausulas exigidas pelo edital.
- **PA-18** - fronteiras com (trabalhista, LGPD, penal) sinalizadas sem citar produto.
- **PA-02** vedada promessa de atenuante - depende de efetividade real.
- **PA-07** ressalva OAB.

## 8. Protocolos acionados

- **P1** Selo. **P3** memoria de decisao para fundamentar atenuante (rastreabilidade dos 16 parametros). **P5** competencia (CGU/controladoria).

## 9. Localizacao

Federal -> CGU (Programa Pro-Etica). Estadual/municipal -> controladorias locais com programas analogos. Estatais -> regulamento interno (Lei 13.303/2016 art. 9º - exige programa).

## 10. Integracao

**Chamada por:** `licitacoes-master`, `/sancao`, `par-lei-12846`, `acordo-leniencia`, `analise-oportunidade`.

**Entrega para:** parecer + plano de acao + documentacao para defesa em PAR + `CASO.md`. Integracao com `par-lei-12846` (fundamentar atenuante) e `acordo-leniencia` (compromisso futuro). Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** programa de integridade ausente ou ineficaz - perda da atenuante de ate 4% em PAR; risco reputacional; vedacao em editais que exijam programa (Lei 14.133 art. 25 §4º).
