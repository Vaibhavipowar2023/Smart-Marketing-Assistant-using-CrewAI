from crewai import Crew, Process
from agents import market_research_analyst, campaign_strategist, performance_analyst
from tasks import research_task, strategy_task, optimization_task

# Assign agents to tasks
research_task.agent = market_research_analyst
strategy_task.agent = campaign_strategist
optimization_task.agent = performance_analyst

# Build the crew
marketing_crew = Crew(
    agents=[market_research_analyst, campaign_strategist, performance_analyst],
    tasks=[research_task, strategy_task, optimization_task],
    process=Process.sequential
)
