## Each node does one task, like calling an LLM, fetching data, or routing output.
from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot login implementation
    """
    def __init__(self, model):
        self.llm=model
        
    def process(self, state:State) -> dict:
        """
        Process the input state and generates a chatbot response.
        """
        return {"messages":self.llm.invoke(state['messages'])}