# 🛡️ soar-llm-correlator

> 🔍 An LLM-powered incident summarizer and event correlator for SIEMs and SOAR platforms — now with native support for **TheHive**!

---

## 🚨 What It Does

This microservice uses **OpenAI's GPT-4** (or any LLM) to:

- Accept **natural language** incident queries from analysts or SOAR automation
- Translate them into **SIEM DSL queries** (Splunk, Elastic, etc.)
- Retrieve and correlate events (lateral movement, privilege escalation, etc.)
- Generate detailed, MITRE-tagged summaries for each incident

---

## ⚙️ Tech Stack

| Component     | Tech                          |
|---------------|-------------------------------|
| API           | FastAPI                       |
| LLM           | OpenAI GPT-4                  |
| Query Engine  | Splunk (SPL) (mocked for now) |
| Summarizer    | GPT + MITRE Mapping           |
| Integration   | Supports **TheHive** SOAR     |

---

## 🧠 TheHive Integration

TheHive supports **custom responders** and **playbook tasks** via Cortex. You can integrate `soar-llm-correlator` using:

### 🔁 1. HTTP Responder (via Cortex)

Use Cortex to define a responder that sends a POST request to:


POST http://<llm-service-host>:8000/query
With payload:

```json
{
  "incident_time": "{{case.createdAt}}",
  "source_ip": "{{observable.data}}",
  "user": "{{case.owner}}",
  "natural_query": "Summarize this incident and identify lateral movement or privilege escalation"
}

📥 2. From TheHive Observable

You can trigger this on any observable (like an IP or username). When executed:

    Cortex sends the request to this LLM microservice

    LLM summarizes all events around that indicator

    You get a structured summary back in the TheHive case timeline

🧩 Example Summary Output (in TheHive)

    🎯 Incident Summary
    On October 14, 2025, the host 10.1.1.10 (user j.doe) executed svchost.exe via process injection. Within the hour, SMB connections were established to 10.1.1.15, and LSASS memory dump activity was detected — indicating lateral movement and credential access.

MITRE Techniques

    T1055 – Process Injection

    T1021.002 – SMB

    T1003.001 – LSASS Dump

✅ Host should be isolated and credentials rotated.
📡 Running the Service

uvicorn app.main:app --reload

🔌 API: /query
📥 Input

{
  "incident_time": "2025-10-14T03:22:00Z",
  "source_ip": "10.1.1.10",
  "user": "j.doe",
  "natural_query": "Find signs of lateral movement in the hour after this event"
}

📤 Output

{
  "summary": "On October 14, host 10.1.1.10 showed...",
  "events": [ {...}, {...} ]
}

📂 File Structure

soar-llm-correlator/
├── app/
│   ├── main.py              # FastAPI app
│   ├── config.py
│   ├── models.py            # Pydantic models
│   ├── query_translator.py  # NL → SIEM query
│   ├── siem_connector.py    # Mock Splunk query
│   ├── llm_handler.py       # GPT call logic
├── data/
│   └── example_events.json
├── tests/
│   └── test_translator.py
├── docs/
│   └── architecture.md
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md

🧪 Local Testing

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest

📈 Roadmap

OpenAI LLM summarization

SIEM DSL translation (Splunk)

Mock data correlation

MITRE technique tagging

Integration with TheHive/Cortex

Elastic + Sentinel backends

Dockerfile + GitHub Actions

    RAG with threat intelligence feeds

🧠 Use Cases
Role	How You Benefit
SOC Analyst	Rapid triage of large incident volumes
IR Lead	Clear MITRE-based summaries
CISO	Executive-level reporting on incident root cause
Engineer	Understand impact and scope fast
🛡️ License

MIT — Use freely. Attribute when in doubt.
🤝 Contributing

PRs welcome! Fork it, make magic, submit a PR.
🔥 Maintainer

Built by defenders who got tired of reading 400 log lines per alert.

    Questions or feature requests?
    Create an Issue


---

## ✅ What to Do Next

1. Replace the placeholder GitHub username (`YOURUSERNAME`) in the README.
2. Commit the updated `README.md`:

```bash
git add README.md
git commit -m "Update README with TheHive integration info"
git push

    In TheHive/Cortex:

        Create a new responder

        Point it to your /query endpoint

        Map TheHive variables (case.owner, observable.data, etc.) to the API fields
