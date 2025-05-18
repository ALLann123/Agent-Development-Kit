#!/usr/bin/python3
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

#build tool and provide api
def search_online(user_search:str)-> str:
    tavily_client=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    response=tavily_client.search(user_search)
    return response

root_agent = Agent(
    name="tool_agent",
    model=LiteLlm(model="groq/llama3-70b-8192"),
    description="Tool agent",
    instruction="""
    You are a helpful online search assistant that can use the following tool:
    - search_online
    Use the information provided by the tool above to answer the users question.
""",
    tools=[search_online],
)
