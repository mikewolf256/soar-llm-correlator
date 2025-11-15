# 🛡️ soar-llm-correlator

LLM-enhanced SOAR component to summarize incidents and correlate events across alert types via SIEM.

## 🚀 Features

- Translate NL queries to Splunk DSL
- Correlate alerts based on time, user, IP
- Summarize with GPT-4
- MITRE ATT&CK mapping
- FastAPI REST interface

## 📦 Install

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🧠 Example Query

```bash
POST /query
{
  "incident_time": "2025-10-14T03:22:00Z",
  "source_ip": "10.1.1.10",
  "user": "j.doe",
  "natural_query": "Find lateral movement attempts within 1 hour"
}
```

## 📈 Output

- MITRE-mapped summary
- Raw correlated events
