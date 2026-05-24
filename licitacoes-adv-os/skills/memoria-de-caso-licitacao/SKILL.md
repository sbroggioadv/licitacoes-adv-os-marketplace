---
name: memoria-de-caso-licitacao
description: >
  Gestao de CASO.md compartimentado por cliente/certame (LGPD + segredo comercial reforcados - PA-09, PA-22). Estrutura do CASO.md: identificacao do certame + fase atual + vias paralelas P4 + Selo de Validacao Legal Previa + documentos + timeline + estrategia + skills acionadas + status. Gitignore garantido (pasta licitacoes/ jamais versionada). WARNING agressivo se pasta sincronizada (iCloud/OneDrive/Dropbox/Drive) - vazamento de proposta + planilha de custos + segredo industrial (Lei 9.279/96 art. 195 XI + Lei 14.133 arts. 13 §3º e 17). Slug determinístico sem expor identidade (UF-orgao-ano-modalidade-seq ou hash SHA-1 truncado). O mesmo licitante pode disputar varios certames - cada um e caso compartimentado. Aciona: caso, CASO.md, abrir caso, novo caso, retomar caso, listar casos, status do caso, slug do caso.
---

# MEMORIA DE CASO LICITATORIO

> Skill **transversal invariante** - gestao de `CASO.md` por certame com compartimentacao rigorosa (PA-22) + sigilo absoluto (PA-09). Implementa PA-09, PA-22, PA-16; integra com todas as skills.

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `/caso-licitacao`, `/status-licitacoes`, ou implicitamente por toda skill que precise ler/atualizar o estado do caso. Recebe: comandos do operador (abrir, retomar, listar, atualizar, fechar). Entrega: `CASO.md` atualizado + alertas + compartimentacao garantida.

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/caso-licitacao`, `/status-licitacoes`, todas as skills (via leitura/atualizacao do `CASO.md`).
- **Pre-requisito:** `<cwd>/licitacoes/` configurado (apos `onboarding-licitacoes`).
- **Aciona em sequencia:** `validador-legislacao-vigente` (para emitir Selo quando ha caso novo); skills da fase atual.
- **Entrega para:** todas as skills (leitura) + `CASO.md` (escrita).

## 2. Marco normativo (sigilo + LGPD)

- **PA-09** - sigilo comercial absoluto:
  - **Lei 14.133/2021 arts. 13 §3º e 17** - sigilo da proposta antes da publicidade do certame.
  - **Lei 9.279/96 art. 195 XI** - segredo industrial (crime de concorrencia desleal).
- **PA-22** - compartimentacao absoluta:
  - **LGPD (Lei 13.709/2018) art. 11** - dado pessoal sensivel.
  - **EAOAB art. 34 IV** - vedacao ao conflito de interesses.
  - **CC art. 422** - boa-fé objetiva (sigilo de cliente).
- **CF art. 5º X** - inviolabilidade da intimidade.
- **CF art. 5º XII** - sigilo de dados.

## 3. Estrutura canonica do CASO.md

```markdown
# CASO - [slug deterministico]

## Identificacao do certame
- Orgao licitante: [ente]
- Modalidade: [pregao eletronico | concorrencia | dialogo competitivo | leilao | concurso]
- Criterio de julgamento: [menor preco | tecnica e preco | maior desconto | maior retorno economico]
- Regime juridico: [Lei 14.133/2021 | Lei 8.666/1993 residual | Lei 13.303/2016 estatal | Lei 11.079/2004 PPP | Lei 8.987/1995 concessao]
- Esfera: [federal | estadual | municipal | estatal]
- Localizacao: [UF / Municipio - TCU/TCE/TCM aplicavel]
- Numero do edital / processo administrativo: [ID]
- Objeto: [sintese - sem expor segredo industrial]
- Valor estimado: [R$ X]

## Fase atual (triagem)
- Fase atual: [F1 pre-edital | F2 edital | F3 sessao/habilitacao | F4 contrato | F5 sancao | F6 TCU/TCE | F7 judicial]
- Fases simultaneas (P4): [lista - exemplo F5 + F7]
- Data da ultima movimentacao: [DD/MM/AAAA]
- Proximo prazo critico: [DD/MM/AAAA - descricao - skill responsavel]

## Selo de Validacao Legal Previa (P1)
- Data-base: [DD/MM/AAAA]
- Data do fato gerador: [DD/MM/AAAA]
- Regime aplicavel: [Lei X / Y]
- Normas validadas: [lista - lei + ano + artigo]
- Sumulas TCU vivas aplicaveis: [222 / 247 / 248 / 251 / 269 / 274 / 277 / 287]
- Jurisprudencia STJ/STF aplicavel: [Tema 905 / 897 / 1.199 pendente / REsp / RE / ADI]
- Foro/competencia: [administrativo + TCU/TCE + JF/JE]
- [VERIFICAR]: [pontos em alvo movel]
- Validade: [data-base + 60 dias]

## Documentos do caso (em arquivos/ - gitignored - PA-09)
- edital.pdf (+ anexos: ETP, TR, planilha estimativa, minuta contratual, matriz de risco)
- proposta.pdf (com planilha de custos - SIGILOSO)
- atos da sessao publica (ata, decisoes)
- recursos / contrarrazoes / decisoes
- contrato.pdf (se F4+)
- notificacoes formais (preservacao de prova)
- decisao TCU / acordao
- ato sancionatorio
- decisao judicial / acordao

## Timeline da fase
| Marco | Data | Prazo seguinte | Skill responsavel |

## Vias paralelas (P4 - Cruzamento Adm + TCU + Judicial)
| Via | Marco | Data | Prejudicialidade | Aproveitamento cruzado |

## Estrategia priorizada
- Prioridade 1: [fase / via]
- Justificativa: [vinculacao ao edital + sumula TCU + jurisprudencia + fato concreto]

## Skills acionadas
- [lista cronologica das skills usadas no caso]

## Status
- Ultima atualizacao: [DD/MM/AAAA]
- Sprint atual: [N/A - este e do operador]
- Operador: [iniciais + OAB]

## Riscos identificados
- [risco] - [mitigacao] - [status]

## Notas operacionais (livre)
- [notas do operador]
```

## 4. Slug deterministico (sem expor identidade)

**NUNCA** usar nome do licitante no slug. Esquemas validos:

- **Esquema A:** `<UF>-<orgao>-<ano>-<modalidade>-<seq>` - ex.: `SP-prefeiturax-2024-pregao-001`
- **Esquema B:** `<sigla-orgao>-<n°-edital>` - ex.: `mptus-edital-345-2024`
- **Esquema C:** hash SHA-1 truncado de identificador interno - ex.: `lic-a3f7c9b2`

Slug nao revela:
- Nome da PJ-cliente.
- Valor da proposta especifica.
- Dados de representante legal.
- Segredo industrial.

## 5. Compartimentacao (PA-22)

Cada caso = pasta propria em `<cwd>/licitacoes/casos/<slug>/`:

```
<cwd>/licitacoes/
├── persona.md (operador - resolvido em runtime)
├── cowork-state.json (state global do escritorio)
├── CLAUDE.md (atalhos do operador)
├── MEMORY.md (memoria do operador)
└── casos/
    ├── <slug-1>/
    │   ├── CASO.md (estrutura canonica)
    │   ├── arquivos/  (gitignored - edital, proposta, contratos)
    │   └── memoria-caso.md (notas estrategicas)
    ├── <slug-2>/
    │   └── ...
    └── ...
```

**Vedada mistura** de dados de clientes/casos diferentes no mesmo arquivo, no mesmo prompt ou na mesma sessao continuada.

**Particularidade licitatoria:** o mesmo cliente pode disputar **varios certames simultaneos** - cada certame e um caso proprio (mesmo cliente, slugs diferentes). Vedada mistura de propostas de certames distintos do mesmo cliente.

## 6. Gitignore garantido + warning de sincronizacao

```
# .gitignore (do plugin)
licitacoes/
**/licitacoes/casos/
```

**Warning agressivo de pasta sincronizada:**

```
WARNING - PASTA SINCRONIZADA DETECTADA (PA-09 + PA-22)
Caminho: <path>
Risco: documentos sigilosos da empresa fornecedora (proposta, planilha de custos,
segredo industrial) podem ser sincronizados para nuvem do servico
(iCloud/OneDrive/Dropbox/Drive).

Implicacao:
- Violacao do sigilo de proposta antes da abertura (Lei 14.133 arts. 13 §3º e 17)
- Crime de concorrencia desleal (Lei 9.279/96 art. 195 XI)
- LGPD - dado pessoal sensivel (art. 11)
- Responsabilidade etica do advogado (EAOAB art. 34)
- Potencial nulidade do certame (vazamento de proposta)

Recomendacao: mover workspace para pasta local (~/Dev/licitacoes/) ou
cifrar a pasta de casos.

Continuar mesmo assim? [s/N]
```

Pasta sincronizada -> warning 2x; so prosseguir com "confirmo o risco" expresso.

## 7. Operacoes do CASO.md

### 7.1 - Abrir caso novo (`/caso-licitacao --new`)
1. Coletar dados de identificacao (sem expor cliente).
2. Gerar slug deterministico.
3. Criar pasta `<cwd>/licitacoes/casos/<slug>/`.
4. Criar `CASO.md` com estrutura canonica.
5. Criar `arquivos/` (gitignored).
6. Acionar `validador-legislacao-vigente` para emitir Selo.

### 7.2 - Retomar caso (`/caso-licitacao --retomar <slug>`)
1. Verificar existencia da pasta.
2. Ler `CASO.md` integralmente.
3. Verificar **Selo** (data-base) - se >60 dias -> acionar `validador-legislacao-vigente`.
4. Disponibilizar contexto para skill solicitante.

### 7.3 - Listar casos (`/caso-licitacao --listar`)
1. Listar pastas em `<cwd>/licitacoes/casos/`.
2. Para cada uma: slug + fase atual + proximo prazo (PA-22 - sem expor identidade).
3. Output sintetico.

### 7.4 - Atualizar caso (implicito em toda skill)
1. Skill que produz output atualiza `CASO.md` (timeline + skills acionadas + status).
2. Selo atualizado quando ha producao apos validacao.

### 7.5 - Status do caso (`/status-licitacoes`)
1. Ler `CASO.md` do caso ativo (default: ultimo modificado).
2. Output: fase, vias paralelas, proximo prazo, alertas, Selo vigente.

## 8. Vedacoes especificas

- **PA-09** sigilo absoluto. **PA-22** compartimentacao absoluta.
- **PA-16** vedada instrucao de "compartilhar dados entre casos" ou "misturar clientes".
- **PA-15** todo registro vinculado ao edital especifico.
- **PA-07** ressalva OAB no fechamento de cada peca/parecer associada ao caso.
- Vedado **persistir** proposta + planilha + segredo industrial no plugin distribuido.
- Pasta sincronizada -> warning + bloqueio se nao confirmado.

## 9. Protocolos acionados

- **P1** - aciona `validador-legislacao-vigente` quando Selo vencido (>60 dias).
- **P5** - registra esfera + foro no `CASO.md`.
- Suporta **P4** - vias paralelas registradas na tabela de cruzamento.

## 10. Localizacao

`CASO.md` registra: esfera do ente + cidade/UF + TCU/TCE/TCM aplicavel. Skill leitora (`licitacoes-master`) usa para roteamento P5.

## 11. Integracao

**Chamada por:** todas as skills (leitura); `/caso-licitacao` (CRUD); `/status-licitacoes` (status).

**Entrega para:** todas as skills (contexto do caso) + operador (status).

**Sem esta skill:** plugin opera sem persistencia + sem compartimentacao - violacao LGPD + PA-22 + risco de conflito de interesses + perda de continuidade entre sessoes.

**Esta skill e INVARIANTE** (state-schema `skills.invariants`) - nao removivel.
