import json
from utils.llm import call_llm


def extract_details(user_input: str) -> dict:
    prompt = f"""
    Extract interview details from the input.

    Input: "{user_input}"

    Rules:
    - Return ONLY valid JSON
    - No explanation, no extra text
    - If value not found, use "Unknown"

    Format:
    {{
        "name": "...",
        "time": "..."
    }}
    """

    response = call_llm(prompt)

    response = response.strip()

    if "{" in response:
        response = response[response.index("{"):]

    if "}" in response:
        response = response[:response.rindex("}") + 1]

    try:
        data = json.loads(response)
        return data
    except Exception as e:
        print("Parsing Error:", response) 
        return {
    "name": data.get("name"),
    "time": data.get("time")
}