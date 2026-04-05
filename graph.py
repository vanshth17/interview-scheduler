from langgraph.graph import StateGraph, START, END
from utils.state import InterviewState
from agents.agents import supervisor_agent, schedule_agent, cancel_agent , reschedule_agent, general_agent



# ROUTER FUNCTION

def route(state: InterviewState):
    if state.get("missing_field"):
        return "schedule"

    return state["intent"]



#GRAPH

def build_graph():
    builder = StateGraph(InterviewState)

    # Nodes
    builder.add_node("supervisor", supervisor_agent)
    builder.add_node("schedule", schedule_agent)
    builder.add_node("cancel", cancel_agent)
    builder.add_node("reschedule", reschedule_agent)
    builder.add_node("general", general_agent)

    builder.add_edge(START, "supervisor")
    builder.add_conditional_edges(
    "supervisor",
    route,
    {
        "schedule": "schedule",
        "cancel": "cancel",
        "reschedule": "reschedule", 
        "general": "general"
    }
)
    builder.add_edge("schedule", END)
    builder.add_edge("cancel", END)
    builder.add_edge("reschedule", END)
    builder.add_edge("general", END)

    return builder.compile()