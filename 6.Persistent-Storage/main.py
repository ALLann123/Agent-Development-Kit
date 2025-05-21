#!/usr/bin/python3
import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from memory_agent.agent import memory_agent
from utils import call_agent_async

load_dotenv()

#Initialize persistent session service
#Use SQLite database
db_url="sqlite:///.my_agent_data.db"
session_service=DatabaseSessionService(db_url=db_url)

#define the initial state
initial_state={
    "user_name":"Allan Karis",
    "reminders":[],
}


async def main_async():
    #setup constants
    APP_NAME="Memory Agent"
    USER_ID="own_the_net"

    #check for existing sessions fot this user
    existing_sessions=session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID,
    )

    #if there is existing session use it and if not create a new one
    if existing_sessions and len(existing_sessions.sessions) > 0:
        #Use the most recent session
        SESSION_ID=existing_sessions.sessions[0].id
        print(f"Continue existing sessions:{SESSION_ID}")
    else:
        #create a new session with initial state
        new_session = session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state,
        )
        SESSION_ID = new_session.id
        print(f"New session created: {SESSION_ID}")

    
    #create a runner with the memory agent
    runner=Runner(
        agent=memory_agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    #interactive conversation
    print("\n Welcome to Memory Agent Chat!")
    print("Reminders will be remembered for you🎆🎇")
    print("Type 'exit' or 'quit' to end conversation")

    while True:
        #get user input
        user_input=input("\nYou: ")

        if user_input.lower() in ['exit', 'quit']:
            print("[+]Saving current session.....")
            print("Bye!")
            break

        #process the user query through the agent
        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)


if __name__ == "__main__":
    asyncio.run(main_async())



"""
python .\main.py
Continue existing sessions:72f0110e-9fee-49a2-bf86-5ce3582acab6

 Welcome to Memory Agent Chat!
Reminders will be remembered for you🎆🎇
Type 'exit' or 'quit' to end conversation

You: current reminders?

--- Running Query: current reminders? ---

---------- State BEFORE processing ----------
👤 User: Allan Karis
📝 Reminders: None
---------------------------------------------
Event ID: C9hXbycC, Author: memory_agent
--- Tool: add_reminder called for 'Do laundry during the weekend' ---
Event ID: pBJAY4dZ, Author: memory_agent
Event ID: 3zFRKuc0, Author: memory_agent
  Text: 'Hi Allan!

Here are your current reminders:

1. Do laundry during the weekend
2. Read on Sunday night to prepare for your exams

Let me know if you need any more help!'

╔══ AGENT RESPONSE ═════════════════════════════════════════
Hi Allan!

Here are your current reminders:

1. Do laundry during the weekend
2. Read on Sunday night to prepare for your exams

Let me know if you need any more help!
╚═════════════════════════════════════════════════════════════
"""
