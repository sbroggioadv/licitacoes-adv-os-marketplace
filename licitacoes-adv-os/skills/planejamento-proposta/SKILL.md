---
name: planejamento-proposta
description: >
  Analise estrategica previa da proposta - skill consultiva, antes da abertura da sessao (PA-09 sigilo absoluto da proposta antes da publicidade do certame - Lei 14.133/2021 art. 13 §3º e art. 17). Define margem, identifica teto e piso (exequibilidade art. 59 §4º - 70% do referencial), simula cenarios de disputa (lances, tecnica e preco, maior desconto), decide participacao isolada x consorcio (art. 15 Lei 14.133 - consorcio so quando expressamente admitido), aplica tratamento ME/EPP quando aplicavel (LC 123/2006), incorpora reservas contingenciais conforme matriz de risco (art. 22). Compartimentacao rigorosa por certame (PA-22). Aciona: planejamento da proposta, montar proposta, simular lance, margem, BDI, exequibilidade, consorcio licitatorio, cota ME/EPP.
---

# PLANEJAMENTO DA PROPOSTA

> Skill **Tier 2 consultiva** - antes da sessao publica. Sigilo absoluto da proposta (PA-09 + Lei 14.133/2021 art. 13 §3º + art. 17). Compartimentacao por certame (PA-22 - vedada mistura de propostas de certames diferentes do mesmo licitante). Implementa P1, P3, P5; respeita PA-15 (vinculacao), PA-09 (sigilo), PA-22 (compartimentacao).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `/edital`, `analise-oportunidade` (quando go = participar), `analise-edital` (apos checklist limpo). Recebe: edital + anexos + matriz de risco analisada + dados internos da PJ (custos, capacidade, restricoes de fluxo, BDI base). **Atencao maxima a PA-09:** todos os dados sigilosos ficam em `<cwd>/licitacoes/casos/<slug>/arquivos/` (gitignored); jamais persistidos no plugin distribuido.

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/edital`, `analise-oportunidade` (go), `analise-edital`, `analise-matriz-risco`.
- **Pre-requisito:** Selo (PA-04); analise de edital completa; matriz de risco mapeada (`analise-matriz-risco`).
- **Aciona em sequencia:** `tratamento-me-epp` (Tier 3) se ME/EPP; `proposta-exequibilidade` (Tier 3) na pre-sessao; `habilitacao-documentos` (Tier 3) em paralelo.
- **Entrega para:** plano estrategico interno (rascunho consultivo - PA-07).

## 2. Marco normativo

- **Lei 14.133/2021:**
  - **art. 13 §3º + art. 17** - sigilo da proposta antes da publicidade.
  - **art. 15** - participacao em consorcio - regra: vedada salvo previsao expressa no edital.
  - **art. 33** - criterios de julgamento.
  - **art. 50** - desclassificacao + inexequibilidade.
  - **art. 59 §4º** - **limite de exequibilidade: 70%** do valor de referencia ou da media das propostas validas.
  - **art. 64** - diligencia/saneamento.
  - **arts. 66-70** - habilitacao.
  - **art. 92** - clausulas necessarias do contrato.
- **LC 123/2006 + LC 147/2014:** arts. 43-48 (ME/EPP - empate ficto, cota, regularizacao).
- **CC arts. 421-422** - boa-fé objetiva.
- **Lei 9.279/96 art. 195 XI** - sigilo do segredo industrial.
- **Sumulas TCU:** 269 (formalismo moderado); 287 (consorcios).

## 3. Os 8 eixos do planejamento

### Eixo 1 - Margem-alvo e BDI

- BDI base: encargos sociais + tributos + custos indiretos + lucro + reservas.
- Reservas contingenciais por categoria de risco (`analise-matriz-risco`): alea ordinaria absorvida; alea extraordinaria com gatilho de revisao.
- Margem-alvo: confortavel (≥ 15% lucro pos-tributos) / media (5-15%) / agressiva (<5%) - decisao estrategica.

### Eixo 2 - Piso de exequibilidade

- **Custo total minimo** (sem lucro, sem reservas): valor abaixo do qual a proposta e tecnicamente inexequivel.
- **Limite legal de exequibilidade (art. 59 §4º Lei 14.133):** 70% do valor de referencia OU 70% da media das propostas validas, conforme o caso. Abaixo disso, presume-se inexequivel - onus de comprovar com planilha de custos detalhada (art. 64 - diligencia).
- **Estrategia:** se piso da PJ > 70% do referencial -> proposta tranquila; se piso da PJ < 70% do referencial -> avaliar (a) atacar o referencial via impugnacao do orcamento estimativo OU (b) participar com defesa preparada da exequibilidade.

### Eixo 3 - Teto - referencial e ponto de equilibrio

- Valor estimado publicado (regra art. 23) ou sigiloso (art. 24 excepcional).
- Concorrencia esperada (analise de mercado): se ha 5+ competidores, tendencia a precos proximos ao piso; se 1-2, tendencia a precos proximos ao teto.
- Ponto de equilibrio: preco que (i) preserva margem-alvo, (ii) e competitivo dentro do esperado, (iii) e seguramente exequivel.

### Eixo 4 - Simulacao por criterio de julgamento

- **Menor preco** (art. 33 I): foco em piso e simulacao de lances.
- **Tecnica e preco** (art. 33 II): matriz de pontuacao - tecnica vale 0-60%; preco 40-100%. Simulacao do quanto vale 1 ponto tecnico em preco.
- **Maior desconto** (art. 33 III): igual a menor preco com perspectiva inversa.
- **Maior retorno economico** (art. 33 IV): menos comum - calculo de valor presente liquido / TIR.

### Eixo 5 - Lances (pregao + concorrencia eletronica)

- Numero de rodadas tipico; passos minimos.
- Estrategia: lance inicial conservador (acima do esperado) + lances de aproximacao + lance final (proximo do piso decidido).
- Risco de virada por concorrente abaixo do piso (gatilho de defesa de exequibilidade - acionar `proposta-exequibilidade` posterior).

### Eixo 6 - Consorcio (art. 15 Lei 14.133 + Sum. TCU 287)

- **Regra:** consorcio so admitido quando edital **expressamente** prever.
- Quando admitido: capital social somado; capacidade tecnica somada; CNDs/CNDT/SICAF de cada consorciada; responsabilidade solidaria.
- Estrategia: avaliar (a) participacao isolada com subcontratacao (se admitida - Sum. TCU 248) vs (b) consorcio (compartilhar capacidade + lucro) vs (c) nao participacao.
- Acordo de consorcio - documento interno + acordos de partilha de riscos (matriz de risco entre consorciadas).

### Eixo 7 - Tratamento ME/EPP (LC 123)

- Verificar enquadramento: receita bruta anual; atividade nao-vedada.
- **Empate ficto (art. 44 LC 123):** ME/EPP com proposta ate 5% superior a melhor classificada tem direito de cobrir - aplicacao em criterio menor preco.
- **Cota reservada (art. 48 III LC 123):** ate 25% do objeto reservado a ME/EPP - aplicacao em compras com lotes/itens.
- **Regularizacao fiscal (art. 43 §1º LC 123):** 5 dias uteis prorrogaveis para regularizar irregularidade fiscal apos declaracao de vencedora.
- Estrategia: ME/EPP avalia em qual mecanismo (empate ficto x cota) e mais favoravel para o certame especifico.

### Eixo 8 - Documentacao acessoria

- Declaracao de enquadramento (LC 123 se ME/EPP).
- Declaracao de elaboracao independente.
- Declaracao de inexistencia de fato impeditivo.
- Atestados (mesmo recorte da habilitacao - `habilitacao-documentos`).
- Planilha de custos detalhada (para defesa de exequibilidade).

## 4. Output - Plano interno (formato)

```
PLANO ESTRATEGICO DA PROPOSTA - CASO [slug]
SIGILOSO - PA-09 + Lei 14.133 arts. 13 §3º e 17
Data: [DD/MM/AAAA] · Selo: [referencia]

CONFIGURACAO DO CERTAME:
- Modalidade: [pregao eletronico / concorrencia / dialogo]
- Criterio: [menor preco / tecnica e preco / maior desconto]
- Valor estimado: [R$ X] (publicado / sigiloso)
- Esfera: [federal / estadual / municipal]

EIXO 1 - Margem-alvo e BDI:
- BDI base: [%]
- Reservas por risco: [valores absolutos por categoria]
- Margem-alvo: [confortavel / media / agressiva] - [% lucro pos-tributos]

EIXO 2 - Piso de exequibilidade:
- Custo total minimo PJ: [R$ X]
- Limite legal (70% do referencial - art. 59 §4º): [R$ Y]
- Posicao: [acima / proximo / abaixo do limite]

EIXO 3 - Teto e ponto de equilibrio:
- Valor de referencia: [R$ Z]
- Ponto de equilibrio: [R$ W]
- Concorrencia esperada: [N competidores]

EIXO 4 - Criterio de julgamento - simulacao:
[Cenarios A/B/C com probabilidade e impacto]

EIXO 5 - Lances:
- Lance inicial: [R$ A] | Lance final: [R$ B] | Passo: [R$ C]

EIXO 6 - Participacao isolada x consorcio:
- Decisao: [isolada / consorcio com Z / nao participar]
- Justificativa: [PA-15 - art. 15 Lei 14.133 + Sum. TCU 287]

EIXO 7 - ME/EPP (se aplicavel):
- Mecanismo: [empate ficto / cota reservada]
- Calendario: regularizacao fiscal LC 123 art. 43 §1º (5 dias prorrogaveis)

EIXO 8 - Documentos acessorios:
- [lista de declaracoes e atestados]

PROXIMOS PASSOS:
- Acionar `habilitacao-documentos` para conferencia documental
- Preparar `proposta-exequibilidade` para defesa preventiva
- Atualizar `calendario-licitatorio` com prazo de validade da proposta (60 dias)

ATENCAO LEGAL:
- Sigilo absoluto da proposta (PA-09) - dados em `<cwd>/licitacoes/casos/<slug>/arquivos/`
- Compartimentacao por certame (PA-22) - vedada mistura

[VERIFICAR]: [regulamento UF/Municipio; jurisprudencia TCU 2024-2026 sobre exequibilidade]

---
[Ressalva OAB - PA-07]
```

## 5. Vedacoes especificas

- **PA-09** - sigilo absoluto da proposta antes da publicidade do certame (Lei 14.133 art. 13 §3º + art. 17). Vedada divulgacao a terceiros, inclusive intra-grupo da PJ-cliente nao envolvido no certame.
- **PA-22** - compartimentacao rigorosa: o mesmo licitante pode disputar certames simultaneos, mas cada um e caso compartimentado. Vedada mistura.
- **PA-04** - Selo antes do plano.
- **PA-15** - decisoes ancoradas na vinculacao ao edital (consorcio so se previsto; ME/EPP no que o edital admite).
- **PA-02** - vedada promessa de adjudicacao; probabilidade tecnica fundamentada.
- **PA-18** - decisao tributaria-societaria do enquadramento ME/EPP fica como "consulta a especialista" se houver duvida - sem citar produto irmao.

## 6. Protocolos acionados

- **P1** - Selo. **P3** - memoria de quantum (BDI, piso, teto, margem) auditavel. **P5** - regulamento local pode afetar ME/EPP/consorcio.

## 7. Localizacao

Federal -> aplicacao plena da Lei 14.133 + LC 123. Estadual/municipal -> regulamento local complementar pode prever cotas ME/EPP especificas; `[VERIFICAR - regulamento UF/Municipio]`. Estatais (Lei 13.303) -> regulamento interno proprio.

## 8. Integracao

**Chamada por:** `licitacoes-master`, `/edital`, `analise-oportunidade`, `analise-edital`, `analise-matriz-risco`.

**Entrega para:** operador (plano interno + ressalva OAB) + `CASO.md`. Aciona `habilitacao-documentos` + `proposta-exequibilidade` em sequencia. Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** proposta enviada sem analise estrategica - risco de inexequibilidade nao defendida (desclassificacao); de margem insuficiente (lucro real abaixo do calculado); de incompatibilidade com matriz de risco (impacto no reequilibrio futuro).
