from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile", temperature=0),
    tools=[DuckDuckGoTools()],
    # CORRECTED: Use 'instructions' and put the string in a list
    instructions=["Always include sources"], 
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get Financial Data",
    model=Groq(id="llama-3.3-70b-versatile", temperature=0),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    # CORRECTED: Use 'instructions' and put the string in a list
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile", temperature=0),
    instructions=["Always include sources", "Use Tools to display data"],
    show_tool_calls=True,
    markdown=True
)

agent_team.print_response("What is the market outlook and financial performance of AI semiconductor companies")