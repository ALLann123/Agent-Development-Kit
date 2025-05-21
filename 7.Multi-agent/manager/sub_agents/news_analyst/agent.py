#!/usr/bin/python3
from google.adk.agents import Agent
import os
from tavily import TavilyClient
from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm

load_dotenv()
#build tool and provide api
def search_online(user_search:str)-> dict:
    tavily_client=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    response=tavily_client.search(user_search)
    return response

news_analyst=Agent(
    name="news_analyst",
    model=LiteLlm(model="groq/llama3-70b-8192"),
    description="News Analyst Agent",
    instruction="""
        You are a helpful assistant that can analyze news articles and provide a summary of the news.
        When asked about news use the provide tool below to gather information about the news:
        -search_online
        If the user ask for news using a relative time, you should use the get_current_time tool to get the current time to use in the search query. 
    """,
    tools=[search_online],
)

