#!/usr/bin/python3
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.news_analyst.agent import news_analyst
from .sub_agents.stock_analyst.agent import stock_analyst
from .tools.tools import get_current_time
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    name="manager",
    model=LiteLlm(model="groq/llama3-70b-8192"),
    description="Manager agent",
    instruction="""
        You are a manager agent that routes requests to specialized sub-agents.
        
        ROUTING RULES:
        1. For jokes/humor -> Immediately route to funny_nerd (DO NOT respond yourself)
        2. For stock/financial questions -> Immediately route to stock_analyst
        3. For news requests -> Use the news_analyst tool
        4. For time requests -> Use get_current_time
        
        IMPORTANT: 
        - When routing, use EXACTLY this format: <<TRANSFER_TO::agent_name>>
        - Never show the transfer command to users
        - Never respond to these topics yourself
        
        Examples:
        User: Tell me a joke
        Response: <<TRANSFER_TO::funny_nerd>>
        
        User: Tesla stock price
        Response: <<TRANSFER_TO::stock_analyst>>
    """,
    sub_agents=[stock_analyst, funny_nerd],
    tools=[
        AgentTool(news_analyst),
        get_current_time,
    ]
)