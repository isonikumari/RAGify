
# RAGify

RAGify is an AI-powered meeting and video assistant. It converts YouTube videos or uploaded audio/video files into useful meeting notes and lets users ask questions about the processed content.

## Features

- Accepts YouTube URLs
- Supports uploaded audio and video files
- Converts media to WAV using FFmpeg
- Splits audio into smaller chunks
- Transcribes audio using OpenAI Whisper
- Supports English, Hindi, and other languages
- Generates:
  - Video title
  - Summary
  - Action items
  - Key decisions
  - Open questions
- Provides a question-answering chat using Retrieval-Augmented Generation (RAG)
- Uses Mistral AI and ChromaDB for answering questions

## Technologies Used

- Python
- Streamlit
- OpenAI Whisper
- Mistral AI
- LangChain
- ChromaDB
- yt-dlp
- FFmpeg
- PyTorch

## Installation

Clone the repository:

```bash
git clone https://github.com/isonikumari/RAGify.git
cd RAGify
