from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os
# I switched to using the Groq Python SDK for better integration and ease of use. As Ollama was giving me some space issues.
load_dotenv()

app = FastAPI()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # Connected to Groq API using the API key from env so that we can access the Groq models.

class Meeting(BaseModel):           # Created a Class to represent the meeting data structure, which includes a transcript field to hold the meeting transcript that we want to summarize.
    transcript: str                # Data type of the transcript

@app.post("/summarize")             #decorator to define a POST endpoint at /summarize, which will receive meeting data and return a summary.
def summarize(meeting: Meeting):
    response = client.chat.completions.create(      # passes to Groq to process the meeting transcript and generate a summary. The model used is "llama3-8b-8192", which is a powerful language model suitable for summarization tasks. The messages parameter includes a system message to set the context for the assistant and a user message containing the meeting transcript to be summarized.
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are Koko, an AI workplace assistant. Summarize meetings clearly and extract action items."
            },
            {
                "role": "user",
                "content": f"Summarize this meeting transcript:\n{meeting.transcript}"
            }
        ]
    )                                                # passes to Groq to process the meeting transcript and generate a summary. The model used is "llama3-8b-8192", which is a powerful language model suitable for summarization tasks. The messages parameter includes a system message to set the context for the assistant and a user message containing the meeting transcript to be summarized.
     
    return {"summary": response.choices[0].message.content} # returns the generated summary as a JSON response, where the summary is extracted from the first choice in the response from Groq.