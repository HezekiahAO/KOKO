from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os
import whisper
import tempfile
import shutil

# I switched to using the Groq Python SDK for better integration and ease of use. As Ollama was giving me some space issues.
load_dotenv()

app = FastAPI()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # Connected to Groq API using the API key from env so that we can access the Groq models.

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



model_whisper = whisper.load_model("base")

# Transcription
@app.post("/transcribe")
async def transcribe(audio: UploadFile = File(...)):
    import imageio_ffmpeg
    import subprocess
    import numpy as np

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        shutil.copyfileobj(audio.file, tmp)
        tmp_path = tmp.name

    ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
    converted_path = tmp_path + "_converted.wav"

    subprocess.run([
        ffmpeg_path, "-i", tmp_path,
        "-ar", "16000", "-ac", "1", "-f", "s16le",
        converted_path
    ], check=True)

    # Load audio as numpy array and pass directly to Whisper
    audio_data = np.frombuffer(open(converted_path, "rb").read(), dtype=np.int16)
    audio_float = audio_data.astype(np.float32) / 32768.0

    result = model_whisper.transcribe(audio_float)
    return {"transcript": result["text"]}

@app.post("/process-meeting")
async def process_meeting(audio: UploadFile = File(...)):
    import imageio_ffmpeg
    import subprocess
    import numpy as np

    # Convert audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        shutil.copyfileobj(audio.file, tmp)
        tmp_path = tmp.name

    ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
    converted_path = tmp_path + "_converted.wav"

    subprocess.run([
        ffmpeg_path, "-i", tmp_path,
        "-ar", "16000", "-ac", "1", "-f", "s16le",
        converted_path
    ], check=True)

    # Transcribe
    audio_data = np.frombuffer(open(converted_path, "rb").read(), dtype=np.int16)
    audio_float = audio_data.astype(np.float32) / 32768.0
    transcript = model_whisper.transcribe(audio_float)["text"]

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