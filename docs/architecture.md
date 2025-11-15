# Architecture

## Flow

1. User sends a natural language query (via SOAR or UI)
2. LLM interprets the query and calls SIEM query generator
3. Logs are fetched and passed back to LLM
4. LLM generates a summary using MITRE mapping

## Modules

- FastAPI: REST interface
- LLM Handler: GPT-4 interface
- SIEM Connector: Mock or live Splunk connector
- Translator: NL to SIEM DSL
