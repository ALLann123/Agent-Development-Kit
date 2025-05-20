#!/usr/bin/python3
import uuid
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answering_agent import agent

load_dotenv()

#create a new session service to store state
session_service_stateful=InMemorySessionService()

initial_state={
    "user_name": "Allan Mbugua",
    "user_preferences":"""
        I like to play soccer, watch Man Utd games and programming
        My favorite food chapati.
        TV show I like The Why Files.
        Quote: No one cared who I was till I put on the mask!!
"""
}

#create a new sesison
APP_NAME="Allan Bot"
USER_ID="own_the_net"
SESSION_ID= str(uuid.uuid4())

stateful_session=session_service_stateful.create_session(
    app_name= APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)

print("\n CREATED NEW SESSION:")
print(f"Session ID: {SESSION_ID}")

runner= Runner(
    agent= agent.question_answering_agent,
    app_name= APP_NAME,
    session_service= session_service_stateful,
)

new_message=types.Content(
    role="user", parts=[types.Part(text="What is his favorite show, game he played, and what computer skills does he have. Provide answer in json format")]
)

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

        