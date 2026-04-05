from db.database import get_connection



# BOOK INTERVIEW
def book_interview(name: str, time: str):
    if not is_time_available(time):
        return f"Time slot {time} is already booked. Please choose another time."

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO interviews (name, time, status) VALUES (?, ?, ?)",
        (name, time, "scheduled")
    )

    conn.commit()
    conn.close()

    return f"Interview scheduled for {name} at {time}"



# CANCEL INTERVIEW
def cancel_interview(name: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE interviews SET status='cancelled' WHERE name=?",
        (name,)
    )

    conn.commit()
    conn.close()

    return f"Interview cancelled for {name}"

def is_time_available(time: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM interviews WHERE time=? AND status='scheduled'",
        (time,)
    )

    result = cursor.fetchone()
    conn.close()

    return result is None

def reschedule_interview(name: str, new_time: str):
    if not is_time_available(new_time):
        return f"Time slot {new_time} is not available."

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE interviews SET time=? WHERE name=? AND status='scheduled'",
        (new_time, name)
    )

    conn.commit()
    conn.close()

    return f"Interview rescheduled for {name} to {new_time}"

def save_memory(thread_id: str, name: str, time: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO memory (thread_id, name, time)
    VALUES (?, ?, ?)
    ON CONFLICT(thread_id)
    DO UPDATE SET name=excluded.name, time=excluded.time
    """, (thread_id, name, time))

    conn.commit()
    conn.close()

def get_memory(thread_id: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, time FROM memory WHERE thread_id=?",
        (thread_id,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return {"name": result[0], "time": result[1]}

    return {"name": None, "time": None}