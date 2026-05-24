---
name: validador-legislacao-vigente
description: >
  Protocolo 1 do plugin. Valida vigencia normativa nos 4 niveis (federal + decreto + IN SEGES + estadual/municipal) e a jurisprudencia STJ/STF/TCU (Sumulas e Temas) NO REGIME APLICAVEL ao fato gerador. Eixo temporal Lei 14.133/2021 vs Lei 8.666/1993 (transicao consolidada 31/12/2023 - art. 191) + Decreto 11.246/2022 + Decreto 11.129/2022 (PAR) + IN SEGES 65/67/73/81/89; reforma da Lei 8.429/1992 pela Lei 14.230/2021 (Tema STF 1.199 pendente). Eixo geografico federal/estadual/municipal/estatal. Emite o Selo de Validacao Legal Previa - pre-requisito absoluto de toda peca, parecer, contrato, defesa e calculo de quantum (PA-04). Marca [VERIFICAR] em alvo movel (IN SEGES, regulamento local, sumula TCU em revisao). Aciona: validar legislacao, qual regime se aplica, lei vigente, datar fato gerador, Lei 14.133, Lei 8.666 transicao, art. 191, sumula TCU 222, 247, 248, 251, 269, 274, 277, 287, Tema 905, Tema 1.199, IN SEGES, Decreto 11.246, emitir o Selo.
---

# VALIDADOR DE LEGISLACAO VIGENTE

> Skill **Tier 0** - o Protocolo 1 em operacao. Pre-requisito absoluto de toda skill de producao (Tier 2-6). Emite o **Selo de Validacao Legal Previa**. Implementa PA-04, PA-09, PA-10, PA-11, PA-13.

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master` antes de toda producao, ou diretamente: "validar legislacao", "qual regime se aplica", "datar fato gerador", "a Lei 14.133 ou Lei 8.666 se aplica?". Recebe: norma(s) citada(s), tipo de procedimento/contrato, data do fato gerador, esfera do ente, UF de atuacao. Entrega: laudo de vigencia nos dois eixos + **Selo** registrado no `CASO.md`.

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master` (obrigatorio antes de Tier 2-6), `calendario-licitatorio`, qualquer skill que precise confirmar norma/jurisprudencia.
- **Entrega para:** a skill solicitante + campo `Selo de Validacao Legal Previa` no `CASO.md`.
- **Dependencia (PA-04):** **nenhuma producao opera sem o Selo.**

## 2. Os dois eixos do alvo movel

O direito das licitacoes muda em duas dimensoes:

- **Eixo temporal** - transicao Lei 8.666/1993 -> Lei 14.133/2021 (art. 191 - coexistencia consolidada em 31/12/2023 para novos procedimentos; contratos antigos seguem Lei 8.666 em toda execucao); Decreto 11.246/2022 (regulamenta Lei 14.133); Decreto 11.129/2022 (PAR Lei 12.846); IN SEGES MGI em mutacao (65/2021, 67/2021, 73/2022, 81/2022, 89/2023 e sucessoras); reforma Lei 8.429/1992 pela Lei 14.230/2021 (Tema STF 1.199 - pendente sobre retroatividade benefica). A norma aplicavel e a vigente **no fato gerador** (PA-03, PA-09).
- **Eixo geografico** - federal (JF + TCU); estadual (JE + TCE); municipal (JE + TCE ou TCM onde existir - SP capital, RJ, BA, GO, CE); estatal (regulamento interno - Lei 13.303/2016 art. 40). Regulamentos estaduais/municipais complementam Lei 14.133 (decretos proprios de SP, RJ, MG, BH, Recife etc.).

## 3. Os 8 passos do Protocolo 1

### Passo 1 - Datar o fato gerador / identificar o regime aplicavel

Data exata do edital, sessao publica, assinatura do contrato ou ato administrativo controvertido. Esta data + natureza do procedimento define regime (PA-03):
- **Procedimentos sob Lei 8.666/1993** e contratos celebrados antes de 31/12/2023 seguem Lei 8.666 em toda execucao (residual);
- **Procedimentos iniciados sob Lei 14.133** vao integralmente pela nova lei;
- **Regimes especiais:** Lei 13.303/2016 (estatais); Lei 11.079/2004 (PPP); Lei 8.987/1995 (concessao); Lei 12.232/2010 (publicidade); Lei 9.472/1997 (telecom).

Sem data -> perguntar: "Qual a data do edital ou do contrato? Ex: 15/03/2024."

### Passo 2 - Inventariar normas nos 4 niveis

- **Federal - Lei:** Lei 14.133/2021 (NLL); Lei 8.666/1993 (residual); Lei 11.079/2004 (PPP); Lei 8.987/1995 (concessao); Lei 13.303/2016 (estatais); Lei 12.846/2013 (Anticorrupcao); Lei 8.429/1992 + Lei 14.230/2021 (improbidade); Lei 12.016/2009 (MS); Lei 8.443/1992 (LOTCU); LC 123/2006 + LC 147/2014 (ME/EPP); Lei 9.784/1999 (PAD federal); CC arts. 421-426; CPC subsidiario.
- **Decretos federais:** Decreto 11.246/2022 (regulamenta Lei 14.133); Decreto 11.129/2022 (PAR); Decreto 10.024/2019 (pregao residual); Decreto 20.910/1932 (prescricao Fazenda).
- **IN SEGES MGI:** IN 65/2021 (pesquisa); IN 67/2021 (dispensa); IN 73/2022 (gestao); IN 81/2022 (dispensa eletronica); IN 89/2023 (catalogo). Sob revisao - `[VERIFICAR - atualizacao IN SEGES]`.
- **Estadual/Municipal:** decretos/leis complementando Lei 14.133 (SP, RJ, MG, Belo Horizonte, Recife); regulamentos de estatais (Banco do Brasil, Caixa, Petrobras). Sem confirmacao -> `[VERIFICAR - regulamento UF/Municipio]` (PA-11).

### Passo 3 - Validar vigencia no regime aplicavel

Cada norma: publicacao (DOU), vacatio, vigencia, revogacao expressa/tacita. Classificar: **VIGENTE / ALTERADA / REVOGADA / VACATIO / INDETERMINADO**. Distinguir redacao alterada por MP/lei - usar a do fato gerador, nao a atual (PA-03).

### Passo 4 - Validar sumulas TCU e jurisprudencia STJ/STF

**Sumulas TCU vivas em 2026** (status `[VERIFICAR - afetacao]`):
- **Sum. 222** - capacidade tecnico-operacional razoavel.
- **Sum. 247** - parcelamento do objeto para ampliar competitividade.
- **Sum. 248** - subcontratacao parcial quando expressamente prevista.
- **Sum. 251** - clausulas tecnicas justificadas, sem restricao indevida.
- **Sum. 269** - formalismo moderado na habilitacao - falha sanavel.
- **Sum. 274** - parcelamento + preclusao administrativa.
- **Sum. 277** - sigilo de informacoes sensiveis sem comprometer publicidade.
- **Sum. 287** - consorcios - participacao conjunta.

**Temas STJ/STF vivos:**
- **Tema 905 STJ** - Selic combinada para condenacoes contra Fazenda.
- **Tema 897 STF** - imprescritibilidade restrita em improbidade dolosa pre-reforma.
- **Tema 1.199 STF** - retroatividade benefica da Lei 14.230/2021 - **pendente** -> `[VERIFICAR]`.
- Jurisprudencia consolidada Lei 8.666 com aplicacao adaptada a Lei 14.133 - sinalizar regime.

**TCU como precedente** - forca persuasiva intensa; acordao vincula Administracao (CF art. 71 IX + Lei 8.443/1992).

### Passo 5 - Travar o regime aplicavel

| Tema | Pre-marco | Pos-marco |
|------|-----------|-----------|
| Procedimento licitatorio | Lei 8.666/1993 (residual contratos pre-31/12/2023) | Lei 14.133/2021 (novos pos-2023) |
| Pregao eletronico | Decreto 10.024/2019 (residual) | Lei 14.133 arts. 28, 32 + regulamentos sucessores |
| PAR | Decreto 8.420/2015 | Decreto 11.129/2022 |
| Improbidade | Lei 8.429/1992 redacao original | Lei 14.230/2021 (Tema STF 1.199 pendente) |
| Estatais | Lei 8.666 antes | Lei 13.303/2016 + regulamento interno |

### Passo 6 - Verificar regras locais e regulamentares

Decreto estadual/municipal complementando Lei 14.133 (fase preparatoria, lista de itens dispensaveis, dispensa eletronica local); regulamento interno de estatal (Lei 13.303 art. 40); manual do TCU (orientacoes). Sem confirmacao -> `[VERIFICAR - decreto local / regulamento estatal]` (PA-11).

### Passo 7 - Rastrear PL/MP/ADIN pendente

PL em tramitacao ou ADIN/ADC ajuizada que pode alterar o cenario (PLs sobre simplificacao da Lei 14.133; ADIs sobre Lei 14.230/2021 - Tema 1.199; ADIs sobre Lei 13.303). Sinalizar.

### Passo 8 - Emitir o Selo

## 4. Formato do Selo de Validacao Legal Previa

```
SELO DE VALIDACAO LEGAL PREVIA
Data-base: [DD/MM/AAAA]
Data do fato gerador: [DD/MM/AAAA]
Regime aplicavel: [Lei 14.133/2021 | Lei 8.666/1993 residual | Lei 13.303 | Lei 11.079 PPP | Lei 8.987 concessao]
Esfera: [federal | estadual | municipal | estatal]
Fase: [F1 pre-edital | F2 edital | F3 sessao/habilitacao | F4 contrato | F5 sancao/PAR | F6 TCU/TCE | F7 judicial]
Subdominio: [obras | servicos comuns | TIC | publicidade | concessao | PPP | estatal | dispensa | inexigibilidade]
Localizacao: [UF/Municipio - TCU/TCE/TCM aplicavel]
Normas validadas:
  Federal:    [Lei + ano + art.] - VIGENTE - redacao de [data]
  Decreto:    [Decreto + numero/ano] - VIGENTE
  IN SEGES:   [IN + numero/ano] - [VIGENTE | VERIFICAR atualizacao]
  Estadual/Municipal: [decreto local] - [VIGENTE | VERIFICAR]
Sumulas TCU vivas aplicaveis: [222 | 247 | 251 | 269 | 274 | 277 | 287 - status]
Jurisprudencia STJ/STF aplicavel: [Tema 905 | Tema 1.199 pendente | REsp/RE/ADI - status]
Foro/competencia: [administrativo (agente/autoridade) + TCU/TCE/TCM + JF/JE]
Alertas: [PL/MP pendente | sumula em revisao | IN SEGES atualizacao | Tema STF 1.199]
[VERIFICAR]: [pontos que demandam checagem manual]
Validade: reflete legislacao na data-base. Reverificar apos [data-base + 60 dias].
```

Selo registrado em `memoria-de-caso-licitacao` (`CASO.md`). Skill de producao sem Selo aciona esta primeiro.

## 5. Flag de norma desatualizada

```
[ALERTA NORMATIVO]
A norma citada ([Lei X art. Y]) nao se aplica ao fato gerador de [data].
Motivo: [revogada por / alterada por / substituida por / regime diverso]
Norma aplicavel ao periodo: [Z]
Acao: [substituir / verificar texto vigente / aguardar regulamentacao]
```

Nunca prosseguir com norma REVOGADA sem confirmacao expressa do operador.

## 6. Casos transitorios criticos (alvo movel)

- **Lei 14.133 vs Lei 8.666 (art. 191)** - contratos pre-31/12/2023 sob Lei 8.666 residual; novos sob Lei 14.133.
- **Pregao** - Decreto 10.024/2019 residual; pos-Lei 14.133 arts. 28, 32 e sucessores.
- **PAR** - Decreto 8.420/2015 anterior; Decreto 11.129/2022 atual.
- **Improbidade Lei 14.230/2021** - retroatividade benefica em debate (Tema STF 1.199) -> `[VERIFICAR]`.
- **IN SEGES** - 65/67/73/81/89 em revisao - `[VERIFICAR - atualizacao]`.

## 7. Vedacoes especificas

- **PA-03/09** - a redacao atual nao substitui a redacao do regime aplicavel.
- **PA-04** - Selo nao emitido = producao bloqueada.
- **PA-10** - vedado citar sumula TCU/Tema revogado, superado ou em revisao sem ressalva.
- **PA-11** - alvo movel ou regra local nao confirmada -> `[VERIFICAR]`. Nunca inventar numero de IN, decreto local ou acordao TCU.
- **PA-13** - toda norma com lei+artigo+ano, jurisprudencia com tribunal+turma+numero+ano + sumula TCU com numero e tema.
- Nunca emitir Selo sem completar os 8 passos.

## 8. Protocolos acionados

- **P1** - esta skill **e** o Protocolo 1.
- **P5 - Localizacao** - Passo 6 aplica o eixo geografico (federal/estadual/municipal/estatal).

## 9. Localizacao

A localizacao e estrutural da validacao. Le esfera do ente + cidade + UF (do `CASO.md`). O Selo so e emitido com localizacao identificada - eixo geografico determina TCU x TCE x TCM, JF x JE, regulamento local aplicavel. Regra local nao confirmada -> `[VERIFICAR - regulamento UF/Municipio]` no Selo (PA-11).

## 10. Integracao

**Chamada por:** `licitacoes-master` (obrigatorio antes de Tier 2-6), `calendario-licitatorio`, qualquer skill que receba citacao de norma.

**Entrega para:** a skill de producao + campo `Selo` no `CASO.md`. Entrega final passa por `revisao-final-licitacoes` (R1-R4).

**Sem esta skill:** nenhuma producao opera (PA-04). Invariante (nao-removivel).
