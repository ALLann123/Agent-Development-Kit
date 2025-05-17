#!/usr/bin/python3
from google.adk.agents import Agent
from dotenv import load_dotenv
import os
from google.adk.models.lite_llm import LiteLlm

#my first agent
root_agent=Agent(
    name="greeting_agent",
    model=LiteLlm(model="groq/llama3-70b-8192"),
    #helps in work delegation of agents
    description="Greeting Agent",
    instruction="""
    You are a helpful assistant that greets the user. Ask
    for the user's name and greet them by name
    """,
)



