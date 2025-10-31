import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from crewai_tools import SerperDevTool

load_dotenv()

# ✅ Use OpenRouter free model
llm = LLM(
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-oss-20b:free",  # free model
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

search_tool = SerperDevTool()

# --- Agents ---
market_research_analyst = Agent(
    role="Market Research Analyst",
    goal="Research audience, competitors, and marketing trends.",
    backstory="Expert analyst specializing in consumer behavior and market insights.",
    tools=[search_tool],
    llm=llm,
    verbose=True,
)

campaign_strategist = Agent(
    role="Marketing Campaign Strategist",
    goal="Develop an effective, creative campaign plan.",
    backstory="Creative strategist skilled in translating insights into engaging campaigns.",
    tools=[search_tool],
    llm=llm,
    verbose=True,
)

performance_analyst = Agent(
    role="Performance Analyst",
    goal="Analyze and optimize campaign performance.",
    backstory="Data-driven expert focused on actionable KPIs and ROI.",
    tools=[search_tool],
    llm=llm,
    verbose=True,
)
