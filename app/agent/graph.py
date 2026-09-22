import os

from langgraph.graph import StateGraph, END

from langchain_groq import ChatGroq

from app.agent.state import AgentState


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)


def understand_request(state: AgentState):

    message = state["user_message"]

    prompt = f"""
You are a hospital appointment assistant.

Understand this patient request:

{message}

Identify:

patient name
doctor name
specialization
appointment date
appointment time

Return a simple response.
"""

    response = llm.invoke(prompt)

    state["response"] = response.content

    return state


def create_graph():

    graph = StateGraph(AgentState)

    graph.add_node(
        "understand_request",
        understand_request
    )

    graph.set_entry_point(
        "understand_request"
    )

    graph.add_edge(
        "understand_request",
        END
    )

    return graph.compile()


agent = create_graph()