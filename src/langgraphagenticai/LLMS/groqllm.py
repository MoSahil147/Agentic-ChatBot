# import os
# import streamlit as st

# from langchain_groq import ChatGroq

# class GroqLLM:
#     def __init__(self, user_controls_input):
#         self.user_controls_input=user_controls_input
        
#     def get_llm_model(self):
#         try:
#             groq_api_key=self.user_controls_input["GROQ_API_KEY"]
#             selected_groq_model=self.user_controls_input["selected_groq_model"]
#             if groq_api_key=='' and os.environ["GROQ_API_KEY"]== '':
#                 st.error("Please Enter the GROQ API KEY")
                
#             llm=ChatGroq(api_key=groq_api_key, model=selected_groq_model)
            
#         except Exception as e:
#             raise ValueError(f"Error Occured With Exception : {e}")
#         return llm

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = (
                self.user_controls_input.get("GROQ_API_KEY")
                or os.getenv("GROQ_API_KEY", "")
            )

            selected_groq_model = (
                self.user_controls_input.get("selected_groq_model")
                or "llama-3.1-8b-instant"
            )

            if not groq_api_key:
                st.error("Please enter the GROQ API key")
                return None

            llm = ChatGroq(
                api_key=groq_api_key,
                model=selected_groq_model,
            )
            return llm

        except Exception as e:
            raise ValueError(f"Error occurred: {e}")