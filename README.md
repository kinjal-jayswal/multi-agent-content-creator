# ✍️ Multi-Agent Content Creator — JK Data Lab

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-0.2+-1C3C3C?style=flat)](https://langchain.com)
[![Ollama](https://img.shields.io/badge/Ollama-llama3%20%7C%20mistral-black?style=flat)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)
[![Author](https://img.shields.io/badge/Author-JK%20Data%20Lab-00FFD4?style=flat)](https://www.jkdatalab.com)

> Four specialized AI agents — Researcher, Writer, Editor, and SEO Expert — collaborate in a pipeline to research, draft, refine, and optimize content on any topic.

---

## What It Does

- **Researcher agent** gathers market data, trends, and key statistics for the requested topic
- **Writer agent** produces a structured article (blog post, LinkedIn article, email newsletter, product description, or technical doc)
- **Editor agent** polishes the draft — tightening prose, improving word choice, and enforcing consistent style
- **SEO Expert agent** analyzes keyword density, readability, and generates title tags and meta descriptions
- **Demo Mode** lets you run the full pipeline without an Ollama backend — ideal for quick evaluation

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Streamlit UI (app.py)                  │
│  ┌──────────┐  ┌────────┐  ┌────────┐  ┌────────────┐  │
│  │Researcher│→ │ Writer │→ │ Editor │→ │ SEO Expert │  │
│  └──────────┘  └────────┘  └────────┘  └────────────┘  │
│          ↓ (tabs: Research / Draft / Edited / SEO / Final)│
└─────────────────────────────────────────────────────────┘
                         ↑
              Sidebar: model, tone, content type,
                       word count, Ollama host
                         ↑
              Ollama (llama3 / mistral) — optional
              LangChain orchestration layer
```

---

## Quick Start

### 1. Clone & install

```bash
git clone <repo-url>
cd 06_multi_agent_content_creator

# Create and activate virtual environment
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Run

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| **Demo Mode** | `True` | Run without Ollama — uses built-in simulated responses |
| **Ollama Host** | `localhost` | Hostname of your Ollama server |
| **Model** | `llama3` | LLM model served by Ollama (`llama3` or `mistral`) |
| **Content Type** | `Blog Post` | Output format for the Writer agent |
| **Tone** | `Professional` | Writing style applied by the Writer and Editor agents |
| **Word Count** | `800` | Target length slider (300–2000 words) |

### Optional: Ollama LAN Setup

```bash
ollama pull llama3
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

Set **Ollama Host** in the sidebar to your server's LAN IP to connect remotely.

---

## Project Structure

```
06_multi_agent_content_creator/
├── app.py              # Main Streamlit app — all four agents defined here
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── venv/               # Virtual environment (not committed)
```

---

## Requirements

| Package | Version | Purpose |
|---------|---------|---------|
| `streamlit` | ≥1.35.0 | Web UI and multi-tab output rendering |
| `requests` | ≥2.31.0 | HTTP calls to Ollama API |
| `langchain` | ≥0.2.0 | Agent orchestration framework |
| `langchain-community` | ≥0.2.0 | Ollama integration for LangChain |
| `python-dotenv` | ≥1.0.0 | Environment variable management |

---

## Module Series

This project is **module 06** in the JK Data Lab Agentic AI series:

| # | Module |
|---|--------|
| 01 | Single-Agent Basics |
| 02 | Tool-Using Agents |
| 03 | Memory & State |
| 04 | RAG Pipeline |
| 05 | Agent-to-Agent Communication |
| **06** | **Multi-Agent Content Creator** ← you are here |

---

## License

MIT © [Kinjal Jayswal — JK Data Lab](https://www.jkdatalab.com)

---

<div align="center">
  Built with ❤️ by <strong><a href="https://www.jkdatalab.com">JK Data Lab</a></strong><br>
  📧 kinjal@jkdatalab.com &nbsp;|&nbsp; 🌐 www.jkdatalab.com
</div>
