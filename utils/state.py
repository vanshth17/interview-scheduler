from typing import TypedDict, Optional

class InterviewState(TypedDict):
    user_input: str
    intent: str
    response: str
    thread_id: str
    name: Optional[str]
    time: Optional[str]
    missing_field: Optional[str]  