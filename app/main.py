from fastapi import FastAPI
from app.models import LLMQuery
from app.query_translator import translate_to_spl
from app.siem_connector import execute_spl_query
from app.llm_handler import summarize_events

app = FastAPI()

@app.post("/query")
def process_query(query: LLMQuery):
    siem_query = translate_to_spl(query)
    logs = execute_spl_query(siem_query)
    summary = summarize_events(logs, query.natural_query)
    return {"summary": summary, "events": logs}
