#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Licitacoes Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-revisao`, `--quick`, `--no-r1r4`, `/revisao off`.
3. Detecta GATILHO LICITATORIO via keywords (3 niveis):
   - Gatilho 1: prompt contem palavras do dominio de licitacoes e contratos
     administrativos
   - Gatilho 2: keywords fortes do dominio (Lei 14.133, edital, pregao, SRP,
     RDC, impugnacao, recurso, TCU, sancao, inidoneidade, reequilibrio, etc.)
   - Gatilho 3: comandos `/start-licitacoes`, `/licitacoes-master`, etc.
4. Se gatilho dispara:
   - Verifica se `licitacoes/cowork-state.json` existe no path atual
   - SIM: injeta protocolo Revisao Tecnica R1-R4 + aponta para skill
     `licitacoes-master`
   - NAO: sugere `/start-licitacoes` ao usuario (mas nao bloqueia)
5. Se ha bypass: reafirma em stdout que o bypass foi aceito (transparencia).
6. Se nao eh tarefa licitatoria: silencio (exit 0 sem output).

Tambem respeita state.json: se `revisao_tecnica.enabled = false`, nunca injeta R1-R4.

Stdlib only.
"""

from __future__ import annotations

import io
import json
import os
import re
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).resolve().parent
PLUGIN_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))

import importlib.util
spec = importlib.util.spec_from_file_location("hook_utils", PLUGIN_ROOT / "scripts" / "hook-utils.py")
hook_utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook_utils)


# Gatilho 1: palavras genericas do dominio de licitacoes e contratos administrativos
TRIGGER_LICITACOES = [
    r"\blicita[çc][ãa]o\b", r"\blicita[çc][õo]es\b",
    r"\bcontrato\s+administrativo\b", r"\bcontratos\s+administrativos\b",
    r"\bdireito\s+administrativo\b",
    r"\bcompras\s+publicas\b", r"\bcompras\s+p[úu]blicas\b",
    r"\bcontratacao\s+publica\b", r"\bcontrata[çc][ãa]o\s+p[úu]blica\b",
    r"\badministracao\s+publica\b", r"\badministra[çc][ãa]o\s+p[úu]blica\b",
    r"\bedital\b", r"\beditais\b",
]

# Gatilho 2: keywords fortes do dominio licitatorio brasileiro
DOMAIN_KEYWORDS = [
    # Modalidades licitatorias
    r"\bpreg[ãa]o\b", r"\bpreg[ãa]o\s+eletr[ôo]nico\b",
    r"\bconcorr[êe]ncia\b", r"\bconcurso\b", r"\bleil[ãa]o\b",
    r"\bdialogo\s+competitivo\b", r"\bdi[áa]logo\s+competitivo\b",
    r"\bdispensa\s+de\s+licita[çc][ãa]o\b", r"\bdispensa\s+eletr[ôo]nica\b",
    r"\binexigibilidade\b",
    # Sistemas e regimes
    r"\bSRP\b", r"\bsistema\s+de\s+registro\s+de\s+pre[çc]os\b",
    r"\bata\s+de\s+registro\s+de\s+pre[çc]os\b",
    r"\bRDC\b", r"\bregime\s+diferenciado\b",
    r"\bPPP\b", r"\bparceria\s+p[úu]blico[\-\s]privada\b",
    r"\bconcess[ãa]o\b", r"\bpermiss[ãa]o\s+de\s+servi[çc]o\s+p[úu]blico\b",
    # Documentos pre-edital e edital
    r"\bETP\b", r"\bestudo\s+t[ée]cnico\s+preliminar\b",
    r"\btermo\s+de\s+refer[êe]ncia\b", r"\bTR\b",
    r"\bprojeto\s+b[áa]sico\b", r"\bprojeto\s+executivo\b",
    r"\bmatriz\s+de\s+risco\b", r"\bmapa\s+de\s+riscos\b",
    r"\bpesquisa\s+de\s+pre[çc]os\b",
    # Habilitacao e fases
    r"\bhabilita[çc][ãa]o\b", r"\binabilita[çc][ãa]o\b",
    r"\bSICAF\b", r"\bPNCP\b",
    r"\batestado\s+de\s+capacidade\s+t[ée]cnica\b", r"\bCAT\b",
    r"\bqualifica[çc][ãa]o\s+t[ée]cnica\b",
    r"\bqualifica[çc][ãa]o\s+econ[ôo]mico[\-\s]financeira\b",
    r"\bregularidade\s+fiscal\b", r"\bCND\b", r"\bCNDT\b",
    r"\bdesclassifica[çc][ãa]o\b", r"\binexequibilidade\b",
    # Impugnacao e recursos
    r"\bimpugna[çc][ãa]o\s+ao\s+edital\b", r"\bimpugna[çc][ãa]o\b",
    r"\brecurso\s+administrativo\b", r"\brecurso\s+hier[áa]rquico\b",
    r"\bcontrarraz[õo]es\b",
    r"\bpedido\s+de\s+esclarecimento\b",
    # Sancoes e penalidades
    r"\bsan[çc][ãa]o\s+administrativa\b", r"\bsan[çc][õo]es\s+administrativas\b",
    r"\badvertencia\b", r"\bmulta\s+contratual\b",
    r"\bimpedimento\s+de\s+licitar\b", r"\binidoneidade\b",
    r"\bdeclara[çc][ãa]o\s+de\s+inidoneidade\b",
    r"\bapenamento\b", r"\bdosimetria\b",
    r"\bPAR\b", r"\bprocesso\s+administrativo\s+de\s+responsabiliza[çc][ãa]o\b",
    r"\bLei\s+anticorrup[çc][ãa]o\b", r"\bacordo\s+de\s+leni[êe]ncia\b",
    r"\bprograma\s+de\s+integridade\b", r"\bcompliance\s+p[úu]blico\b",
    # Contrato administrativo
    r"\bclausulas\s+exorbitantes\b", r"\bcl[áa]usulas\s+exorbitantes\b",
    r"\bgarantia\s+contratual\b", r"\bseguro[\-\s]garantia\b",
    r"\bfian[çc]a\s+banc[áa]ria\b",
    r"\baditivo\s+contratual\b", r"\btermo\s+de\s+apostilamento\b",
    r"\breequilibrio\s+economico[\-\s]financeiro\b", r"\breequil[íi]brio\b",
    r"\brevis[ãa]o\s+contratual\b", r"\brepactua[çc][ãa]o\b",
    r"\breajuste\s+contratual\b",
    r"\brescis[ãa]o\s+contratual\b", r"\brescis[ãa]o\s+unilateral\b",
    r"\bteoria\s+da\s+imprevis[ãa]o\b",
    r"\bordem\s+cronol[óo]gica\s+de\s+pagamento\b",
    # Controle externo
    r"\bTCU\b", r"\bTCE\b", r"\btribunal\s+de\s+contas\b",
    r"\bac[óo]rd[ãa]o\s+TCU\b", r"\bsumula\s+TCU\b", r"\bs[úu]mula\s+TCU\b",
    r"\brepresenta[çc][ãa]o\b", r"\btomada\s+de\s+contas\b",
    r"\bsustacao\s+de\s+ato\b", r"\bdetermina[çc][ãa]o\b",
    r"\bCGU\b", r"\bcontroladoria\s+geral\b",
    # Medidas judiciais
    r"\bmandado\s+de\s+seguran[çc]a\b", r"\bMS\s+preventivo\b",
    r"\bacao\s+anulat[óo]ria\b", r"\ba[çc][ãa]o\s+anulat[óo]ria\b",
    r"\bacao\s+de\s+obriga[çc][ãa]o\s+de\s+fazer\b",
    r"\bacao\s+de\s+cobran[çc]a\b",
    r"\bacao\s+de\s+ressarcimento\b",
    r"\bsuspens[ãa]o\s+de\s+seguran[çc]a\b",
    r"\bautotutela\s+administrativa\b",
    # Improbidade administrativa
    r"\bimprobidade\s+administrativa\b",
    r"\bLei\s+8\.?429\b", r"\bLei\s+14\.?230\b",
    r"\bressarcimento\s+ao\s+er[áa]rio\b",
    # Legislacao chave
    r"\bLei\s+14\.?133\b", r"\bnova\s+lei\s+de\s+licita[çc][õo]es\b",
    r"\bLei\s+8\.?666\b",
    r"\bLei\s+10\.?520\b", r"\bLei\s+12\.?462\b",
    r"\bLei\s+11\.?079\b", r"\bLei\s+8\.?987\b",
    r"\bLei\s+13\.?303\b", r"\bestatuto\s+das\s+estatais\b",
    r"\bLei\s+12\.?846\b", r"\bLei\s+12\.?527\b", r"\bLAI\b",
    r"\bLei\s+13\.?140\b", r"\bLei\s+9\.?307\b",
    r"\bDecreto\s+10\.?024\b", r"\bDecreto\s+11\.?246\b", r"\bDecreto\s+11\.?129\b",
    r"\bIN\s+SEGES\b", r"\bIN\s+MGI\b",
    # ME/EPP e tratamento diferenciado
    r"\bME/EPP\b", r"\bmicroempresa\b",
    r"\bempate\s+ficto\b",
    r"\bcota\s+reservada\b", r"\bmargem\s+de\s+prefer[êe]ncia\b",
    r"\bLC\s+123\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-licitacoes",
    "/licitacoes-master",
    "/caso-licitacao",
    "/triagem",
    "/edital",
    "/impugnacao",
    "/recurso",
    "/contrato",
    "/sancao",
    "/judicial",
    "/revisao-final",
    "/status-licitacoes",
]

# Keywords gerais (fallback - protocolo cauteloso quando casa generico)
LICITAC_KEYWORDS_GENERAL = [
    r"\bfornecedor\b", r"\blicitante\b",
    r"\bcontratado\b", r"\bcontratada\b",
    r"\b[óo]rg[ãa]o\s+p[úu]blico\b", r"\bente\s+federativo\b",
    r"\borgao\s+contratante\b", r"\bgestor\s+do\s+contrato\b",
    r"\bfiscaliza[çc][ãa]o\s+do\s+contrato\b",
    r"\badvocacia\s+empresarial\s+em\s+licita[çc][õo]es\b",
]

BYPASS_TOKENS = [
    "--no-revisao",
    "--no-r1r4",
    "--quick",
    "/revisao off",
    "/revisao-off",
]


def _load_input() -> dict:
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except Exception:
        return {}


def _matches_any(text: str, patterns: list[str]) -> bool:
    for pat in patterns:
        if re.search(pat, text, re.IGNORECASE):
            return True
    return False


def _is_licitacoes(prompt: str) -> bool:
    """Detecta se o prompt e do dominio licitatorio (gatilhos 1, 2 ou 3)."""
    if _matches_any(prompt, TRIGGER_LICITACOES):
        return True
    if _matches_any(prompt, DOMAIN_KEYWORDS):
        return True
    low = prompt.lower()
    for cmd in PLUGIN_COMMANDS:
        if cmd.lower() in low:
            return True
    return False


def _is_licitacoes_general(prompt: str) -> bool:
    """Detecta tarefa licitatoria em geral (sem keyword forte)."""
    return _matches_any(prompt, LICITAC_KEYWORDS_GENERAL)


def _has_bypass(prompt: str) -> str | None:
    low = prompt.lower()
    for token in BYPASS_TOKENS:
        if token in low:
            return token
    return None


def _has_licitacoes_state(cowork: Path | None) -> bool:
    """Verifica se existe `licitacoes/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "licitacoes" / "cowork-state.json").exists()


def _revisao_tecnica_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica revisao_tecnica.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "licitacoes" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("revisao_tecnica", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env LICITAC_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("LICITAC_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "licitacoes" / "cowork-state.json").exists():
            return p
    return hook_utils.find_cowork(Path.cwd())


def main() -> int:
    payload = _load_input()
    prompt = payload.get("prompt") or payload.get("user_prompt") or ""
    if not isinstance(prompt, str) or not prompt.strip():
        return 0

    cowork = _resolve_cowork()
    bypass = _has_bypass(prompt)

    is_licitacoes = _is_licitacoes(prompt)
    is_licitacoes_other = _is_licitacoes_general(prompt) and not is_licitacoes

    # Caso 1: bypass explicito
    if bypass and (is_licitacoes or is_licitacoes_other):
        sys.stdout.write(
            f"[licitacoes-adv-os] Bypass detectado ({bypass}). "
            "Pecas, pareceres e estrategias serao entregues SEM a "
            "Revisao Tecnica R1-R4. Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa licitatoria + plugin configurado
    if is_licitacoes and _has_licitacoes_state(cowork):
        if not _revisao_tecnica_enabled(cowork):
            sys.stdout.write(
                "[licitacoes-adv-os] Demanda licitatoria detectada. "
                "Revisao Tecnica DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: licitacoes-master.\n"
            )
        else:
            sys.stdout.write(
                "[licitacoes-adv-os] Demanda licitatoria detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `licitacoes-master` (Tier 0 - sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as 22 Proibicoes Absolutas (PA-01 a PA-22), com atencao especial:\n"
                "   - PA-01: vedacao a opinar sobre conveniencia administrativa (plugin e JURIDICO)\n"
                "   - PA-04: Selo de Validacao Legal Previa antes de qualquer estrategia (P1)\n"
                "   - PA-03: datar parecer/peca pelo regime aplicavel (Lei 14.133 vs Lei 8.666 transicao)\n"
                "   - PA-09: dados sigilosos de empresa cliente NUNCA no plugin (LGPD + segredo industrial)\n"
                "   - PA-10: confidencialidade processual oponivel (recursos administrativos)\n"
                "   - PA-12: independencia das esferas (administrativa != TCU != judicial)\n"
                "   - PA-14: empresa licitante (subjetiva) vs Administracao (objetiva)\n"
                "   - PA-07: a saida e rascunho operacional - responsabilidade tecnica do advogado (OAB)\n"
                "4. Acionar os 6 Protocolos da Camada 2 conforme demanda\n"
                "   (P1 Vigencia legal, P2 Integridade documental, P3 Memoria de decisao,\n"
                "    P4 Cruzamento Administrativo+TCU+Judicial, P5 Localizacao do ente,\n"
                "    P6 Revisao R1-R4)\n"
                "5. Antes de entregar: Revisao Tecnica R1->R2->R3->R4 (skill `revisao-final-licitacoes`)\n"
                "\n"
                "Bypass disponivel: `--no-revisao`, `--quick`, `/revisao off`.\n"
            )
        return 0

    # Caso 3: tarefa licitatoria mas plugin NAO configurado
    if is_licitacoes and not _has_licitacoes_state(cowork):
        sys.stdout.write(
            "[licitacoes-adv-os] Detectei demanda licitatoria, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-licitacoes para configurar (~5 min).\n"
            "Vou criar uma pasta `licitacoes/` aqui com a identidade do "
            "advogado/escritorio, OAB, cidade/UF, area de foco (consultivo / contencioso administrativo / TCU / judicial), "
            "tom de voz e configuracao das skills.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa licitatoria geral - protocolo cauteloso
    if is_licitacoes_other:
        sys.stdout.write(
            "[licitacoes-adv-os] Tarefa licitatoria detectada (sem frente especifica). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas - exigir dado real do caso).\n"
            "2. Apresentar estrutura + premissas antes de redigir peca/parecer.\n"
            "3. Aguardar confirmacao do advogado-operador.\n"
            "4. Antes de entregar: executar Revisao Tecnica R1-R4 se aplicavel.\n"
            "Bypass: `--no-revisao`, `--quick`, `/revisao off`.\n"
        )
        return 0

    # Caso default: nao e tarefa licitatoria - silencio
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
