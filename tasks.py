from crewai import Task

research_task = Task(
    description=(
        "Conduct a comprehensive market analysis. Include competitor insights, "
        "target demographics, and current trends. Identify opportunities for the campaign."
    ),
    expected_output="A concise 2–3 paragraph market analysis report.",
)

strategy_task = Task(
    description=(
        "Based on the research, create a strategic marketing plan. "
        "Include audience, message, channels, and campaign timeline."
    ),
    expected_output="A 3–4 paragraph marketing campaign plan.",
)

optimization_task = Task(
    description=(
        "Evaluate the plan for weaknesses. Recommend improvements, performance KPIs, and tracking ideas."
    ),
    expected_output="A 2-paragraph optimization summary with actionable KPIs.",
)
