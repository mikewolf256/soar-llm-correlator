import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_events(events: list, original_prompt: str) -> str:
    prompt = f\"\"\"
    Context: {original_prompt}

    These are related logs:
    {events}

    Generate an incident summary with MITRE techniques and response recommendations.
    \"\"\"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a senior SOC analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()
