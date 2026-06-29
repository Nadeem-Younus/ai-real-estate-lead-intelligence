# AI Real Estate Lead Intelligence

A multi-agent AI platform that helps real estate professionals qualify leads, recommend properties, analyze neighborhoods, and generate personalized follow-up emails.

The application is built using CrewAI, FastAPI, MCP-style services, Google Places API, Brevo Email API, Langfuse observability, and Docker.

## Features

* Lead qualification and scoring
* Property recommendation engine
* Neighborhood intelligence using Google Places
* AI-generated follow-up emails
* Human-in-the-loop email editing
* Email delivery through Brevo
* MCP-based service architecture
* Dockerized deployment
* Langfuse observability integration

## Architecture

User → Streamlit UI → CrewAI Agents

Agents:

* Lead Agent
* Property Agent
* Market Agent
* Follow-up Agent

External Services:

* Google Places API
* Brevo Email API

MCP Servers:

* Maps MCP Server
* Brevo MCP Server

## Tech Stack

* Python 3.11
* CrewAI
* OpenAI GPT-4o-mini
* Streamlit
* FastAPI
* Docker
* Langfuse
* Google Maps API
* Brevo API

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd ai-real-estate-lead-intelligence
```

Create environment variables:

```bash
cp .env.example .env
```

Update the values in `.env`.

Install dependencies:

```bash
pip install -r requirements.txt
```

Run with Docker:

```bash
docker compose build --no-cache
docker compose up
```

Application URLs:

* Streamlit UI: http://localhost:8501
* Maps MCP: http://localhost:9000/docs
* Brevo MCP: http://localhost:9001/docs

## Project Workflow

1. User submits lead requirements.
2. Lead Agent evaluates lead quality.
3. Property Agent recommends matching properties.
4. Market Agent retrieves neighborhood intelligence.
5. Follow-up Agent generates personalized email.
6. User reviews and edits email.
7. Brevo MCP Server sends the email.

## Future Enhancements

* CRM integration
* Property database integration
* User authentication
* Cloud deployment
* Advanced Langfuse tracing

## Author

Muhammad Nadeem Younus
