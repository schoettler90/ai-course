# Course Pensum: AI Agents — From Zero to Builder

A ~20-hour beginner-friendly course on AI and AI Agents, structured in 10 classes of approximately 2 hours each.
Each class contains multiple lessons with concept explanations, real-world case studies, guided hands-on exercises, independent challenges, and quizzes.

---

## Course Map at a Glance

| Class | # | Lesson | Hours | Module | Tools / Frameworks |
|-------|---|--------|-------|--------|---------------------|
| 1 | 01 | Welcome: AI in the Real World | 1h | Foundations | Claude Code (demo) |
| 1 | 02 | A Brief History of AI | 1h | Foundations | — |
| 2 | 03 | How LLMs Work | 2h | Foundations | ChatGPT, Claude.ai, Gemini |
| 3 | 04 | Using LLM APIs and Structured Outputs | 1h | LLMs in Code | Anthropic SDK, OpenAI SDK |
| 3 | 05 | Tools & MCP | 1h | LLMs in Code | Anthropic SDK, JSON, MCP |
| 4 | 06 | RAG: Concepts & Implementation | 2h | RAG | LangChain, Chroma |
| 5 | 07 | Claude Code: Agent Architecture and Design | 2h | Agents & Code | Claude Code |
| 6 | 08 | Antigravity: Build a Simple Application | 2h | Code Agents | Antigravity |
| 7 | 09 | Claude Cowork: Document and Data Analysis | 2h | Code Agents | Claude Cowork |
| 8 | 10 | OpenClaw: Local AI and Personal Agents | 2h | Local AI | OpenClaw, Ollama |
| 9 | 11 | OpenClaw: Build a Marketing Agent | 2h | Local AI | OpenClaw |
| 10 | 12 | No-Code Agents with N8N | 2h | Advanced | N8N |

---

## Class 1 — Foundations (2 hours)

### Lesson 01 — Welcome: AI in the Real World
**Theme:** Who is this course for, and why does it matter now?

**Topics:**
- Introduction: instructor background, motivation for the course
- What is AI? What is an AI agent? (intuitive definitions, no jargon)
- Real-world use cases: AI in daily life, business, science, and creativity
- Live demo: Claude Code as a state-of-the-art agent in action
- Overview of the course journey ahead

**Key glossary terms:** AI, Agent, LLM, Claude Code

---

### Lesson 02 — A Brief History of AI
**Theme:** How did we get here? From perceptrons to agents.

**Topics:**
- Early AI and rule-based systems (1950s–1980s)
- Machine Learning: teaching computers from data
- Neural networks and the rise of deep learning
- GPUs: the hardware that changed everything
- AlexNet and the ImageNet moment (2012)
- Convolutional Neural Networks (CNNs) and computer vision
- The Transformer architecture: *"Attention Is All You Need"* (2017)
- Scaling Laws: bigger is better (up to a point)
- GPT-2, GPT-3, GPT-4 and the LLM revolution
- Where we are today: foundation models and AI agents

**Key glossary terms:** Machine Learning, Neural Network, Deep Learning, GPU, AlexNet, CNN, Transformer, Scaling Laws, GPT, Foundation Model

---

## Class 2 — LLMs, Prompt Engineering & Multimodal AI (2 hours)

### Lesson 03 — How LLMs Work
**Theme:** Understand how large language models work and start using the leading AI tools.

**Topics:**
- Tokens: how text becomes numbers
- The context window: what the model can "see"
- Pre-training vs. fine-tuning vs. RLHF
- Why models hallucinate — and what to do about it
- System prompts and how they shape behavior
- Tour of ChatGPT, Claude.ai, and Gemini
- Multimodal AI: moving beyond text (images, audio, and documents)
- **Exercise:** Solve the same three tasks across all three tools and compare results

**Key glossary terms:** Token, Context Window, Fine-tuning, RLHF, Hallucination, System Prompt, ChatGPT, Claude, Gemini, Multimodal

---

## Class 3 — LLM APIs, Structured Outputs & Tools (2 hours)

### Lesson 04 — Using LLM APIs and Structured Outputs
**Theme:** Going beyond the chat interface — talking to models in code and getting reliable output.

**Topics:**
- What is an API and why use it programmatically?
- Getting API keys: OpenAI, Anthropic, Google
- Making your first API call in Python
- Request structure: messages, roles, model selection
- Handling responses and errors
- Cost awareness: tokens, pricing, rate limits
- Why unstructured text output is hard to use in code
- Structured outputs: asking models to respond in JSON
- Parsing and validating structured responses
- **Exercise:** Build a Python script that queries the Claude API and returns structured JSON data

**Key glossary terms:** API, Token, LLM, Client, Structured Output, JSON

---

### Lesson 05 — Tools & MCP
**Theme:** Giving LLMs the ability to act — and connecting them to everything.

**Topics:**
- Tool calling (function calling): giving models the ability to act
- Defining tools: name, description, parameters
- Parsing and using tool call results
- The problem before MCP: every tool integration was one-off and fragile
- What is MCP (Model Context Protocol)? Hosts, clients, and servers explained
- How MCP standardizes tool connections across agents and models
- Built-in MCP servers: filesystem, web search, databases, GitHub, Slack
- Using MCP with Claude Code: configuration and practical use
- MCP vs. raw tool calling: when to use each
- **Exercise:** Build a tool-calling agent, then configure Claude Code with MCP servers to do the same task with less code
- **Challenge:** Build and register a simple custom MCP server

**Key glossary terms:** Tool Calling, Tool, API, MCP

---

## Class 4 — Retrieval-Augmented Generation (2 hours)

### Lesson 06 — RAG: Concepts & Implementation
**Theme:** Ground AI in your own data — understand it, then build it.

**Topics:**
- The problem: LLMs have a knowledge cutoff and can hallucinate facts
- What is RAG? The retrieve-then-generate pipeline
- Embeddings: turning text into vectors
- Semantic similarity: finding relevant chunks by meaning, not keywords
- Vector databases: Chroma, Pinecone, Weaviate
- Chunking strategies: how to split documents effectively
- Introduction to LangChain: why use a framework?
- Loading and chunking documents in LangChain
- Creating embeddings and storing them in a vector database
- Assembling the RAG chain: retriever + LLM
- **Exercise:** Build a Q&A bot over a set of PDF or text files
- **Challenge:** Add a memory component so the bot tracks conversation history

**Key glossary terms:** RAG, Embedding, Vector Database, Hallucination, Context Window, LangChain, Memory

---

## Class 5 — Claude Code: Agent Architecture and Design (2 hours)

### Lesson 07 — Claude Code: Agent Architecture and Design
**Theme:** Understand what agents are, then build one with Claude Code.

**Topics:**
- *Agent Architecture:*
  - The difference between a chatbot and an agent
  - The four components of an agent: perception, memory, reasoning, action
  - The agentic loop in detail
  - Types of memory: in-context, external (RAG), persistent
  - Types of tools: search, code execution, file I/O, APIs
  - Agent failure modes: infinite loops, hallucinated tool calls, context overflow
  - Real-world case study: an agent that automates a multi-step research task
- *Claude Code Introduction:*
  - What is Claude Code and how is it different from Copilot or ChatGPT?
  - Installation and setup
  - How Claude Code reads files, runs commands, and uses tools
  - The permission model: what Claude can and cannot do by default
  - First session: navigating and understanding a codebase
  - **Exercise:** Use Claude Code to refactor a small Python project
- *Claude Code Deep Dive — Memory, CLAUDE.md, and Skills:*
  - `CLAUDE.md`: giving Claude project-specific memory and instructions
  - Global vs. project-level `CLAUDE.md` files
  - Skills: reusable workflows as slash commands
  - Writing your own skill for a repetitive task
  - Memory types in Claude Code: in-context, file-based, external
  - Best practices for long-running agent sessions
  - **Exercise:** Write a `CLAUDE.md` for a real project and create a custom skill

**Key glossary terms:** Agent, Agentic Loop, Memory, Tool, Orchestration, Claude Code, CLAUDE.md, Skills

---

## Class 6 — Code Agents in Practice (2 hours)

### Lesson 08 — Antigravity: Build a Simple Application
**Theme:** Put it all together — write and ship a working app using an AI code agent.

**Topics:**
- Recap: what Antigravity is and how it fits into the code agent landscape
- Setting up an Antigravity project from scratch
- Translating a feature idea into an agent-friendly task description
- Iterating with the agent: reviewing diffs, approving changes, giving feedback
- Managing project context: GEMINI.md, knowledge base, and skills
- Debugging with an AI agent: reading errors, guiding fixes
- When to intervene vs. let the agent run
- Shipping: local preview, basic deployment (e.g., static site or simple API)
- **Exercise:** Build and deploy a small web app or CLI tool of your choice, entirely guided by Antigravity
- **Challenge:** Add a feature the agent didn't originally plan for and iterate to completion

**Key glossary terms:** Antigravity, Agent, GEMINI.md, Skills, Tool, Agentic Loop

---

## Class 7 — Claude Cowork: Document and Data Analysis (2 hours)

### Lesson 09 — Claude Cowork: Document and Data Analysis
**Theme:** Use Claude's collaborative workspace to analyze real documents and data — no code required.

**Topics:**
- What is Claude Cowork (claude.ai Projects)? Sharing context across a conversation
- Uploading and working with PDFs, Word files, spreadsheets, and CSVs
- Asking nuanced questions across multiple documents
- Extracting structured data: tables, key facts, summaries
- Code Interpreter in Claude: generating and running Python for data analysis
- Building a repeatable document review workflow (e.g., contracts, reports)
- Generating charts, pivot summaries, and written reports from raw data
- Real-world case study: a team automating weekly business reporting
- **Exercise:** Upload a mixed set of documents (PDF + CSV), extract key insights, and produce a structured summary report
- **Challenge:** Design a repeatable prompt workflow that a non-technical colleague could run themselves

**Key glossary terms:** Claude Cowork, Structured Output, Tool Calling, Code Interpreter, Notebook, RAG

---

## Class 8 — OpenClaw: Local AI and Personal Agents (2 hours)

### Lesson 10 — OpenClaw: Local AI and Personal Agents
**Theme:** Run AI on your own machine and automate personal tasks with OpenClaw.

**Topics:**
- *Local AI Foundations:*
  - Why run AI locally? Privacy, cost, control, and offline use
  - Local models: Ollama, LM Studio, and running open-weight models
  - Trade-offs: capability vs. privacy vs. cost
- *OpenClaw:*
  - OpenClaw: personal AI assistant with messaging app integration
  - Setup and configuration
  - Persistent memory and skills
  - Browser automation and file system access
  - Connecting to local or cloud models
  - **Exercise:** Set up OpenClaw and automate a personal task via Telegram or Slack

**Key glossary terms:** OpenClaw, Memory, Tool, Agent, Skills, Ollama

---

## Class 9 — OpenClaw: Build a Marketing Agent (2 hours)

### Lesson 11 — OpenClaw: Build a Marketing Agent
**Theme:** Advanced local agency — building a production-ready marketing assistant.

**Topics:**
- Defining a complex multi-tool agent: web search, browser automation, and local file access
- Workflow design: research → plan → generate → review
- Using skills for task-specific intelligence
- Connecting OpenClaw to specific local datasets
- Fine-tuning the interaction model for marketing copy and strategy
- **Exercise:** Build a marketing agent that researches a competitor, plans a campaign, and drafts three social media posts
- **Challenge:** Add a skill that allows the agent to analyze brand sentiment using browser automation

**Key glossary terms:** OpenClaw, Agent, Skills, Tool, Orchestration, Memory

---

## Class 10 — No-Code Agents with N8N (2 hours)

### Lesson 12 — No-Code Agents with N8N
**Theme:** Build powerful AI workflows without writing a line of code.

**Topics:**
- What is N8N? Visual workflow automation vs. code-based agents
- N8N concepts: nodes, triggers, workflows, and credentials
- Connecting N8N to LLMs: OpenAI, Claude, and Gemini nodes
- AI Agent node: giving N8N the ability to reason and use tools
- Built-in tools: web search, HTTP requests, code execution, file handling
- Chaining workflows: using sub-workflows as tools for a parent agent
- Memory in N8N: session memory and persistent storage
- Self-hosting vs. N8N Cloud: privacy and deployment options
- **Exercise:** Build an AI agent workflow that monitors a news feed, summarizes articles, and sends a daily digest by email
- **Challenge:** Add a RAG step — store article summaries in a vector store and let the agent answer questions about past news

**Key glossary terms:** N8N, Agent, Agentic Loop, Tool, Orchestration, Memory, Workflow Automation


*Lessons are interleaved: concept → guided exercise → independent challenge. Each lesson ends with a short quiz referencing the glossary.*
