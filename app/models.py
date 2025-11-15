from pydantic import BaseModel
from typing import List

class LLMQuery(BaseModel):
    incident_time: str
    source_ip: str
    user: str
    natural_query: str

class SIEMEvent(BaseModel):
    timestamp: str
    event_type: str
    src_ip: str
    dst_ip: str
    user: str
    message: str
