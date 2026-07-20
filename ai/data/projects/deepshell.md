---
id: project_deepshell

title: DeepShell

type: project

status: In Progress

priority: 100

visibility: public

category: AI Application

repository: portfolio-os

skills:
  - Python
  - FastAPI
  - LangGraph
  - Textual
  - RAG
  - ChromaDB
  - REST API
  - System Design
  - Agentic AI

last_updated: 2026-07-19
---

# Overview

DeepShell is an AI-powered terminal portfolio that combines a modern Textual user interface with an AI digital twin named DeepDev.

Unlike a traditional portfolio website, DeepShell allows visitors to interact with an AI assistant capable of answering questions about projects, professional experience, technical skills, publications, and career journey using Retrieval-Augmented Generation (RAG).

The project is designed with a modular architecture so that the same AI backend can power multiple interfaces, including a terminal application, a future web portfolio, and other clients.

---

# Motivation

Traditional portfolios are static and only present information.

The goal of DeepShell is to transform a portfolio into an interactive knowledge system where recruiters and engineers can explore projects conversationally.

Rather than reading bullet points on a resume, users can ask questions such as:

- Which AI technologies have you worked with?
- Why did you build this project?

The AI retrieves relevant knowledge and generates grounded responses instead of relying on generic summaries.

---

# Objectives

The primary objectives of DeepShell are:

- Build an AI-powered interactive portfolio.
- Learn production-ready AI engineering practices.
- Demonstrate LangGraph-based agent orchestration.
- Implement Retrieval-Augmented Generation.
- Create reusable backend services for multiple frontends.
- Showcase software architecture and system design skills.

---

# Architecture

The project is divided into independent modules.

## Terminal Interface

Built using the Textual framework.

Responsibilities:

- Navigation
- User interaction
- Terminal rendering
- API communication

The terminal application contains no AI logic.

---

## AI Backend

Built using FastAPI.

Responsibilities:

- Receive requests
- Execute LangGraph workflows
- Retrieve relevant knowledge
- Generate responses
- Return structured JSON

The backend is independent of the user interface.

---

## Knowledge Base

Knowledge is stored as structured Markdown documents.

Categories include:

- Projects
- Experience
- Skills
- Publications
- Education
- Certifications

Each document contains metadata and detailed engineering context.

---

## Retrieval Pipeline

Planned pipeline:

User Question

↓

Intent Routing

↓

Knowledge Selection

↓

Vector Search

↓

Context Building

↓

LLM Response

---

# Technologies

Programming

- Python

Frameworks

- FastAPI
- Textual
- LangGraph

AI

- Retrieval-Augmented Generation
- Large Language Models
- Agentic AI

Database

- ChromaDB (planned)

Models

- Groq-hosted LLMs

---

# Design Principles

DeepShell follows several engineering principles:

- Separation of concerns
- Modular architecture
- API-first development
- Reusability
- Scalability
- Maintainability
- Production-oriented design

The terminal application, AI backend, and future web application are intentionally independent components.

---

# Challenges

Major engineering challenges include:

- Designing a reusable AI backend.
- Creating a structured knowledge base.
- Building an extensible LangGraph workflow.
- Maintaining grounded AI responses.
- Designing scalable project architecture.
- Supporting multiple user interfaces.

---

# Future Roadmap

Planned features include:

- Metadata-aware RAG
- Multi-agent workflows
- Conversation memory
- GitHub integration
- Portfolio website using the same backend
- Streaming responses
- Source citations
- SSH-accessible DeepShell
- Voice interaction
- Tool calling
- Docker deployment

---

# Key Learnings

This project is strengthening understanding of:

- AI application architecture
- LangGraph orchestration
- Retrieval-Augmented Generation
- FastAPI backend development
- System design
- Modular software engineering
- Building production-ready AI applications