import os
import requests
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.tools import tool
from langchain.agents.agent_types import AgentType

import streamlit as st

API_BASE = st.secrets["FASTAPI_BASE_URL"]

@tool
def get_university_contact(university: str) -> str:
    """Gets contact info for a given university name."""
    try:
        url = API_BASE + university.replace(" ", "%20")
        res = requests.get(url)
        data = res.json()
        if 'contact' in data:
            c = data['contact']
            return (
                f"Contact for {university.title()}:\n"
                f"Phone: {c['phone']}\n"
                f"Email: {c['email']}\n"
                f"Website: {c['website']}"
            )
        return data.get("error", "No info found.")
    except Exception as e:
        return f"Error: {str(e)}"

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2, openai_api_key=st.secrets["OPENAI_API_KEY"])
agent = initialize_agent([get_university_contact], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False)

def ask_chatbot(message):
    return agent.run(message)
