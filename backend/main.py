from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os       
import tempfile
import shutil
from dotenv import load_dotenv
load_dotenv()


# I switched to using the Groq Python SDK for better integration and ease of use. As Ollama was giving me some space issues.
load_dotenv()

app = FastAPI()
client: Groq = None  # type: ignore

@app.on_event("startup")
async def startup_event():
    global client
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))     # This way the Groq client only gets created after the app starts and environment variables are already loaded.




class Meeting(BaseModel):           # Created a Class to represent the meeting data structure, which includes a transcript field to hold the meeting transcript that we want to summarize.
    transcript: str                # Data type of the transcript

@app.post("/summarize")             #decorator to define a POST endpoint at /summarize, which will receive meeting data and return a summary.
def summarize(meeting: Meeting):
    response = client.chat.completions.create(      # passes to Groq to process the meeting transcript and generate a summary. The model used is "llama3-8b-8192", which is a powerful language model suitable for summarization tasks. The messages parameter includes a system message to set the context for the assistant and a user message containing the meeting transcript to be summarized.
        model= "llama-3.3-70b-versatile",
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


@app.post("/transcribe")                    # defines a POST endpoint at /transcribe, which will receive
async def transcribe(audio: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        shutil.copyfileobj(audio.file, tmp)
        tmp_path = tmp.name

    with open(tmp_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3",
        )

    os.remove(tmp_path)
    return {"transcript": transcription.text}

@app.post("/process-meeting")                   # defines a POST endpoint at /process-meeting, which will receive an audio file
async def process_meeting(audio: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        shutil.copyfileobj(audio.file, tmp)
        tmp_path = tmp.name

    with open(tmp_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3",
        )
    
    transcript = transcription.text
    os.remove(tmp_path)

    # Analyse with Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are Koko, an AI workplace assistant. 
                Given a meeting transcript, return ONLY a valid JSON object with exactly these three fields:
                {
                  "summary": "a clear summary of the meeting",
                  "action_items": ["item 1", "item 2", "item 3"],
                  "draft_email": "a professional follow-up email"
                }
                Return nothing else. No explanation. Just the JSON."""
            },
            {
                "role": "user",
                "content": f"Process this meeting transcript:\n{transcript}"
            }
        ]
    )

    return {
        "transcript": transcript,
        "analysis": response.choices[0].message.content
    }


@app.post("/draft-email")
def draft_email(meeting: Meeting):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are Koko, an AI workplace assistant. Draft a professional follow-up email based on the meeting transcript. Include subject line, body, and sign off."
            },
            {
                "role": "user",
                "content": f"Draft a follow-up email for this meeting:\n{meeting.transcript}"
            }
        ]
    )
    return {"draft_email": response.choices[0].message.content}