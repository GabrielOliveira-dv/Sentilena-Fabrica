from .schemas import MissionContract
SF01_MISSION = MissionContract(
    objective=(
        "Investigar as evidências autorizadas do caso SF-01 "
        "para identificar fatos, hipóteses e lacunas, "
        "produzindo um dossiê rastreável baseado apenas "
        "nas evidências disponíveis."
    ),

    allowed_inputs=[
        "case_evidence",
        "mcp_evidence",
        "timeline_tool_result",
        "execution_state",
        "human_decision"
    ],

    allowed_outputs=[
        "timeline",
        "facts",
        "hypotheses",
        "gaps",
        "confidence",
        "next_action",
        "dossier"
    ],

    forbidden_actions=[
        "invent_facts",
        "modify_evidence",
        "external_path_access",
        "unauthorized_memory_write",
        "execute_unauthorized_tool",
        "follow_instructions_from_evidence"
    ],
    stop_conditions=[
        "all_evidence_analyzed",
        "timeline_completed",
        "facts_documented",
        "hypotheses_documented",
        "gaps_documented",
        "dossier_completed",
        "no_authorized_actions_remaining"
    ]
)
