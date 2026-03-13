# 🚀 Lumina RAG Engine

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![RAG](https://img.shields.io/badge/AI-Advanced--RAG-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**Lumina RAG Engine** is a production-grade, modular Retrieval-Augmented Generation (RAG) system designed for enterprise-scale knowledge management. It features a sophisticated hybrid search architecture, intelligent re-ranking using Cross-Encoders, and native citation support to ensure high precision and grounded AI responses.

---

## 🌟 Key Features

- **Hybrid Search Architecture**: Combines semantic vector search (ChromaDB/FAISS) with keyword-based retrieval (BM25) for maximum recall.
- **Intelligent Re-ranking**: Integrates SOTA Cross-Encoders to re-rank retrieved documents based on query relevance.
- **Citation Awareness**: Every generated response includes precise references to source documents and page numbers.
- **Scalable Document Ingestion**: Asynchronous pipeline for processing PDFs, TXT, and Markdown files with intelligent chunking.
- **Modular LLM Backend**: Plug-and-play support for OpenAI (GPT-4), Anthropic (Claude 3), and Local Models (vLLM/Ollama).

## 🏗️ System Architecture

`mermaid
graph TD
    Query[User Query] --> Ingest[Query Ingestion]
    Ingest --> HybridSearch{Hybrid Search}
    HybridSearch --> Vector[Vector Store]
    HybridSearch --> Keyword[BM25 Index]
    Vector --> Candidates[Raw Candidates]
    Keyword --> Candidates
    Candidates --> ReRanker[Cross-Encoder Re-ranker]
    ReRanker --> Context[Top Contexts]
    Context --> LLM[LLM Generator]
    LLM --> Response[Response + Citations]
`

## 🛠️ Tech Stack

- **Core**: Python 3.10, FastAPI, Pydantic.
- **AI/ML**: PyTorch, Sentence-Transformers, OpenAI API.
- **Vector DB**: ChromaDB / FAISS.
- **UI**: Streamlit.
- **Infra**: Docker, Azure AKS Ready.

## 📂 Project Structure

\\\
lumina-rag-engine/
├── src/
│   ├── engine/              # RAG pipeline and retrieval logic
│   ├── api/                 # FastAPI backend for query processing
│   └── ingestion/           # Document processing and embedding
├── ui/                      # Streamlit dashboard for interaction
├── Dockerfile               # Container definition
├── requirements.txt         # Dependencies
└── README.md
\\\

## 🚀 Quick Start

1. **Clone the repository**
   \\\ash
   git clone https://github.com/snapple-w/lumina-rag-engine.git
   cd lumina-rag-engine
   \\\

2. **Run with Docker**
   \\\ash
   docker build -t lumina-rag .
   docker run -p 8501:8501 lumina-rag
   \\\

## 👨‍💻 Author

**Hitesh Malhotra**
*Senior Software Engineer | AI Systems Architect*
[LinkedIn](https://www.linkedin.com/in/hiteshmalhotra/)

---
*Building grounded and reliable AI systems for the enterprise.*