# 🤖 Multi-Agent AI Interview Coordination System

A conversational AI system that automates interview scheduling using **LangGraph**, **Ollama (local LLM)**, and **SQLite** — built with a multi-agent architecture and real-world workflow logic.

---

# Features

* 🧠 **Multi-Agent Architecture (LangGraph)**

  * Supervisor Agent (intent routing)
  * Scheduling Agent
  * Rescheduling Agent
  * Cancellation Agent
  * General Conversation Agent

* 💬 **Conversational AI (Multi-turn)**

  * Handles incomplete inputs
  * Asks follow-up questions
  * Maintains context across turns

* 🗄️ **SQLite Persistence**

  * Stores interview schedules
  * Maintains session memory (thread-based)

* ⚙️ **Tool-Based System**

  * Availability checking
  * Interview booking
  * Rescheduling & cancellation

* 🔁 **Smart Conflict Resolution**

  * Detects double bookings
  * Suggests alternative time slots

* 🧩 **Hybrid AI + Rule-Based Routing**

  * LLM for understanding
  * Deterministic rules for reliability

---

# Architecture

```
User Input
   ↓
Supervisor Agent (Intent Detection)
   ↓
Routing (LangGraph)
   ↓
Specialized Agent
   ↓
Tool (DB Operation)
   ↓
SQLite Database
   ↓
Response to User
```

---

## 📂 Project Structure

```
.
├── agents/
│   ├── agents.py
├── tools/
│   ├── interview_tools.py
├── db/
│   ├── database.py
├── utils/
│   ├── parser.py
│   ├── state.py
├── config/
│   ├── settings.py
├── graph.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Tech Stack

* **LangGraph** – Multi-agent orchestration
* **Ollama (LLaMA3 / Mistral)** – Local LLM (no paid APIs)
* **Python** – Backend logic
* **SQLite** – Persistent storage
* **LangChain (optional)** – LLM integration utilities

---

## 🧠 How It Works

1. User sends a natural language request
2. Supervisor Agent detects intent
3. Request is routed to the correct agent
4. Agent extracts structured data (name, date, time)
5. Tool executes database operation
6. System responds conversationally

---

# Example Conversations

### ✅ Scheduling

```
User: schedule interview for Vansh at 5pm today
AI: Interview scheduled for Vansh on today at 5pm
```

---

### ❌ Conflict + Suggestions

```
User: schedule interview for Rahul at 5pm today
AI: 5pm on today is already booked. Available slots: 6pm, 7pm, 4pm. Which one works?
```

---

### 🔁 Multi-turn Flow

```
User: schedule interview
AI: Who is the candidate?

User: Vansh
AI: When should I schedule the interview for Vansh?

User: 3pm
AI: Interview scheduled for Vansh on today at 3pm
```

---

## 🔐 Environment Setup

Create a `.env` file:

```
MODEL_NAME=llama3
DB_PATH=interviews.db
ENV=development
```

---

## ▶️ Run the Project

```bash
# install dependencies
pip install -r requirements.txt

# run the app
python main.py
```

---

## 🧪 Key Engineering Concepts Demonstrated

* Multi-agent systems (LangGraph)
* LLM + deterministic system design
* State management & memory handling
* Input normalization & data consistency
* Conflict detection in scheduling systems
* Conversational AI with follow-up handling

---

## 🚧 Future Improvements

*  Real date normalization (`today → YYYY-MM-DD`)
*  FastAPI backend
*  Frontend chat interface
*  Role-based system (HR vs Candidate)
*  Dashboard for interview management

---

## 🙌 Author

Built as a hands-on project to explore **multi-agent AI systems, conversational workflows, and backend architecture**.

---

⭐ If you find this useful, consider giving it a star!
