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
Follows up on tasks before deadlines hit, keeping you and your team accountable without the back-and-forth.

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
```

<br/>

## Tech Stack

| Layer | Technology |
| --- | --- |
| Frontend | Next.js |
| Audio Capture | WebRTC |
| Voice Detection | Silero VAD |
| Speech-to-Text | Whisper |
| LLM Engine | Groq API |
| Memory / Context | RAG / LLMIndex |
| Text-to-Speech | Kokoro TTS |
| Backend | FastAPI |
| Database | SQLite |
| Version Control | GitHub |

<br/>

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/health` | Server health check |
| POST | `/summarize` | Transcript → meeting summary |
| POST | `/action-items` | Transcript → task list |
| POST | `/draft-email` | Transcript → follow-up email |
| POST | `/transcribe` | Audio file → transcript |

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
```

<br/>

## Roadmap

- [ ] Core meeting listener & transcription engine
- [ ] Smart summary generation
- [ ] Automated email drafting
- [ ] Action item extraction & assignment
- [ ] Zoom integration
- [ ] Google Meet integration
- [ ] Microsoft Teams integration
- [ ] WhatsApp integration
- [ ] Mobile app — iOS & Android
- [ ] Team collaboration dashboard
- [ ] Custom voice & tone settings per user
- [ ] Multi-language support

<br/>

## Current Stage

Koko is in active early development, built by team **Neural5** as part of **TheUdaraProject Hackathon**.

> *"We're just getting started — and we can't wait to show you what she becomes."*

<br/>

## Team

Built with purpose by **Neural5** at **TheUdaraProject Hackathon**.

<br/>

---

<div align="center">
  <strong>Koko. By Neural5.</strong><br/>
  <em>She listens. She understands. She gets things done.</em>
</div>
