from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()

class Meeting(BaseModel):
    transcript: str

@app.post("/summarize")
def summarize(meeting: Meeting):
    response = ollama.chat(model="llama3", messages=[
        {"role": "user", "content": f"Summarize this meeting:\n{meeting.transcript}"}
    ])
    return {"summary": response['message']['content']}