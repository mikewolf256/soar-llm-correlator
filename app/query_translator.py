from app.models import LLMQuery

def translate_to_spl(query: LLMQuery) -> str:
    return f\"\"\"
        search index=main 
        (event_type="smb_connection" OR event_type="rdp_login")
        src_ip="{query.source_ip}"
        earliest="{query.incident_time}-1h"
        latest="{query.incident_time}+1h"
        | table _time, event_type, user, src_ip, dst_ip, message
    \"\"\"
