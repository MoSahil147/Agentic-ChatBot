## It stores variables, messages, or results that later nodes use.

from typing_extensions import TypedDict, List
## TypedDict -> It gives structure to dictionaries used in type checking.
from langgraph.graph.message import add_messages
## add_messages is a helper from LangGraph that merges or appends messages inside a graph node’s state.
from typing import Annotated

class State(TypedDict):
    """
    Represent the structure of the state used in graph
    """
    
    messages: Annotated[List, add_messages]
