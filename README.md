<div align="center">

  <h1>Koko</h1>
  <p><strong>Your AI Workplace Assistant</strong></p>
  <p><em>"An assistant that works like an extension of you."</em></p>

  <br/>

  ![Status](https://img.shields.io/badge/Status-In%20Development-7c5cfc?style=flat-square)
  ![Hackathon](https://img.shields.io/badge/TheUdaraProject-Hackathon-a78bfa?style=flat-square)
  ![Team](https://img.shields.io/badge/Team-Neural5-0d0d1a?style=flat-square&color=7c5cfc)

</div>

<br/>

## What is Koko?

Koko is an AI-powered workplace assistant that eliminates the friction that comes after every meeting. From missed action items to delayed follow-up emails — Koko handles it all, automatically, so you can stay focused on the work that actually matters.

She doesn't just take notes. She listens, understands context, and takes action.

<br/>

## The Problem

Every professional knows this feeling:

- You finish a one-hour meeting and can't remember half of what was decided
- Your inbox piles up with follow-ups you haven't written yet
- Action items get lost because no one tracked them clearly
- You spend more time documenting work than actually doing it

Traditional note-taking tools require manual input. AI transcription tools give you walls of text. Neither solves the real problem — **turning conversations into clear, actionable outcomes, instantly.**

That's the gap Koko fills.

<br/>

## What Koko Does

**🎙️ Voice Intelligence**
Listens to your meetings and conversations in real time. Identifies key decisions, commitments, and discussion points without any manual input.

**📋 Smart Summaries**
Turns long meetings into short, structured, actionable recaps the moment your call ends.

**✉️ Email Assistant**
Drafts your follow-up emails automatically based on what was discussed. Review, tweak if needed, and send.

**✅ Action Items**
Extracts every task, deadline, and commitment from the conversation and assigns them clearly so nothing falls through the cracks.

**🔔 Smart Reminders**
Sends reminders when deadlines are approaching automatically, without you having to chase anyone.

**🤖 Agentic Capabilities (Coming Soon)**
Koko is being built to act autonomously not just generate outputs, but follow through on them. The web MVP is the foundation. The agent is the goal.

<br/>

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      USER LAYER                         │
│      Zoom / Google Meet / Microsoft Teams / WhatsApp    │
└──────────────────────────┬──────────────────────────────┘
                           │ Audio / Voice Input
                           ▼
┌─────────────────────────────────────────────────────────┐
│                  FRONTEND — HTML/CSS/JS                 │
│                                                         │
│  • WebRTC — captures microphone audio from browser      │
│  • Drag & drop audio upload                             │
│  • Displays: Transcript, Summary, Action Items, Email   │
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
│  ┌───────────────┐     │  • Deadline Reminders    │     │
│  │  Kokoro TTS   │     └─────────────────────────┘     │
│  │ Text → Speech │                                      │
│  └───────────────┘     ┌─────────────────────────┐     │
│                        │     RAG / LLMIndex       │     │
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
│  • Deadline Reminders                                   │
│  • Voice Response via Kokoro TTS (coming soon)          │
└─────────────────────────────────────────────────────────┘
```

<br/>

## Tech Stack

| Layer | Technology | Notes |
| --- | --- | --- |
| Frontend | HTML / CSS / JS | Clean UI with drag & drop audio upload |
| Audio Capture | WebRTC | Browser-based mic capture |
| Voice Detection | Silero VAD | Detects speech vs silence |
| Speech-to-Text | Whisper (base model) | Local transcription via OpenAI Whisper |
| Audio Processing | FFmpeg + imageio-ffmpeg | Converts audio to Whisper-compatible format |
| LLM Engine | Groq API (llama-3.3-70b-versatile) | Switched from Ollama due to local storage constraints |
| Memory / Context | RAG / LLMIndex | Coming soon |
| Text-to-Speech | Kokoro TTS | Coming soon |
| Backend | FastAPI | Python backend with all endpoints |
| Database | SQLite | Coming soon |
| Version Control | GitHub | With CI/CD pipeline |

<br/>

## Why Groq Instead of Ollama?

The original plan was to run Ollama locally for the LLM. During development we switched to **Groq API** for the following reasons:

- Local storage constraints made downloading Ollama models (4GB+) impractical
- Groq's free tier is fast and reliable enough for a hackathon build
- `llama-3.3-70b-versatile` on Groq outperforms smaller local models
- Zero setup — just an API key

Ollama remains an option for future self-hosted deployments.

<br/>

## API Endpoints

| Method | Endpoint | Description | Status |
| --- | --- | --- | --- |
| GET | `/health` | Server health check | ✅ Live |
| POST | `/summarize` | Transcript → meeting summary | ✅ Live |
| POST | `/transcribe` | Audio file → transcript | ✅ Live |
| POST | `/process-meeting` | Audio → transcript + summary + action items + email | ✅ Live |
| POST | `/action-items` | Transcript → task list | ✅ Live |
| POST | `/draft-email` | Transcript → follow-up email | ✅ Live |

<br/>

## Integrations

Koko works where you already work.

| Platform | Support |
| --- | --- |
| Zoom | ✅ |
| Google Meet | ✅ |
| Microsoft Teams | ✅ |
| WhatsApp | ✅ |

<br/>

## Who Is Koko For?

| User | How Koko Helps |
| --- | --- |
| Founders & Executives | Stay on top of decisions without drowning in documentation |
| Project Managers | Track every action item across every meeting automatically |
| Sales Teams | Never miss a follow-up or lose a client commitment again |
| Remote Teams | Bridge the gap between async and live collaboration |
| Freelancers & Consultants | Deliver professional recaps to clients without the extra effort |

<br/>

## Getting Started

```bash
# Clone the repo
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
```

Then open `http://127.0.0.1:8000/docs` to test the API.

<br/>

## Project Structure

```
backend/
├── main.py              ← FastAPI app (all endpoints)
├── requirements.txt     ← dependencies
├── .env                 ← API keys (never commit this)
├── .env.example         ← template for env variables
├── .gitignore
└── tests/
    └── test_main.py     ← unit tests

frontend/
├── koko.html            ← main landing page
├── koko-landing.html    ← get started / onboarding
├── koko-app.html        ← working meeting processor
└── project.html         ← original project page
```

<br/>

## Progress Log

### Week 2 — June 2026
- ✅ FastAPI backend set up and running
- ✅ Virtual environment (`KOKO`) configured
- ✅ Switched from Ollama to Groq API (`llama-3.3-70b-versatile`)
- ✅ Whisper (base) integrated for audio transcription
- ✅ FFmpeg pipeline for audio conversion
- ✅ `/summarize` endpoint live
- ✅ `/transcribe` endpoint live
- ✅ `/process-meeting` endpoint live — full pipeline working
- ✅ `/action-items` endpoint live
- ✅ `/draft-email` endpoint live
- ✅ `/health` endpoint live
- ✅ Frontend pages built and connected
- ✅ GitHub repo with `.gitignore`
- ✅ Deployment — Done(Depolyed at [KOKO](https://koko-fronted.onrender.com))
- 🔴 CI/CD pipeline — pending
- 🔴 Unit tests — pending

<br/>

## Roadmap

- [x] Core transcription engine (Whisper)
- [x] Smart summary generation (Groq)
- [x] Automated email drafting
- [x] Action item extraction
- [x] Working web MVP
- [ ] Deadline reminders & notifications
- [ ] Live deployment
- [ ] CI/CD pipeline
- [ ] Unit tests
- [ ] Zoom integration
- [ ] Google Meet integration
- [ ] Microsoft Teams integration
- [ ] WhatsApp integration
- [ ] Agentic capabilities
- [ ] Mobile app — iOS & Android
- [ ] Team collaboration dashboard
- [ ] Multi-language support

<br/>

## Current Stage

Koko is in active early development, built by team **Neural5** as part of **TheUdaraProject Hackathon**.

The web MVP is live and working at: [KOKO](https://koko-fronted.onrender.com). The goal is a fully autonomous AI agent that doesn't just generate outputs — but follows through on them.

> *"We're just getting started and we can't wait to show you what she becomes."*

<br/>

## Team

Built with purpose by **Neural5** at **TheUdaraProject Hackathon**.

<br/>

---

<div align="center">
  <strong>Koko. By Neural5.</strong><br/>
  <em>She listens. She understands. She gets things done.</em>
</div>
