from graph import build_graph
from db.database import init_db


def main():
    init_db()

    graph = build_graph()

    thread_id = "user_1"

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    print("AI Interview Assistant Started (type 'exit' to quit)")

    state = {
        "user_input": "",
        "intent": "",
        "response": "",
        "thread_id": thread_id,
        "name": None,
        "time": None,
        "missing_field": None
    }

    while True:
        user_input = input("\nEnter request: ")

        if user_input.lower() == "exit":
            print("Exiting...")
            break

        state["user_input"] = user_input

        state = graph.invoke(state, config=config)

        print("Response:", state["response"])


if __name__ == "__main__":
    main()