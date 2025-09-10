import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str, prompt: str) -> str:
    """Generate a summary using an LLM with the given prompt."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes transcripts."},
                {"role": "user", "content": prompt + "\n\n" + text}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"<<ERROR: {e}>>"
