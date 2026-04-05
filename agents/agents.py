from utils.state import InterviewState
from tools.interview_tools import book_interview, cancel_interview
from utils.llm import call_llm
from utils.parser import extract_details
from tools.interview_tools import save_memory


# SUPERVISOR
def supervisor_agent(state: InterviewState):

    # 🔥 IMPORTANT FIX
    if state.get("missing_field"):
        return {**state, "intent": "schedule"}

    prompt = f"""
    Classify the intent of the user input.

    Input: "{state['user_input']}"

    Options:
    - schedule
    - cancel
    - reschedule
    - general

    Return only one word.
    """

    intent = call_llm(prompt).lower()

    if intent not in ["schedule", "cancel", "reschedule"]:
        intent = "general"

    return {**state, "intent": intent}

def schedule_agent(state: InterviewState):
    user_input = state["user_input"]


    if state.get("missing_field") == "name":
        name = user_input.strip()

        return {
            **state,
            "name": name,
            "missing_field": "time",
            "response": f"Great. When should I schedule the interview for {name}?"
        }

    if state.get("missing_field") == "time":
        name = state.get("name")
        time = user_input.strip()

        result = book_interview(name, time)
        save_memory(state["thread_id"], name, time)

        return {
            **state,
            "response": f"Done! Interview scheduled for {name} at {time}",
            "missing_field": None,
            "name": name,
            "time": time
        }


    data = extract_details(user_input)

    name = data.get("name")
    time = data.get("time")

    if not name or name == "Unknown":
        return {
            **state,
            "missing_field": "name",
            "response": "Sure! Who is the candidate?"
        }

    if not time or time == "Unknown":
        return {
            **state,
            "missing_field": "time",
            "name": name,
            "response": f"Got it. When should I schedule the interview for {name}?"
        }


    result = book_interview(name, time)
    save_memory(state["thread_id"], name, time)

    return {
        **state,
        "response": f"Great! {result}",
        "name": name,
        "time": time,
        "missing_field": None
    }

# CANCEL AGENT
def cancel_agent(state: InterviewState):
    data = extract_details(state["user_input"])

    name = data.get("name", "Unknown")

    result = cancel_interview(name)

    return {**state, "response": result}

from tools.interview_tools import reschedule_interview

from tools.interview_tools import get_memory

def reschedule_agent(state: InterviewState):
    data = extract_details(state["user_input"])

    name = data.get("name")
    time = data.get("time")

    memory = get_memory(state["thread_id"])

    if name == "Unknown" or not name:
        name = memory["name"]

    if time == "Unknown" or not time:
        time = memory["time"]

    result = reschedule_interview(name, time)

    # update memory
    save_memory(state["thread_id"], name, time)

    return {**state, "response": result}

def general_agent(state: InterviewState):
    prompt = f"""
    You are an AI assistant designed for HR recruiters.

    Your role:
    - Help recruiters manage interview scheduling
    - Speak from HR perspective (NOT candidate)
    - Be concise and professional
    - Do NOT ask about job applications or candidate intentions

    User input: "{state['user_input']}"

    Respond appropriately as an HR assistant.
    """

    reply = call_llm(prompt)

    return {**state, "response": reply}