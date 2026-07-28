# ⚡ AgentPulse-Groq

> Autonomous Multi-Agent AI Suite powered by **Agno Framework** and ultra-fast **Groq LLM (Llama 3.3)**.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Agno](https://img.shields.io/badge/Framework-Agno-FF6F61?style=for-the-badge)
![Groq](https://img.shields.io/badge/Inference-Groq_Llama_3.3-F05032?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

---

## 🖼️ Application UI Preview

<img width="1917" height="1018" alt="Screenshot 2026-07-28 144516" src="https://github.com/user-attachments/assets/f6658814-f558-411f-84af-5e6f5581bc74" />

<img width="1853" height="760" alt="Screenshot 2026-07-28 144534" src="https://github.com/user-attachments/assets/4cd84855-74ce-4498-8b67-c117ace67359" />


---

## 🌟 Features & Agents

| Agent Name | Description | Key Tools / DB |
| :--- | :--- | :--- |
| **🎥 YouTube Video Analyzer** | Extracts video metadata, key learnings, and creates structured timestamps with a Streamlit UI. | `YouTubeTools`, Streamlit |
| **📈 Finance Agent** | Researches real-time stock fundamentals, market recommendations, and financial metrics. | `YFinanceTools`, `DuckDuckGoTools` |
| **🌐 Travel Agent** | Performs real-time travel safety analysis and web searches. | `DuckDuckGoTools` |
| **🧠 Memory Agent** | Retains long-term user context across sessions using SQLite database. | `SqliteDb` |
| **🗣️ Translation Team** | Multi-agent team collaborating to answer queries simultaneously in English, Hindi, and Chinese. | `Agno Team Orchestrator` |

---

## 🏗️ Project Structure

```text
AgentPulse-Groq/
├── agents/
│   ├── travel_agent.py      # Real-time Travel & Web Search Agent
│   ├── finance_agent.py     # Stock & Market Research Agent
│   ├── memory_agent.py      # SQLite Persistent Memory Agent
│   ├── team_agent.py        # Multi-Lingual Translation Team
│   └── youtube_agent.py     # YouTube Video Analyzer Engine
├── ui.py                    # Streamlit Web Dashboard
├── .env                     # Environment Variables (Ignored in Git)
├── .gitignore               # Ignored files configuration
├── requirements.txt         # Project Dependencies
└── README.md                # Documentation
