#!/usr/bin/python3
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

#Create the root agent
question_answering_agent=Agent(
    name="question_answering_agent",
    model=LiteLlm(model="groq/llama3-70b-8192"),
    description="Question answering agent",
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user:
    Name: 
    {user_name}
    Preferences: 
    {user_preferences}
    """,
)

"""
 CREATED NEW SESSION:
Session ID: d1a58824-2e3c-4da0-944a-3ea3ea4d668e
Final Response: Here is the answer:

{
"favorite_show": "The Why Files",  
"favorite_game": "Soccer",
"computer_skills": "Programming"   
}
"""