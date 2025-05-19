#!/usr/bin/python
from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field
from google.adk.models.lite_llm import LiteLlm

#we use pydantic to define the output schema
class EmailContent(BaseModel):
    subject: str=Field(
        description="The subject line of the Email. Should be concise and descriptive."
    )
    body: str=Field(
        description=" The main content of the email. Should be well formated with proper greeting, paragraphs, and signature."
    )

    #create the email generator agent
root_agent=LlmAgent(
    name="email_agent",
    model=LiteLlm(model="groq/llama3-70b-8192"),
    instruction="""
    You are an Email Generation Assistant.
        Your task is to generate a professional email based on the user's request.

        GUIDELINES:
        - Create an appropriate subject line (concise and relevant)
        - Write a well-structured email body with:
            * Professional greeting
            * Clear and concise main content
            * Appropriate closing
            * Your name as signature
        - Suggest relevant attachments if applicable (empty list if none needed)
        - Email tone should match the purpose (formal for business, friendly for colleagues)
        - Keep emails concise but complete

        IMPORTANT: Your response MUST be valid JSON matching this structure:
        - Your response MUST be a **valid, single-line JSON** string matching this exact structure:
        {
            "subject": "Subject line here",
            "body": "Email body here with proper paragraphs and formatting",
        }

        DO NOT include any explanations or additional text outside the JSON response.
""",
    description="Generate professional emails with structured subject and body.",
    output_schema=EmailContent,
    output_key="email"
)