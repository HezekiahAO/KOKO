<div align="center">
  <h1>Koko</h1>
  <p><strong>Your AI Workplace Assistant</strong></p>
  <p><em>"An assistant that works like an extension of you."</em></p>
  <br/>
Show Image
Show Image
Show Image
</div>
<br/>
What is Koko?
Koko is an AI-powered workplace assistant that eliminates the friction that comes after every meeting. From missed action items to delayed follow-up emails — Koko handles it all, automatically, so you can stay focused on the work that actually matters.
She doesn't just take notes. She listens, understands context, and takes action.
<br/>
The Problem
Every professional knows this feeling:

You finish a one-hour meeting and can't remember half of what was decided
Your inbox piles up with follow-ups you haven't written yet
Action items get lost because no one tracked them clearly
You spend more time documenting work than actually doing it

Traditional note-taking tools require manual input. AI transcription tools give you walls of text. Neither solves the real problem — turning conversations into clear, actionable outcomes, instantly.
That's the gap Koko fills.
<br/>
What Koko Does
🎙️ Voice Intelligence
Listens to your meetings and conversations in real time. Identifies key decisions, commitments, and discussion points without any manual input.
📋 Smart Summaries
Turns long meetings into short, structured, actionable recaps the moment your call ends.
✉️ Email Assistant
Drafts your follow-up emails automatically based on what was discussed. Review, tweak if needed, and send.
✅ Action Items
Extracts every task, deadline, and commitment from the conversation and assigns them clearly so nothing falls through the cracks.
🔔 Smart Reminders
Follows up on tasks before deadlines hit, keeping you and your team accountable without the back-and-forth.
<br/>
System Architecture
┌─────────────────────────────────────────────────────────┐
│                      USER LAYER                         │
│      Zoom / Google Meet / Microsoft Teams / WhatsApp    │
└──────────────────────────┬──────────────────────────────┘
                           │ Audio / Voice Input
                           ▼
┌─────────────────────────────────────────────────────────┐
│                  FRONTEND — Next.js                     │
│                                                         │
│  • WebRTC — captures microphone audio from browser      │
│  • Silero VAD — detects when user is speaking           │
│  • Displays: Summaries, Action Items, Draft Emails      │
└──────────────────────────┬──────────────────────────────┘
                           │ Audio Chunks
                           ▼
┌─────────────────────────────────────────────────────────┐
│                  BACKEND — FastAPI                      │
│                                                         │
│  ┌───────────────┐     ┌─────────────────────────┐     │
│  │ Whisper (STT) │     │     Groq LLM Engine      │     │
│  │ Audio → Text  │────▶│  • Summarization         │     │
│  └───────────────┘     │  • Action Items          │     │
│                        │  • Email Drafting        │     │
│  ┌───────────────┐     └─────────────────────────┘     │
│  │  Kokoro TTS   │                                      │
│  │ Text → Speech │     ┌─────────────────────────┐     │
│  └───────────────┘     │     RAG / LLMIndex       │     │
│                        │  Context from meetings   │     │
│                        └─────────────────────────┘     │
└──────────────────────────┬──────────────────────────────┘
                           │ Structured Output
                           ▼
┌─────────────────────────────────────────────────────────┐
│                     OUTPUT LAYER                        │
│  • Meeting Summary                                      │
│  • Action Items (with owners + deadlines)               │
│  • Draft Follow-up Email                                │
│  • Voice Response via Kokoro TTS                        │
└─────────────────────────────────────────────────────────┘
<br/>
Tech Stack
LayerTechnologyFrontendNext.jsAudio CaptureWebRTCVoice DetectionSilero VADSpeech-to-TextWhisperLLM EngineGroq API (llama-3.3-70b-versatile)Memory / ContextRAG / LLMIndexText-to-SpeechKokoro TTSBackendFastAPIDatabaseSQLiteVersion ControlGitHub
<br/>
API Endpoints
MethodEndpointDescriptionStatusGET/healthServer health check🔴 PendingPOST/summarizeTranscript → meeting summary🟢 LivePOST/action-itemsTranscript → task list🔴 PendingPOST/draft-emailTranscript → follow-up email🔴 PendingPOST/transcribeAudio file → transcript🟢 Live
<br/>
Integrations
Koko works where you already work.
PlatformSupportZoom✅Google Meet✅Microsoft Teams✅WhatsApp✅
<br/>
Who Is Koko For?
UserHow Koko HelpsFounders & ExecutivesStay on top of decisions without drowning in documentationProject ManagersTrack every action item across every meeting automaticallySales TeamsNever miss a follow-up or lose a client commitment againRemote TeamsBridge the gap between async and live collaborationFreelancers & ConsultantsDeliver professional recaps to clients without the extra effort
<br/>
Getting Started
bash# Clone the repo
git clone https://github.com/neural5/koko.git
cd koko-backend

# Create and activate virtual environment
python -m venv KOKO
KOKO\Scripts\activate        # Windows
source KOKO/bin/activate     # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Add your environment variables
cp .env.example .env
# Add your GROQ_API_KEY to .env

# Run the server
uvicorn main:app --reload
Then open http://127.0.0.1:8000/docs to test the API.
<br/>
Project Structure
koko-backend/
├── main.py              ← FastAPI app (all endpoints)
├── requirements.txt     ← dependencies
├── .env                 ← API keys (never commit this)
├── .env.example         ← template for env variables
├── .gitignore
└── tests/
    └── test_main.py     ← unit tests

koko-frontend/
├── app/
│   └── page.jsx         ← main UI
├── .env.local
└── package.json
<br/>
Progress Log
Week 2 — June 2026

✅ FastAPI backend set up and running locally
✅ Virtual environment (KOKO) configured
✅ /summarize endpoint live — powered by Groq llama-3.3-70b-versatile
✅ /transcribe endpoint live — powered by Whisper (base model)
✅ GitHub repo initialised with .gitignore
🔴 /action-items endpoint — in progress
🔴 /draft-email endpoint — in progress
🔴 Frontend — in progress
🔴 Deployment — in progress
🔴 CI/CD — in progress

<br/>
Roadmap

 Core transcription engine
 Smart summary generation
 Automated email drafting
 Action item extraction & assignment
 Frontend UI
 Live deployment
 CI/CD pipeline
 Zoom integration
 Google Meet integration
 Microsoft Teams integration
 WhatsApp integration
 Mobile app — iOS & Android
 Team collaboration dashboard
 Custom voice & tone settings per user
 Multi-language support

<br/>
Current Stage
Koko is in active early development, built by team Neural5 as part of TheUdaraProject Hackathon.

"We're just getting started — and we can't wait to show you what she becomes."

<br/>
Team
Built with purpose by Neural5 at TheUdaraProject Hackathon.
<br/>

<div align="center">
  <strong>Koko. By Neural5.</strong><br/>
  <em>She listens. She understands. She gets things done.</em>
</div>