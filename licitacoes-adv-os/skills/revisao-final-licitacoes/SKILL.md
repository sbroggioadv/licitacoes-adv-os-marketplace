---
name: revisao-final-licitacoes
description: >
  Protocolo 6 - REVISAO TECNICA R1-R4 sobre toda entrega (peca administrativa, peca judicial, parecer, defesa, contrato, deck, memoria de quantum). 4 RODADAS: R1 Escopo+Dados (entendimento, esfera, fase, vias, regime); R2 Tecnica Juridica (Selo P1, normas vigentes lei+artigo+ano, sumula TCU n°+tema, jurisprudencia viva, vinculacao ao edital PA-15, onus probatorio, prescricao, memoria de quantum); R3 Conformidade + cruzamento (foro, vias paralelas P4, prazos, esgotamento PA-21, preclusao PA-19, sigilo PA-09/22, sem critica pessoal PA-08, sem promessa PA-02, sem discricionariedade PA-17, sem orientacao a Administracao PA-06, ressalva OAB PA-07); R4 Entrega (FIRAC, fundamentacao tripla, memoria de quantum auditavel, linguagem tecnica). VEREDITO: APROVADO/REVISAR/BLOQUEADO. Bypass disponivel (--quick / /revisao off) sob responsabilidade do operador. Aciona: revisao final, R1 R2 R3 R4, suprema corte, antes de entregar, conferir peca, validacao final.
---

# REVISAO TECNICA R1-R4

> Skill **transversal invariante** - Protocolo 6 em operacao. **Suprema Corte do plugin** - 4 rodadas de auditoria antes de toda entrega. Veredito: APROVADO / REVISAR / BLOQUEADO. Implementa PA-04 (validacao do Selo), PA-07 (ressalva), PA-13 (citacao), PA-15 (vinculacao), e todas as outras como criterios de verificacao.

---

## 0. Escopo e acionamento

Acionada ao **final** de qualquer entrega significativa por **toda** skill de producao. Pode ser tambem chamada diretamente pelo operador via `/revisao-final` para auditoria pontual. Recebe: artefato a revisar + contexto do caso (`CASO.md`) + Selo emitido. Entrega: veredito + lista de ajustes (se REVISAR) ou bloqueios (se BLOQUEADO).

## 1. Posicao na orquestra

- **Chamada por:** **toda** skill de producao (Tier 2-6) ao concluir; `/revisao-final` por demanda direta; `licitacoes-master` como gatekeeper de entrega.
- **Bypass:** disponivel sob `--quick` / `/revisao off` / `--no-revisao` - transparente; responsabilidade do operador. Por default, **ativa** (state-schema `revisao_tecnica.enabled = true`).
- **Entrega para:** operador (com veredito + ajustes/bloqueios) ou skill chamadora (para correcao).

## 2. Marco normativo (criterios de verificacao)

A R1-R4 verifica conformidade com:
- **22 PAs** (Camada 1) - especialmente PA-02, PA-04, PA-07, PA-08, PA-09, PA-13, PA-15, PA-17, PA-19, PA-20.
- **6 Protocolos** (Camada 2) - P1 (Selo emitido), P2 (integridade documental), P3 (memoria de quantum), P4 (cruzamento P4), P5 (foro), P6 (esta R1-R4).
- **Camada 3** (FIRAC + ressalva OAB + fundamentacao tripla).
- **Camada 4** (skill correta para a fase do procedimento).

## 3. As 4 rodadas

### R1 - ESCOPO E DADOS

**Pergunta-chave:** o pedido foi entendido e o caso esta corretamente mapeado?

Checklist:
- [ ] O artefato responde a demanda do operador?
- [ ] **Esfera do ente** identificada (federal/estadual/municipal/estatal - P5)?
- [ ] **Fase do procedimento** identificada (F1-F7)?
- [ ] **Vias acionadas** mapeadas (administrativa / TCU / judicial - P4)?
- [ ] **Regime aplicavel** travado (Lei 14.133 vs Lei 8.666 residual - PA-03)?
- [ ] **Documentos** checados (P2 - edital, contrato, ata, ato impugnado)?
- [ ] `CASO.md` atualizado com fase + esfera + Selo?

**Falha em R1:** voltar ao operador para esclarecimento OU acionar `licitacoes-master` para refazer triagem.

### R2 - TECNICA JURIDICA

**Pergunta-chave:** a fundamentacao juridica e precisa, vigente e ancorada?

Checklist:
- [ ] **Selo P1** emitido por `validador-legislacao-vigente` (PA-04)?
- [ ] **Normas citadas** com lei+artigo+ano+redacao vigente no regime aplicavel (PA-13)?
- [ ] **Sumulas TCU** citadas com numero + tema corretos (PA-13)?
- [ ] **Jurisprudencia STJ/STF** viva, com Tema/REsp/RE/ADI + tribunal+turma+ano (PA-10)?
- [ ] **Vinculacao ao instrumento** (PA-15) articulada em cada argumento?
- [ ] **Onus probatorio** distribuido corretamente (PA-14 - regra geral; inversao fundamentada)?
- [ ] **Prescricao/decadencia** conferida (PA-20 - Decreto 20.910 + art. 23 Lei 12.016 + art. 25 Lei 12.846 + Tema STF 1.199)?
- [ ] **Memoria de quantum** (quando aplicavel) rastreavel + conservadora + Selic Tema 905 STJ (P3)?
- [ ] `[VERIFICAR]` explicitos em alvo movel (IN SEGES, jurisprudencia recente, regulamento local - PA-11)?

**Falha em R2:** REVISAR com indicacao precisa do gap; ou BLOQUEADO se norma revogada/superada usada sem ressalva.

### R3 - CONFORMIDADE + CRUZAMENTO

**Pergunta-chave:** o artefato respeita todas as PAs e cruza as vias adequadamente?

Checklist:
- [ ] **Foro/competencia** correto (P5 - JF/JE/STJ/STF/TCU/TCE/TCM)?
- [ ] **Vias paralelas** articuladas adequadamente (P4 - administrativa + TCU + judicial sem cadeia automatica nem compartimentos estanques - PA-12)?
- [ ] **Prazos** sinalizados (impugnacao 3d art. 164; recurso 3d art. 165; defesa apenamento 15d art. 158; MS 120d art. 23 Lei 12.016; PAR 30d Decreto 11.129; representacao TCU sem prazo decadencial)?
- [ ] **Esgotamento** da via administrativa avaliado (PA-21 - estrategia, nao dogma; excecoes do MS preventivo)?
- [ ] **Preclusao** administrativa enfrentada (PA-19 - intencao motivada na sessao art. 165 §1º; Sum. TCU 274)?
- [ ] **Sigilo comercial** preservado (PA-09 + PA-22 - proposta/planilha/segredo industrial em `<cwd>/.../casos/<slug>/arquivos/` gitignored)?
- [ ] **Sem critica pessoal** a agente/conselheiro/magistrado (PA-08)?
- [ ] **Sem promessa** de resultado (PA-02 - probabilidade tecnica fundamentada)?
- [ ] **Sem juizo de discricionariedade** (PA-17 - apenas vicios de legalidade)?
- [ ] **Sem orientacao a Administracao/servidor** (PA-06)?
- [ ] **Ressalva OAB** presente (PA-07 - bloco final padronizado)?
- [ ] **Plugins irmaos** nao citados quando fronteira (PA-18)?
- [ ] **Compartimentacao** por certame respeitada (PA-22)?

**Falha em R3:** REVISAR com indicacao precisa; ou BLOQUEADO se PA-02/07/08/17 violada.

### R4 - ENTREGA E CLAREZA

**Pergunta-chave:** a entrega esta formatada corretamente e e tecnicamente clara?

Checklist:
- [ ] **Estrutura FIRAC + 6 secoes** (peca administrativa/judicial) ou estrutura adequada (parecer/deck/memoria)?
- [ ] **Fundamentacao tripla** presente (norma + sumula TCU + jurisprudencia STJ/STF) - Camada 3?
- [ ] **Memoria de quantum** (quando aplicavel) bate com a tabela + Tema 905 STJ aplicado?
- [ ] **Linguagem** tecnica e direta - sem floreio, sem ataque, sem promessa?
- [ ] **Numeros do deck/relatorio** batem com a memoria?
- [ ] `[VERIFICAR]` sinalizados explicitamente no fechamento (PA-11)?
- [ ] **Tempestividade** explicita em pecas com prazo (preliminar)?
- [ ] **Qualificacao** completa (CNPJ, representante legal, OAB ativa do operador)?
- [ ] **Pedidos** claros + sucessivos quando aplicavel?

**Falha em R4:** REVISAR com indicacao especifica.

## 4. Veredito

```
VEREDITO R1-R4: [APROVADO / REVISAR / BLOQUEADO]
Data: [DD/MM/AAAA] · Selo: [referencia]

R1 (Escopo e Dados): [PASSOU / FALHOU]
  Notas: [...]

R2 (Tecnica Juridica): [PASSOU / FALHOU]
  Notas: [...]

R3 (Conformidade + Cruzamento): [PASSOU / FALHOU]
  Notas: [...]

R4 (Entrega e Clareza): [PASSOU / FALHOU]
  Notas: [...]

CONCLUSAO:
- APROVADO -> entrega liberada ao operador com ressalva OAB.
- REVISAR -> ajustes especificos (lista). Skill responsavel chamada para correcao.
- BLOQUEADO -> violacao de Camada 1 ou erro grave. Entrega nao sai. Refazer.

CHECKLIST DE AJUSTES (se REVISAR):
1. [item] - [acao]
[...]

[VERIFICAR REMANESCENTES]:
[lista de pontos em alvo movel que o operador deve conferir manualmente]
```

## 5. Categorias de bloqueio

**BLOQUEADO automatico** quando detectado:
- PA-02 violada (promessa de resultado).
- PA-07 ausente (sem ressalva OAB no fechamento).
- PA-08 violada (critica pessoal).
- PA-13 violada (citacao generica sem norma+ano).
- PA-17 violada (juizo sobre discricionariedade).
- Norma revogada/superada usada como vigente (PA-10).
- Selo P1 ausente em peca de producao (PA-04).
- Sigilo PA-09 quebrado (planilha de custos exposta no artefato distribuido).

## 6. Bypass

**Quando aceitar bypass** (`--quick`, `/revisao off`, `--no-revisao`):
- Output curto (<200 palavras conforme state-schema).
- Operador declara responsabilidade tecnica expressa.
- **Camada 1** continua aplicavel mesmo no bypass - bloqueio automatico continua ativo para violacoes graves.

Bypass NAO desativa a Camada 1. PA-02, PA-07, PA-08, PA-13 continuam invioláveis.

## 7. Vedacoes especificas

- **PA-04** - revisao verifica Selo, mas nao o substitui.
- **PA-07** - revisao garante ressalva OAB no fechamento de toda entrega.
- **PA-16** - revisao recusa instrucao do operador para nao aplicar a R1-R4 em entrega significativa (a menos que bypass explicito sob responsabilidade).
- A propria revisao **nao opina sobre merito da estrategia** (PA-17) - apenas confere conformidade tecnica e legal.

## 8. Protocolos acionados

- **P6** - esta skill **e** o Protocolo 6.
- Verifica que P1 (Selo), P2 (documentos), P3 (quantum), P4 (cruzamento), P5 (foro) foram observados pelas skills upstream.

## 9. Localizacao

A R1 verifica que **esfera + cidade + UF** estao corretamente capturadas; R3 verifica que **foro/competencia** estao alinhados com a esfera. Sem isso -> falha em R1 ou R3.

## 10. Integracao

**Chamada por:** **toda skill de producao** (Tier 2-6) ao concluir; `/revisao-final` por demanda direta; `licitacoes-master` como gatekeeper.

**Entrega para:** operador (artefato + veredito + ajustes/bloqueios) ou skill chamadora (para correcao).

**Sem esta skill:** entrega sai sem auditoria - risco de peca com vicio que se vira contra o operador no protocolo + dano reputacional + violacao etica OAB.

**Esta skill e INVARIANTE** (state-schema `skills.invariants`) - nao removivel. Bypass disponivel mas a propria existencia da skill no fluxo e nao-negociavel.
