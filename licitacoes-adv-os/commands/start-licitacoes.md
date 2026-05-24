---
description: Wizard de onboarding inicial - configura identidade, OAB, escritorio, AREA_FOCO, frentes, tom, modo. Cria persona local + state-schema. Alerta agressivo sobre sigilo comercial (proposta, planilha, segredo industrial - Lei 9.279/96 art. 195 XI).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [opcional - tipo de configuracao]
---

Voce foi acionado pelo comando `/start-licitacoes` do plugin Licitacoes Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** wizard de onboarding inicial - personalizar o plugin ao perfil do escritorio especialista em licitacoes.

## PROTOCOLO

1. **Acionar a skill `onboarding-licitacoes`** - ela conduz o wizard em 10 blocos.
2. Coleta: identidade (nome, OAB, UF), escritorio, cidade+UF, AREA_FOCO (consultivo-edital / contencioso-administrativo / tcu-tce / judicial / todos), frentes, subdominios, tom de voz, modo de melhor saida.
3. Cria persona local + state-schema em `<cwd>/licitacoes/`.
4. **Alerta agressivo** sobre sigilo comercial (Lei 14.133 arts. 13 §3º e 17 + Lei 9.279/96 art. 195 XI) - pasta sincronizada (iCloud/OneDrive/Dropbox/Drive) e risco LGPD + concorrencia desleal.
5. **Idempotente** - se ja existe state, perguntar atualizar vs recriar.

**Skill a acionar:** `onboarding-licitacoes`.
