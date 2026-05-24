---
name: analise-matriz-risco
description: >
  Analise da matriz de alocacao de riscos do contrato administrativo (art. 22 Lei 14.133/2021) - identifica riscos retidos pela Administracao x riscos transferidos ao contratado. Classifica por categoria: caso fortuito/forca maior (art. 393 CC), fato do principe, fato da Administracao, alea economica extraordinaria (art. 124 §1º). Avalia impactos no preco (BDI, encargos, reservas contingenciais), clausulas criticas e preparacao tecnica para futuro reequilibrio economico-financeiro (arts. 124-125). Identifica matriz enviesada (transferencia indevida ao contratado) como vicio passivel de impugnacao (PA-15). Aciona: matriz de risco, alocacao de risco, alea extraordinaria, fato do principe, fato da Administracao, caso fortuito contratual, reequilibrio futuro, BDI contingencial.
---

# ANALISE DA MATRIZ DE RISCO

> Skill **Tier 1** - analise tecnico-juridica da matriz de risco do contrato administrativo, definida no edital/TR e anexa ao contrato (art. 22 Lei 14.133/2021). Pre-requisito tecnico do `planejamento-proposta` e do futuro `reequilibrio-economico-financeiro`. Implementa P1, P2; respeita PA-15 (vinculacao).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `analise-oportunidade` ou `analise-etp-tr` quando o edital exibe matriz de risco (obrigatoria nos contratos de **maior vulto e de obras/servicos especiais** - art. 22 Lei 14.133). Tambem acionada por `contrato-administrativo` (Tier 4) na fase F4 quando ha negociacao de matriz no momento da assinatura ou aditivo.

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `analise-oportunidade`, `analise-etp-tr`, `contrato-administrativo`, `reequilibrio-economico-financeiro`.
- **Pre-requisito:** Selo emitido (PA-04).
- **Aciona em sequencia:** `deteccao-vicios-edital` (se matriz enviesada); `impugnacao-edital` (se vicio passivel); `planejamento-proposta` (incorporar reservas contingenciais ao BDI); `reequilibrio-economico-financeiro` no futuro (preserva base tecnica).
- **Entrega para:** parecer + tabela de classificacao de riscos por categoria/alocacao/probabilidade/impacto.

## 2. Marco normativo

- **Lei 14.133/2021:**
  - **art. 22** - matriz de alocacao de riscos (obrigatoria em obras/servicos especiais e contratos de maior vulto; facultativa em outros).
  - **art. 22 §3º** - matriz pode definir mecanismo de revisao para riscos identificados.
  - **art. 104 III** - clausula exorbitante de fiscalizacao.
  - **art. 124** - alteracao contratual; **§1º** - reequilibrio em caso de algum risco realizar (fato superveniente imprevisivel ou previsivel mas com consequencias incalculaveis - revisao); **art. 124 II d** - hipoteses de reequilibrio.
  - **art. 125** - aplicacao do reequilibrio; manutencao da equacao economico-financeira (CF art. 37 XXI).
- **CC art. 393** - caso fortuito e forca maior; **CC arts. 421-422** - boa-fé objetiva.
- **IN SEGES MGI:**
  - IN 73/2022 - gestao contratual.
  - IN 5/2017 SLTI (residual para repactuacao de mao-de-obra exclusiva).
- **CF art. 37 XXI** - manutencao da equacao economico-financeira como direito constitucional do contratado.
- **Jurisprudencia TCU 2020-2024** - reequilibrio em pandemia + inflacao 2022-2023 - acordaos consolidados (referenciar `[VERIFICAR - decisoes TCU 2024-2026]` quando aplicavel).

## 3. Estrutura canonica de uma matriz de risco

Cada risco listado conforme **5 dimensoes**:

1. **Identificacao** - codigo + descricao do evento.
2. **Categoria** - caso fortuito/forca maior; fato do principe; fato da Administracao; alea ordinaria; alea extraordinaria; risco do contratado.
3. **Probabilidade** - baixa/media/alta.
4. **Impacto** - baixo/medio/alto - quantificado se possivel.
5. **Alocacao** - quem responde: Administracao retida / Contratado transferido / Compartilhado.

## 4. Categorias de risco e regra de alocacao

| Categoria | Definicao | Alocacao tipica/correta |
|-----------|-----------|-------------------------|
| **Caso fortuito / forca maior** (CC art. 393) | Evento inevitavel e imprevisivel (terremoto, ato terrorista de grande proporcao) | Administracao (rescisao sem culpa - art. 137 IX Lei 14.133); reequilibrio se executar parcial |
| **Fato do principe** | Ato geral e abstrato do Estado que indiretamente impacta o contrato (mudanca de aliquota tributaria geral, modificacao normativa) | Administracao retida -> revisao (art. 124 §1º) |
| **Fato da Administracao** | Ato especifico da Administracao contratante que diretamente onera/dificulta a execucao (atraso de pagamento, demora em fornecer projeto, alteracao do local) | Administracao retida integralmente - revisao + suspensao + indenizacao se for o caso |
| **Alea ordinaria** | Risco proprio do negocio, previsivel pelo contratado (oscilacao normal de insumos, variacao cambial moderada) | Contratado retido - integrado ao BDI |
| **Alea extraordinaria** | Imprevisivel ou previsivel mas com consequencias incalculaveis (inflacao excepcional pandemia, choque de oferta especifico) | Compartilhado -> revisao (art. 124 §1º) |
| **Risco do contratado** | Inadimplemento culposo (atraso por falha tecnica, defeito de execucao) | Contratado retido + sancao se for o caso |

## 5. Matriz enviesada - vicios tipicos

Identificar quando matriz **transfere indevidamente** ao contratado riscos que deveriam ser da Administracao - vicio passivel de impugnacao (PA-15 + art. 164 Lei 14.133):

- **Fato da Administracao transferido ao contratado** - atraso de pagamento ou demora em projeto/licenca alocado ao contratado.
- **Caso fortuito/forca maior nao previstos** - matriz omissa contraria art. 393 CC + art. 137 IX Lei 14.133.
- **Alea extraordinaria como ordinaria** - ex.: variacao cambial "extrema" tratada como risco normal do contratado.
- **Vedacao implicita ao reequilibrio** - clausula que afasta art. 124 Lei 14.133 (revisao) - **nula** por contrariar CF art. 37 XXI.
- **Indices de reajuste ausentes** quando devidos (contratos contínuos - IN SEGES 5/2017 residual para mao-de-obra exclusiva).
- **Repactuacao vedada** em servicos contínuos com mao-de-obra exclusiva (vicio - direito legal a repactuacao anual).

## 6. Impacto no BDI

A matriz se traduz em **reservas contingenciais** no BDI da proposta:

- **Alea ordinaria** absorvida pelo BDI (lucro + despesas indiretas + tributos + reserva para variacoes pequenas).
- **Riscos compartilhados** com revisao prevista (art. 22 §3º) -> reserva menor + clausula de gatilho.
- **Riscos da Administracao retidos** -> sem reserva (ou minima por inadimplemento do `gestao-cronograma-fiscalizacao`).

**Output:** recomendar reservas contingenciais por categoria, suportadas pela matriz contratual. Vies da matriz inflaciona reserva -> impacta competitividade.

## 7. Preparacao tecnica para reequilibrio futuro

A matriz alocada hoje **e referencia para o futuro reequilibrio** (art. 124-125 Lei 14.133). Estrategia preventiva:

1. Documentar matriz original (anexo do contrato).
2. Monitorar cada risco listado durante a execucao.
3. Quando risco realizar, formalizar pedido administrativo de revisao/reajuste/repactuacao - matriz e prova pre-constituida.
4. Articular com `gestao-cronograma-fiscalizacao` (Tier 4) - notificacoes formais como prova.

## 8. Output - Parecer de matriz (formato)

```
PARECER MATRIZ DE RISCO
Edital/Contrato: [orgao + n° + objeto]
Data-base: [DD/MM/AAAA] · Selo: [referencia]

ESTRUTURA DA MATRIZ (5 dimensoes verificadas):
| Risco | Categoria | Probabilidade | Impacto | Alocacao | Avaliacao |

CLASSIFICACAO POR CATEGORIA (regra de alocacao):
- Caso fortuito/forca maior: [conforme / nao-conforme - art. 393 CC + art. 137 IX]
- Fato do principe: [conforme / nao-conforme - art. 124 §1º]
- Fato da Administracao: [conforme / nao-conforme]
- Alea ordinaria: [conforme / nao-conforme]
- Alea extraordinaria: [conforme / nao-conforme - art. 124 §1º]

VICIOS DA MATRIZ:
1. [vicio] - [base: lei + sumula TCU] - [impugnar / negociar / aceitar com reserva]

IMPACTO NO BDI:
- Reserva contingencial recomendada por categoria
- Comparacao com BDI base do segmento

ESTRATEGIA:
- Matriz limpa -> incorporar reservas e seguir
- Matriz enviesada -> [impugnar art. 164 / proposta com ressalva / nao participar]
- Preparar monitoramento para reequilibrio futuro (Tier 4)

[VERIFICAR]: [decisoes TCU 2024-2026 sobre alea extraordinaria pos-pandemia/inflacao]

---
[Ressalva OAB - PA-07]
```

## 9. Vedacoes especificas

- **PA-04** - Selo antes da analise.
- **PA-15** - vicios articulados na vinculacao ao instrumento.
- **PA-17** - vedado opinar sobre conveniencia administrativa (escolha por matriz de risco vs nao matriz quando facultativa); apenas vicios de legalidade quando matriz existe.
- **PA-11** - jurisprudencia TCU 2020-2024 reequilibrio pandemia/inflacao -> `[VERIFICAR]`.

## 10. Protocolos acionados

- **P1** - Selo.
- **P2** - integridade do anexo de matriz no edital.
- **P5** - regulamento local pode especificar matriz para certos objetos -> `[VERIFICAR - regulamento UF/Municipio]`.

## 11. Localizacao

Federal -> IN SEGES 73/2022; jurisprudencia TCU sobre alea extraordinaria. Estadual/municipal -> regulamento local complementando art. 22. Estatais (Lei 13.303/2016) -> regulamento interno proprio.

## 12. Integracao

**Chamada por:** `licitacoes-master`, `analise-oportunidade`, `analise-etp-tr`, `contrato-administrativo`, `reequilibrio-economico-financeiro`.

**Entrega para:** operador + `CASO.md`. Se matriz enviesada -> `deteccao-vicios-edital` + `impugnacao-edital`. Para a fase F4: `planejamento-proposta` (BDI), `gestao-cronograma-fiscalizacao` (monitoramento dos riscos), `reequilibrio-economico-financeiro` (quando risco realizar). Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** matriz aceita acriticamente; reservas contingenciais inadequadas; reequilibrio futuro sem base tecnica robusta.
