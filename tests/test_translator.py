from app.query_translator import translate_to_spl
from app.models import LLMQuery

def test_translate_to_spl():
    query = LLMQuery(
        incident_time="2025-10-14T03:22:00Z",
        source_ip="10.1.1.10",
        user="j.doe",
        natural_query="Check for lateral movement"
    )
    spl = translate_to_spl(query)
    assert "smb_connection" in spl
