---
name: analise-etp-tr
description: >
  Analise tecnico-juridica do Estudo Tecnico Preliminar (art. 18 Lei 14.133/2021) e do Termo de Referencia (art. 6º XXIII Lei 14.133/2021) - documentos da fase interna que estruturam o edital. Verifica completude, justificativa da contratacao, pesquisa de precos (IN SEGES 65/2021), solucoes de mercado, parcelamento (Sum. TCU 247, 274), definicao do objeto, especificacoes tecnicas (vedada marca/modelo direcionado - art. 7º), criterios de aceitabilidade, prazos. Identifica exigencias restritivas precoces preparando impugnacao futura (vinculacao - PA-15). Apoia acesso via LAI (Lei 12.527/2011) quando documentos nao publicados. Aciona: analisar ETP, analisar TR, termo de referencia, estudo tecnico preliminar, pesquisa de precos, parcelamento, especificacao tecnica restritiva, marca direcionada.
---

# ANALISE DE ETP E TERMO DE REFERENCIA

> Skill **Tier 1** - analise dos documentos da fase interna do procedimento (ETP + TR). Pré-requisito ideal para `analise-edital`. Implementa P1, P2; respeita PA-15 (vinculacao), PA-11 ([VERIFICAR] em alvo movel).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master` ou `analise-oportunidade` quando ha acesso ao ETP/TR - publicados juntos ao edital (regra) ou obtidos via LAI (Lei 12.527/2011) antes da publicacao do edital. Recebe: ETP + TR + planilha estimativa (orçamento) + matriz de risco + minuta contratual, em `<cwd>/licitacoes/casos/<slug>/arquivos/` (PA-09).

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `analise-oportunidade`, `/triagem` (fase F1 ou inicio F2).
- **Pre-requisito:** Selo emitido (PA-04).
- **Aciona em sequencia:** `deteccao-vicios-edital` (se identifica vicio passivel de impugnacao); `analise-matriz-risco` (paralelo).
- **Entrega para:** parecer tecnico sobre consistencia do ETP/TR + lista de exigencias restritivas + roteiro para futura impugnacao (se for o caso).

## 2. Marco normativo

- **Lei 14.133/2021:**
  - art. 18 - **ETP** obrigatorio (descricao da necessidade, requisitos da contratacao, estimativa do quantitativo, levantamento de mercado, justificativa de parcelamento ou nao, demonstrativo da previsao orcamentaria, providencias para adequacao, contratacoes correlatas, possiveis impactos ambientais).
  - art. 6º XXIII - **TR** (definicao do objeto, fundamentacao da contratacao, descricao da solucao, requisitos da contratacao, modelo de execucao, modelo de gestao, criterios de medicao e pagamento, forma e criterios de selecao do fornecedor, estimativa do valor, adequacao orcamentaria).
  - art. 7º - vedacao a especificacoes restritivas (marca/modelo) - excecoes justificadas.
  - art. 22 - matriz de alocacao de riscos.
  - art. 23 - estimativa de valor (pesquisa de precos).
  - art. 24 - confidencialidade do orcamento estimativo - regra excepcional, conforme estrategia.
- **Lei 12.527/2011 (LAI):** acesso a informacao - ETP e TR sao publicos apos finalizacao da fase interna, salvo classificacao restrita.
- **IN SEGES MGI:**
  - IN 65/2021 - pesquisa de precos (parametros, fontes, metodos).
  - IN 73/2022 - gestao contratual.
  - IN 89/2023 - catalogo padronizado.
- **Sumulas TCU:**
  - **Sum. 247** - parcelamento do objeto para ampliar competitividade.
  - **Sum. 274** - parcelamento + preclusao administrativa.
  - **Sum. 251** - clausulas tecnicas justificadas, sem restricao indevida.

## 3. Checklist de analise do ETP (art. 18)

1. **Descricao da necessidade** - real ou ficticia? Fundamentacao adequada?
2. **Requisitos da contratacao** - tecnicos justificados? Restricoes a competitividade?
3. **Estimativa de quantitativo** - metodologia? Consistencia com a demanda demonstrada?
4. **Levantamento de mercado** - quantos fornecedores potenciais? Pesquisa abrangente?
5. **Justificativa de parcelamento** - **se nao parcelado, exige justificativa robusta** (Sum. TCU 247, 274). Parcelamento e regra; nao-parcelamento e excecao motivada.
6. **Previsao orcamentaria** - LDO/LOA compativel? Dotacao indicada?
7. **Adequacao** - infraestrutura, equipe, capacitacao para receber o objeto?
8. **Contratacoes correlatas** - dependencias com outros contratos?
9. **Impactos ambientais** - quando aplicavel.

## 4. Checklist de analise do TR (art. 6º XXIII)

1. **Definicao do objeto** - precisa, sem ambiguidade, sem especificacao tecnica restritiva (art. 7º).
2. **Fundamentacao da contratacao** - alinhada ao ETP.
3. **Descricao da solucao** - solucao especifica vs ampla? Vies para fornecedor unico?
4. **Requisitos da contratacao** - prazos, locais, condicoes, garantia, sustentabilidade.
5. **Modelo de execucao** - regime (empreitada por preco global/unitario/integral, contratacao por escopo) - consistente com objeto.
6. **Modelo de gestao** - papeis (fiscal tecnico, fiscal administrativo, gestor), rotinas.
7. **Criterios de medicao e pagamento** - clareza; vinculo ao art. 141 (ordem cronologica).
8. **Forma e criterios de selecao** - criterio de julgamento (menor preco / tecnica e preco / maior desconto / maior retorno economico - art. 33) compativel com objeto?
9. **Estimativa do valor** - pesquisa de precos conforme IN SEGES 65/2021 (3 fontes minimas; mediana; mais aplicavel ao objeto).
10. **Adequacao orcamentaria** - cobertura confirmada.

## 5. Top vicios precoces detectaveis em ETP/TR

Identificados aqui ja preparam **impugnacao** futura (PA-15 + arts. 164 Lei 14.133):

- **Marca/modelo direcionado** (art. 7º Lei 14.133) - especificacao tecnica que so um fornecedor atende. Justificativa tecnica robusta exigida.
- **Capacidade tecnica desproporcional** (Sum. TCU 222) - atestados que excedem o razoavel.
- **Atestados especificos demais** (objeto + quantitativo + local) - Sum. TCU 247.
- **Parcelamento nao justificado** (Sum. TCU 247, 274) - obrigatorio se viavel tecnico/economicamente.
- **Visita tecnica obrigatoria sem necessidade** - restringe competitividade.
- **Prazo de execucao incompativel** com objeto.
- **Garantia desproporcional** (>5% sem ser obra de grande vulto - art. 96).
- **Indices economico-financeiros sem justificativa** (art. 69 + Sum. TCU 251).
- **Profissional do quadro permanente** desnecessario para natureza do objeto.
- **Pesquisa de precos frágil** - menos de 3 fontes, fontes nao representativas, mediana fora de mercado (IN SEGES 65/2021).
- **Subcontratacao vedada quando o objeto admite** (Sum. TCU 248).
- **Confidencialidade do orcamento estimativo nao justificada** (art. 24 - regra excepcional).

## 6. Estrategia consultiva

**Diligencia preparatoria via LAI** (Lei 12.527/2011): se documentos nao publicados antes do edital, pedir acesso administrativo - cria registro probatorio, provoca pronunciamento da Administracao e fortalece eventual impugnacao.

**Esclarecimento vs impugnacao** (fronteira com `esclarecimento-edital`, `impugnacao-edital`): esclarecimento dirime duvida sem questionar legalidade; impugnacao aponta vicio. Esclarecimento estrategico antes da impugnacao gera pronunciamento que pode embasar a impugnacao depois.

**Compatibilidade com matriz de risco** (paralelo a `analise-matriz-risco`): se ETP/TR ja apresentam matriz de risco enviesada (riscos sem correlacao + transferencia indevida ao contratado), sinalizar para impugnacao especifica.

## 7. Output - Parecer de ETP/TR (formato)

```
PARECER ETP/TR
Edital: [orgao + n° processo + objeto]
Documentos analisados: [ETP / TR / planilha estimativa / matriz de risco / minuta]
Data-base: [DD/MM/AAAA] · Selo: [referencia]

ETP - CHECKLIST (9 itens):
[ ] Descricao da necessidade ... [conforme / nao-conforme / lacuna]
[continuar com os 9]

TR - CHECKLIST (10 itens):
[ ] Definicao do objeto ... [conforme / nao-conforme]
[continuar com os 10]

VICIOS PRECOCES DETECTADOS:
1. [vicio] - [base legal: lei + sumula TCU] - [estrategia: impugnacao / esclarecimento]
[...]

ESTRATEGIA CONSULTIVA:
- [Diligencia LAI / esclarecimento / impugnacao / continuar para analise-edital]
- Prazos: impugnacao 3 dias uteis art. 164 (apos publicacao do edital)

[VERIFICAR]: [pontos em alvo movel - IN SEGES atualizacao]

---
[Ressalva OAB - PA-07]
```

## 8. Vedacoes especificas

- **PA-04** - Selo antes da analise.
- **PA-09 + PA-22** - sigilo de proposta da PJ-cliente; ETP/TR do orgao sao publicos mas conferencia em `<cwd>/.../casos/<slug>/arquivos/`.
- **PA-11** - `[VERIFICAR]` em IN SEGES (alvo movel) e regulamento local.
- **PA-15** - vicios articulados na vinculacao ao instrumento.
- **PA-17** - vedado opinar sobre escolha do criterio de julgamento (discricionariedade); apenas vicios de legalidade.

## 9. Protocolos acionados

- **P1** - Selo.
- **P2** - conferencia de integridade do ETP/TR (completude dos 9+10 itens).
- **P5** - esfera do ente afeta regulamento local complementar.

## 10. Localizacao

Ente federal -> IN SEGES MGI aplicavel + jurisprudencia TCU. Ente estadual/municipal -> regulamento local complementar Lei 14.133 + TCE/TCM. `[VERIFICAR - regulamento UF/Municipio]` quando nao confirmado.

## 11. Integracao

**Chamada por:** `licitacoes-master`, `analise-oportunidade`, `/triagem`.

**Entrega para:** operador (parecer) + `CASO.md`. Se vicios -> aciona `deteccao-vicios-edital` (consolidacao top 15) -> `impugnacao-edital` (se for go-impugnar). Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** analise do edital comeca sem base nos documentos preparatorios - perde-se janela de vicios precoces e oportunidade de diligencia via LAI.
