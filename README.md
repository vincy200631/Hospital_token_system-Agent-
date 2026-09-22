# 🏥 Hospital Token System — Agentic AI

An **Agentic AI-based Hospital Token Management System** that helps manage doctors, appointments, and patient tokens using natural-language requests.

The project combines **FastAPI, LangGraph, Groq LLM, PostgreSQL, and SQLAlchemy** to build an AI-powered hospital backend.

---

## 🚀 Project Overview

Traditional hospital token systems require patients to manually select doctors, appointment dates, and times.

This project aims to provide an AI-assisted workflow where a patient can communicate naturally with the system.

For example:

> "I need to book an appointment with a dermatologist tomorrow."

The AI agent can understand the request and use backend tools to perform hospital operations.

### Planned Agent Workflow

```text
Patient
   ↓
Natural Language Request
   ↓
FastAPI
   ↓
LangGraph Agent
   ↓
Groq LLM
   ↓
Agent decides which tool to use
   ↓
┌──────────────────────────────┐
│ Doctor Search                │
│ Availability Check           │
│ Token Booking                │
│ Token Status                 │
│ Token Cancellation           │
└──────────────────────────────┘
   ↓
PostgreSQL
   ↓
Agent Response
