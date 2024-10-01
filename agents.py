import os
from crewai import Agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.tools import DuckDuckGoSearchRun
import streamlit as st

search_tool = DuckDuckGoSearchRun()

load_dotenv()

key = "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"

llm = ChatGroq(model="gemma2-9b-it", verbose=True, temperature=0.7, key)

def streamlit_callback(step_output):
    st.markdown("---")
    for step in step_output:
        if isinstance(step, tuple) and len(step) == 2:
            action, observation = step
            if isinstance(action, dict):
                st.markdown(f"# Action")
                st.markdown(f"**Tool:** {action.get('tool', '')}")
                st.markdown(f"**Tool Input:** {action.get('tool_input', '')}")
                st.markdown(f"**Log:** {action.get('log', '')}")
                st.markdown(f"**Action:** {action.get('action', '')}")
            elif isinstance(action, str):
                st.markdown(f"**Action:** {action}")

            st.markdown(f"**Observation:** {str(observation)}")

class RoastAgent:

    def r1(self):
        return Agent(
            role='Resume Roaster',
            goal=""" This is the resume of a person, write a funny, brutal and uncensored very disrespectful roast for them. if given data doesn't seems like resume then tell me to upload resume and give me at least 300 words response and in proper text. also add emoji in resume and see your response should directly mention the person by you whoese resume it is""",
            backstory="""You are very Famous Resume Roaster""",
            tools=[search_tool],
            llm=llm,
            verbose=False,
            #step_callback=streamlit_callback,
        )

        
