---
name: proposta-exequibilidade
description: >
  Analise do limite de exequibilidade (art. 59 §4º Lei 14.133/2021 - presuncao de inexequibilidade abaixo de 70% do valor de referencia ou da media das propostas validas conforme o caso). Estrategia DEFENSIVA quando a proposta do licitante-cliente esta sob suspeita (planilha de custos detalhada como prova; demonstracao de viabilidade tecnica e economica; diligencia saneadora art. 64; jurisprudencia TCU consolidada sobre exequibilidade). Estrategia de ATAQUE quando concorrente apresentou proposta inexequivel (intencao de recurso motivada art. 165; razoes; pedido de desclassificacao + diligencia). Aciona: exequibilidade da proposta, art. 59 §4º, 70% do referencial, planilha de custos, defesa de proposta, ataque a proposta concorrente, inexequibilidade.
---

# PROPOSTA E EXEQUIBILIDADE

> Skill **Tier 3** - dois lados: **defesa** do licitante-cliente quando sua proposta esta sob suspeita; **ataque** quando concorrente apresenta proposta inexequivel. Limite legal: art. 59 §4º Lei 14.133/2021 - 70%. Implementa P1, P2, P3, P6; respeita PA-15 (vinculacao), PA-14 (onus probatorio), PA-09 (sigilo da planilha).

---

## 0. Escopo e acionamento

Acionada por `licitacoes-master`, `/triagem` na fase F3, ou diretamente quando: (a) o licitante-cliente recebe **diligencia de exequibilidade** (art. 64 Lei 14.133) - modo defesa; (b) **concorrente apresenta proposta abaixo de 70%** do referencial - modo ataque. Recebe: proposta, planilha de custos, valor de referencia, media das propostas validas. Sigilo PA-09.

## 1. Posicao na orquestra

- **Chamada por:** `licitacoes-master`, `/triagem` (fase F3), `planejamento-proposta` (defesa preventiva), `recurso-administrativo` (apos desclassificacao injusta).
- **Pre-requisito:** Selo (PA-04); planilha de custos disponivel (PA-09 sigilo).
- **Aciona em sequencia:** `recurso-administrativo` se desclassificacao por inexequibilidade ja ocorreu; `contrarrazoes-recurso` se concorrente recorre.
- **Entrega para:** **peca defensiva** (resposta a diligencia) OU **peca de ataque** (intencao de recurso + razoes) - rascunho com R1-R4 e ressalva OAB.

## 2. Marco normativo

- **Lei 14.133/2021:**
  - **art. 59 §4º** - presuncao de inexequibilidade abaixo de **70%** do valor de referencia ou da media das propostas validas, conforme o caso.
  - **art. 50 II** - desclassificacao por inexequibilidade.
  - **art. 64** - diligencia saneadora (Administracao pode/deve solicitar comprovacao).
  - **art. 56** - sessao publica.
  - **art. 165** - recurso administrativo (intencao motivada + razoes em 3 dias uteis).
- **Sumulas TCU:**
  - **Sum. 269** - formalismo moderado (saneamento documental).
  - Jurisprudencia TCU consolidada sobre exequibilidade (acordaos referenciaveis) - `[VERIFICAR - decisoes TCU 2024-2026]`.
- **CPC art. 373 §1º** - distribuicao dinamica do onus (subsidiario) - PA-14.
- **Lei 9.279/96 art. 195 XI** - sigilo do segredo industrial.

## 3. Logica do limite de 70%

```
PRESUNCAO DE INEXEQUIBILIDADE - art. 59 §4º Lei 14.133/2021
- Valor de referencia: R$ X (publicado ou sigiloso)
- 70% do referencial: R$ 0,70 X
- Media das propostas validas: R$ Y (criterio alternativo)
- 70% da media: R$ 0,70 Y

PROPOSTA <70% do criterio aplicavel -> presuncao de inexequibilidade
PROPOSTA >=70% -> presuncao de exequibilidade (mas pode ser questionada com fundamentacao)
```

**Onus probatorio:** PA-14 - apos a presuncao incidir, o licitante tem **onus** de demonstrar viabilidade com planilha de custos (art. 64 - diligencia). Distribuicao dinamica nao se aplica automaticamente.

## 4. Modo DEFESA - quando a proposta do cliente esta sob suspeita

### Cenarios:
- Proposta abaixo de 70% (presuncao incide).
- Proposta entre 70% e 80% (presuncao nao incide mas pode ser questionada por concorrente ou pelo proprio agente).

### Estrategia de defesa:
1. **Planilha de custos detalhada** (PA-09 - sigiloso, em `<cwd>/licitacoes/casos/<slug>/arquivos/`):
   - Insumos diretos (materia-prima, mao-de-obra direta, equipamentos).
   - Custos indiretos (BDI - encargos sociais conforme legislacao, tributos federais/estaduais/municipais aplicaveis, despesas indiretas, lucro).
   - Memorial de calculo - cada item rastreavel.
   - Comprovacao documental (cotacoes de fornecedores, planilhas de mao-de-obra, dados oficiais).

2. **Demonstracao de viabilidade tecnica e economica:**
   - Capacidade operacional ja instalada (custo marginal baixo).
   - Compras em grande volume (vantagem de escala).
   - Equipamentos depreciados (sem necessidade de reposicao no contrato).
   - Subsidios cruzados internos (mas evitar invocar para nao parecer pratica anti-competitiva).
   - Inovacao tecnologica ou metodo proprio (eficiencia diferenciada).

3. **Resposta formal a diligencia** (art. 64 Lei 14.133):
   - Documentos solicitados pelo agente, prazo cumprido.
   - Memorial juridico fundamentado (lei + sumula TCU + jurisprudencia).
   - Vinculacao ao instrumento (PA-15) - proposta cumpre o objeto do edital.

### Estrutura da peca defensiva:

```
EXMO. [AGENTE DE CONTRATACAO / COMISSAO]
PROCESSO [n°] - EDITAL [n°]

RESPOSTA A DILIGENCIA - COMPROVACAO DE EXEQUIBILIDADE
(art. 59 §4º + art. 64 Lei 14.133/2021)

I - DA DILIGENCIA
Em [DD/MM/AAAA] esta Empresa foi notificada para comprovar a exequibilidade
de sua proposta no valor de R$ [X] (referencial R$ [Y] - relacao [Z]%).

II - DA EXEQUIBILIDADE - FUNDAMENTACAO TECNICA
[Planilha de custos detalhada anexa]
- Custos diretos: R$ [a]
- Custos indiretos (BDI): R$ [b]
- Margem operacional: R$ [c]
- Total: R$ [a+b+c]

Cada item rastreavel a [cotacoes / dados oficiais / experiencia operacional].

III - DEMONSTRACAO DE VIABILIDADE
[Capacidade instalada + escala + eficiencia - fundamentar sem comprometer
sigilo de segredo industrial Lei 9.279/96 art. 195 XI]

IV - FUNDAMENTOS LEGAIS
- Art. 59 §4º Lei 14.133/2021 - presuncao **relativa** (jurisprudencia TCU)
- Sum. TCU 269 - formalismo moderado (saneamento e admitido)
- Vinculacao ao edital (art. 12 + 25 Lei 14.133) - proposta cumpre o objeto
- CC art. 422 - boa-fé objetiva
- PA-14 - onus de exequibilidade cumprido com planilha + documentos

V - DOS PEDIDOS
a) Acolhimento da resposta a diligencia como tecnicamente fundada;
b) Manutencao da Impugnante na disputa (classificacao da proposta).

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}} - OAB/{{OAB_UF}} {{OAB_NUMERO}}

---
[Ressalva OAB - PA-07]
```

## 5. Modo ATAQUE - quando concorrente apresenta proposta inexequivel

### Cenarios:
- Concorrente classificado em primeiro lugar com proposta abaixo de 70%.
- Concorrente sem capacidade operacional aparente para o preco apresentado.

### Estrategia de ataque:
1. **Intencao de recurso motivada NA SESSAO** (art. 165 §1º) - obrigatorio sob pena de preclusao.
2. **Razoes em 3 dias uteis** (art. 165) - peca completa.
3. **Pedido principal:** desclassificacao do concorrente pelo art. 50 II + art. 59 §4º.
4. **Pedido sucessivo:** diligencia obrigatoria (art. 64) ao concorrente; manutencao da decisao se nao demonstrar.
5. **Fundamentacao tecnica:** demonstrar com **dados publicos de mercado** (precos de insumos, planilhas oficiais, jurisprudencia TCU) que a proposta abaixo de 70% nao e viavel para o objeto.

### Estrutura da peca de ataque:

```
EXMO. [AUTORIDADE COMPETENTE]
PROCESSO [n°] - EDITAL [n°]

RAZOES DE RECURSO ADMINISTRATIVO
(art. 165 Lei 14.133/2021 - 3 dias uteis - tempestivo)

I - PRELIMINAR DE TEMPESTIVIDADE E LEGITIMIDADE
- Intencao manifestada na sessao publica de [DD/MM/AAAA] - tempestiva (art. 165 §1º)
- Razoes apresentadas em [DD/MM/AAAA] - dentro dos 3 dias uteis
- Recorrente: licitante classificada em [posicao]

II - DOS FATOS
A Concorrente [X] apresentou proposta de R$ [W] - relacao [Z]% do referencial.
A presuncao de inexequibilidade do art. 59 §4º Lei 14.133/2021 incide.

III - DO DIREITO

III.1 - Art. 59 §4º Lei 14.133/2021 - presuncao **relativa** de inexequibilidade
III.2 - Sum. TCU [referencias sobre exequibilidade]
III.3 - Vinculacao ao edital (PA-15) - art. 12 Lei 14.133
III.4 - Onus do concorrente em comprovar (PA-14)

IV - DA INVIABILIDADE TECNICA DA PROPOSTA DO CONCORRENTE
[Dados publicos de mercado + planilha de custos do segmento + jurisprudencia TCU
de propostas analogas desclassificadas]

V - DOS PEDIDOS
a) Conhecimento e provimento do recurso;
b) Desclassificacao da Concorrente [X] pelo art. 50 II + art. 59 §4º Lei 14.133;
c) Subsidiariamente, diligencia obrigatoria (art. 64) com prazo certo;
d) Subsidiariamente, manutencao da Concorrente se demonstrar inequivocamente.

[Cidade], [DD/MM/AAAA]
___________________________________
{{ADVOGADO_NOME}} - OAB/{{OAB_UF}} {{OAB_NUMERO}}

---
[Ressalva OAB - PA-07]
```

## 6. Vedacoes especificas

- **PA-04** - Selo. **PA-09** - sigilo da planilha de custos (a sua e a do concorrente quando acessada).
- **PA-14** - onus probatorio: licitante demonstra; nao se inverte automaticamente.
- **PA-15** - argumentos ancorados na vinculacao ao instrumento.
- **PA-02** - sem promessa de provimento.
- **PA-07** - ressalva OAB. **PA-08** - sem critica pessoal.

## 7. Protocolos acionados

- **P1** Selo. **P2** integridade da proposta + planilha. **P3** memoria de calculo auditavel. **P6** R1-R4.

## 8. Localizacao

Federal -> TCU paradigma. Estadual/municipal -> TCE/TCM + regulamento local. `[VERIFICAR]` regulamento UF/Municipio.

## 9. Integracao

**Chamada por:** `licitacoes-master`, `planejamento-proposta`, `recurso-administrativo`.

**Entrega para:** operador (peca defensiva ou de ataque) + `CASO.md`. Aciona `recurso-administrativo` (modo ataque) ou `contrarrazoes-recurso` (modo defesa contra recurso de concorrente). Entrega final passa por `revisao-final-licitacoes`.

**Sem esta skill:** licitante-cliente desclassificado por nao defender exequibilidade; ou perde oportunidade de desclassificar concorrente inexequivel (preclusao na sessao).
