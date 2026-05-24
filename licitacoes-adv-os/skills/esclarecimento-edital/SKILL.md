---
name: esclarecimento-edital
description: >
  Pedido de esclarecimento ao edital (art. 164 §1º Lei 14.133/2021 - mesmo prazo da impugnacao, 3 dias uteis antes da abertura). Distincao tecnica em relacao a impugnacao: esclarecimento dirime duvida sem questionar legalidade; impugnacao aponta vicio. Estrategia: quando usar esclarecimento como diligencia preparatoria de impugnacao - provoca pronunciamento da Administracao que sera usado como elemento de prova/argumentacao em impugnacao subsequente ou em recurso administrativo. Vinculacao ao instrumento (PA-15) - duvida sobre interpretacao das clausulas. Aciona: pedido de esclarecimento, esclarecer edital, duvida sobre edital, art. 164 §1º, interpretacao de clausula.
---

# ESCLARECIMENTO AO EDITAL

> Skill **Tier 2** - peca administrativa para dirimir duvida interpretativa sobre o edital. Pode ser **diligencia preparatoria de impugnacao** (estrategia). Mesmo prazo do art. 164 Lei 14.133/2021 (3 dias uteis antes da abertura). Implementa P1, P5; respeita PA-15 (vinculacao), PA-08 (sem critica pessoal), PA-07 (ressalva OAB).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `analise-edital`, `deteccao-vicios-edital` quando o trecho do edital comporta **duvida interpretativa** (nao vicio claro). Recebe: trecho que gera duvida + interesse do licitante em entendimento especifico. Entrega: peca de esclarecimento estrategica (rascunho - PA-05, PA-07).

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `analise-edital`, `deteccao-vicios-edital` (quando vicio nao e claro mas pode ser fundamentado depois da resposta), `analise-oportunidade`.
- **Pre-requisito:** Selo emitido (PA-04); prazo confirmado (`calendario-licitatorio`).
- **Aciona em sequencia:** `revisao-final-licitacoes` antes da entrega; resposta da Administracao pode embasar futura `impugnacao-edital` ou peca de `recurso-administrativo`.
- **Entrega para:** operador apos R1-R4. Operador protocola sob OAB ativa.

## 2. Marco normativo

- **Lei 14.133/2021:**
  - **art. 164 §1º** - esclarecimento ate **3 dias uteis antes da abertura**, mesmo prazo da impugnacao;
  - **art. 164 §3º** - resposta da Administracao ate o dia anterior a abertura;
  - **art. 12** - vinculacao ao instrumento (PA-15);
  - **art. 13** - publicidade do procedimento.
- **Lei 9.784/1999** - processo administrativo federal - direito de peticao + dever de resposta.
- **CF art. 5º XXXIV a** - direito de peticao aos Poderes Publicos.
- **CF art. 37 caput** - publicidade.
- **Sumulas TCU:** 269 (formalismo moderado - cabe esclarecimento de duvida documental).

## 3. Distincao tecnica - esclarecimento x impugnacao

| Criterio | Esclarecimento | Impugnacao |
|----------|----------------|------------|
| **Natureza** | Dirimir duvida interpretativa | Apontar vicio de legalidade |
| **Tese central** | "Como entender X?" | "X viola a lei/principio" |
| **Pedido** | Resposta interpretativa | Correcao/retificacao/anulacao |
| **Tom** | Consultivo, neutro | Combativo, fundamentado |
| **Base legal nuclear** | art. 164 §1º Lei 14.133 | art. 164 Lei 14.133 |
| **Resposta da Administracao** | Cria interpretacao vinculante | Acolhe (corrige) ou rejeita |
| **Estrategia subsequente** | Pode embasar impugnacao futura | Recurso interno + TCU + MS |

**Quando preferir esclarecimento sobre impugnacao:**
1. Trecho ambiguo, sem vicio claro - duvida real.
2. Estrategia: provocar pronunciamento que sera usado em impugnacao subsequente caso a resposta seja desfavoravel ou contradiga o edital.
3. Tatica de baixo custo politico - nao confronta a Administracao diretamente.
4. Permite ao licitante alinhar a proposta com interpretacao oficial.
5. Quando ha **multiplas interpretacoes possiveis** - busca-se a oficial.

**Quando preferir impugnacao sobre esclarecimento:**
1. Vicio de legalidade claro - perda de tempo pedir esclarecimento.
2. Restricao a competitividade flagrante.
3. Marca/modelo direcionado.
4. Garantia desproporcional sem justificativa.
5. Prazo de impugnacao curto - foco direto.

## 4. Estrategia - esclarecimento como diligencia preparatoria

Cenario tipico: trecho do edital permite 2 interpretacoes (A e B). Interpretacao A favorece o licitante (ex.: aceita atestado de servico afim); B prejudica (ex.: exige atestado identico).

- **Etapa 1:** pedir esclarecimento perguntando "considera-se atendido o requisito X com atestado de servico Y?".
- **Etapa 2:** se Administracao responde A -> registro favoravel; alinhar proposta.
- **Etapa 3:** se Administracao responde B -> **impugnacao subsequente** ancorada na resposta (contradicao com norma/sumula TCU); resposta da Administracao e elemento de prova.
- **Etapa 4:** se Administracao **nao responde** ate o dia anterior a abertura (art. 164 §3º descumprido) -> registrar; **impugnacao ou MS** subsequente fundamentado em violacao ao direito de peticao + falta de publicidade.

## 5. Estrutura canonica da peca

```
EXMO. [AGENTE DE CONTRATACAO / COMISSAO / AUTORIDADE]
PROCESSO ADMINISTRATIVO N° [n°]
EDITAL N° [n°] - [MODALIDADE] - [OBJETO]

PEDIDO DE ESCLARECIMENTO (art. 164 §1º Lei 14.133/2021)

I - TEMPESTIVIDADE
O presente esclarecimento e tempestivo. Edital publicado em [DD/MM/AAAA]; abertura
prevista para [DD/MM/AAAA]; prazo do art. 164 §1º (3 dias uteis antes) ate [DD/MM];
protocolado em [DD/MM] - dentro do prazo.

II - QUALIFICACAO DO SOLICITANTE
[Razao social - CNPJ - representante legal]. Interesse legitimo em participar
do certame com correta compreensao das exigencias.

III - DOS PONTOS QUE COMPORTAM DUVIDA

III.1 - Ponto 1: [referencia clara ao item do edital]
Trecho: "[citacao literal]"

Duvida: [pergunta clara, neutra, sem juizo de legalidade]. Exemplo: "Considera-se
atendido o requisito de capacidade tecnica do item X com atestado relativo a
servico de natureza Y?"

Fundamentos da duvida:
- Interpretacao 1 (literal): [...]
- Interpretacao 2 (sistemica): [...]
- Vinculacao ao instrumento (art. 12 Lei 14.133): a clareza interpretativa
  e necessaria para igualdade entre licitantes.

III.2 - Ponto 2: [...]

IV - DOS PEDIDOS
Diante do exposto, requer:
a) Conhecimento do presente esclarecimento por tempestivo;
b) Resposta oficial aos Pontos 1, 2 e demais arrolados;
c) Publicacao da resposta com observancia do art. 164 §3º Lei 14.133 (ate o dia
   anterior a abertura) - resguardando o principio da publicidade (CF art. 37 caput).

V - DOCUMENTOS ANEXOS
- Procuracao OAB ativa (PA-05, PA-07)
- Documentos societarios

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}}
OAB/{{OAB_UF}} {{OAB_NUMERO}}
{{FIRM_NAME}}

---
[Ressalva OAB - PA-07]
```

## 6. Esclarecimento documental (vies Sum. TCU 269)

Quando duvida e sobre **forma documental** (qual atestado serve, qual certidao basta, qual formato de planilha), explorar **Sum. TCU 269** - formalismo moderado: falha sanavel + saneamento (art. 64 Lei 14.133). Esclarecimento bem feito previne inabilitacao por formalismo.

## 7. Vedacoes especificas

- **PA-04** - Selo antes da peca.
- **PA-15** - duvida ancorada na vinculacao ao instrumento (interpretacao das clausulas).
- **PA-08** - tom neutro, sem critica pessoal a agente.
- **PA-02** - vedada promessa de que a resposta sera favoravel.
- **PA-07** - ressalva OAB obrigatoria.
- **PA-17** - vedado pedir que o agente revise discricionariedade; pedir esclarecimento, nao opinar sobre acerto da escolha.

## 8. Protocolos acionados

- **P1** - Selo. **P5** - autoridade competente para receber. **P6** - R1-R4 antes da entrega.

## 9. Localizacao

Mesmo regime do `impugnacao-edital` - autoridade definida no edital. Federal (autoridade federal). Estadual/municipal (autoridade local).

## 10. Integracao

**Chamada por:** `licitacoes-master`, `analise-edital`, `deteccao-vicios-edital`, `analise-oportunidade`.

**Entrega para:** operador (peca apos R1-R4 + ressalva OAB) + `CASO.md`. Resposta da Administracao -> pode acionar `impugnacao-edital` (se contradiz norma) ou registrar para `planejamento-proposta` (se favoravel).

**Sem esta skill:** duvidas interpretativas viram inabilitacao surpresa ou proposta nao alinhada com interpretacao oficial; perde-se elemento probatorio para impugnacao subsequente.
