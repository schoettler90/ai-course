# Course Pensum: AI Agents — From Zero to Builder

A ~20-hour beginner-friendly course on AI and AI Agents.
Each lesson is approximately 1 hour and includes a concept explanation, real-world case study, guided hands-on exercise, independent challenge, and quiz.

---

## Course Map at a Glance

| # | Lesson | Module | Tools / Frameworks |
|---|--------|--------|--------------------|
| 01 | Welcome: AI in the Real World | Foundations | Claude Code (demo) |
| 02 | A Brief History of AI | Foundations | — |
| 03 | How LLMs Work, First AI Tools & Prompt Engineering | Foundations | ChatGPT, Claude.ai, Gemini |
| 04 | Multimodal AI: Beyond Text | Foundations | Claude, GPT-4V, DALL-E, Whisper |
| 05 | Machine Learning: Concepts & Practice | ML by Hand | Python, PyTorch, Jupyter |
| 06 | Using LLM APIs | LLMs in Code | Anthropic SDK, OpenAI SDK |
| 07 | Tools, Structured Outputs & MCP | LLMs in Code | Anthropic SDK, JSON, MCP |
| 08 | RAG: Concepts & Implementation | RAG | LangChain, Chroma |
| 09 | Agent Architecture and Design | Agents | — |
| 10 | Agents with LangChain | Agents | LangChain |
| 11 | No-Code Agents with N8N | Agents | N8N |
| 12 | Claude Code Introduction | Code Agents | Claude Code |
| 13 | Claude Code: Memory and Skills | Code Agents | Claude Code |
| 14 | Computer Use & The Code Agent Ecosystem | Code Agents | Claude, Playwright, Gemini CLI, Antigravity, Codex |
| 15 | Practice: Build a Simple Application with Antigravity | Code Agents | Antigravity |
| 16 | Practice: Document and Data Analysis with Claude Cowork | Code Agents | Claude Cowork |
| 17 | Local AI and OpenClaw | Local AI | OpenClaw, Ollama |
| 18 | Practice: OpenClaw Deep Dive — Build a Marketing Agent | Local AI | OpenClaw |
| 19 | Multi-Agent Systems | Advanced | LangGraph, AutoGen |
| 20 | Ethics, Safety, and What's Next | Advanced | — |

---

## Module 1 — Foundations

### Lesson 01 — Welcome: AI in the Real World
**Theme:** Who is this course for, and why does it matter now?

**Topics:**
- Introduction: instructor background, motivation for the course
- What is AI? What is an AI agent? (intuitive definitions, no jargon)
- Real-world use cases: AI in daily life, business, science, and creativity
- Live demo: Claude Code as a state-of-the-art agent in action
- Overview of the 20-lesson journey ahead

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

### Lesson 03 — How LLMs Work, Your First AI Tools & Prompt Engineering
**Theme:** Understand the models, use them, and learn to speak their language.

**Topics:**
- Tokens: how text becomes numbers
- The context window: what the model can "see"
- Pre-training vs. fine-tuning vs. RLHF
- Why models hallucinate — and what to do about it
- System prompts and how they shape behavior
- Tour of ChatGPT, Claude.ai, and Gemini — similarities, differences, pricing
- When to use which tool
- *Prompt Engineering:*
  - The anatomy of a good prompt: role, context, task, format
  - Zero-shot, few-shot, and chain-of-thought prompting
  - Common mistakes and how to fix them
- **Exercise:** Solve the same three tasks across all three tools, then rewrite 3 weak prompts into strong ones

**Key glossary terms:** Token, Context Window, Fine-tuning, RLHF, Hallucination, System Prompt, Prompt Engineering, ChatGPT, Claude, Gemini

---

### Lesson 04 — Multimodal AI: Beyond Text
**Theme:** AI that can see, hear, and generate images.

**Topics:**
- What is multimodal AI? Moving past text-only models
- Sending images to models: Claude, GPT-4V, Gemini Vision
- Vision tasks: describe, analyze, compare, and extract data from images
- Reading documents visually: OCR, scanned PDFs, screenshots
- Image generation: DALL-E, Midjourney, and Stable Diffusion (concepts and use)
- Audio AI: speech-to-text (Whisper), text-to-speech
- Real-world use cases: accessibility tools, receipt parsing, visual search
- **Exercise:** Build a pipeline that takes a photo of a handwritten note or receipt and extracts structured data
- **Challenge:** Generate three image variations from a text brief

**Key glossary terms:** Multimodal, Token, Context Window, API

---

## Module 2 — Machine Learning by Hand

### Lesson 05 — Machine Learning: Concepts & Practice
**Theme:** Understand the ideas, then train your first neural network.

**Topics:**
- Supervised vs. unsupervised vs. reinforcement learning
- Training, validation, and test sets
- Loss functions, gradient descent, and backpropagation (conceptual)
- Overfitting, underfitting, and the role of data
- Real-world ML: spam filters, recommendation engines, fraud detection
- Setting up a Python environment with `uv` and Jupyter
- The MNIST dataset: handwritten digit recognition
- Building a simple feedforward network in PyTorch
- Training loop: forward pass, loss, backward pass, weight update
- Visualizing training: loss curves and accuracy
- **Exercise:** Train the network and modify the architecture to improve accuracy
- **Challenge:** Train on a different dataset (e.g., FashionMNIST)

**Key glossary terms:** Machine Learning, Deep Learning, Neural Network, Weight, Reinforcement Learning, Notebook, GPU

---

## Module 3 — Working with LLMs Programmatically

### Lesson 06 — Using LLM APIs
**Theme:** Going beyond the chat interface — talking to models in code.

**Topics:**
- What is an API and why use it programmatically?
- Getting API keys: OpenAI, Anthropic, Google
- Making your first API call in Python
- Request structure: messages, roles, model selection
- Handling responses and errors
- Cost awareness: tokens, pricing, rate limits
- **Exercise:** Build a simple Python script that answers questions via the Claude API

**Key glossary terms:** API, Token, LLM, Client

---

### Lesson 07 — Tools, Structured Outputs & MCP
**Theme:** Making LLMs reliable components — and connecting them to everything.

**Topics:**
- Why unstructured text output is hard to use in code
- Structured outputs: asking models to respond in JSON
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

**Key glossary terms:** Tool Calling, Structured Output, JSON, Tool, API, MCP

---

## Module 4 — Retrieval-Augmented Generation (RAG)

### Lesson 08 — RAG: Concepts & Implementation
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

## Module 5 — Building AI Agents

### Lesson 09 — What Makes an Agent? Architecture and Design
**Theme:** Moving from question-answering to goal-achieving.

**Topics:**
- The difference between a chatbot and an agent
- The four components of an agent: perception, memory, reasoning, action
- The agentic loop in detail
- Types of memory: in-context, external (RAG), persistent
- Types of tools: search, code execution, file I/O, APIs
- Agent failure modes: infinite loops, hallucinated tool calls, context overflow
- Real-world case study: an agent that automates a multi-step research task

**Key glossary terms:** Agent, Agentic Loop, Memory, Tool, Orchestration, Multi-step Reasoning

---

### Lesson 10 — Building Agents with LangChain
**Theme:** Hands-on: wire together an agent that reasons and acts.

**Topics:**
- LangChain agents: ReAct, tool-use, and planning patterns
- Defining custom tools in Python
- Connecting agents to the web (search), files, and APIs
- Observability: logging and tracing agent steps
- **Exercise:** Build a research agent that searches the web and summarizes findings
- **Challenge:** Add a tool that saves results to a file

**Key glossary terms:** LangChain, Agent, Tool Calling, Agentic Loop, Orchestration

---

### Lesson 11 — No-Code Agents with N8N
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

---

## Module 6 — Code Agents

### Lesson 12 — Claude Code: An Agent That Writes and Runs Code
**Theme:** Meet the state-of-the-art in agentic software development.

**Topics:**
- What is Claude Code and how is it different from Copilot or ChatGPT?
- Installation and setup
- How Claude Code reads files, runs commands, and uses tools
- The permission model: what Claude can and cannot do by default
- First session: navigating and understanding a codebase
- **Exercise:** Use Claude Code to refactor a small Python project

**Key glossary terms:** Claude Code, Tool, Agentic Loop, Agent

---

### Lesson 13 — Claude Code Deep Dive: Memory, CLAUDE.md, and Skills
**Theme:** Making Claude Code work the way you want, persistently.

**Topics:**
- `CLAUDE.md`: giving Claude project-specific memory and instructions
- Global vs. project-level `CLAUDE.md` files
- Skills: reusable workflows as slash commands
- Writing your own skill for a repetitive task
- Memory types in Claude Code: in-context, file-based, external
- Best practices for long-running agent sessions
- **Exercise:** Write a `CLAUDE.md` for a real project and create a custom skill

**Key glossary terms:** CLAUDE.md, Skills, Memory, Claude Code

---

### Lesson 14 — Computer Use & The Code Agent Ecosystem
**Theme:** Agents that control browsers, plus the full landscape of coding tools.

**Topics:**
- What is computer use? Agents that perceive and interact with GUIs
- Claude's computer use capability: how it sees and acts on screen content
- Playwright-based browser automation: a code-first approach
- Building a browser agent that navigates, clicks, and extracts data
- Risks and safeguards: sandboxing, human-in-the-loop, scope limits
- Gemini CLI: terminal-based coding agent powered by Gemini
- Google Antigravity: the agent-first IDE — Editor view, Manager view, knowledge base
- OpenAI Codex CLI: architecture and use cases
- Side-by-side comparison: autonomy, safety, tool access, cost, privacy
- When to use a browser agent vs. terminal agent vs. visual workflow (N8N)
- **Exercise:** Build a browser agent that extracts structured data from a website, then repeat the same task using a second coding tool of your choice

**Key glossary terms:** Computer Use, Gemini CLI, Antigravity, Agent, Orchestration, Tool

---

### Lesson 15 — Practice: Build a Simple Application with Antigravity
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

### Lesson 16 — Practice: Document and Data Analysis with Claude Cowork
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

## Module 7 — Local and Personal AI

### Lesson 17 — Running AI Locally: OpenClaw and Privacy-First Agents
**Theme:** AI that lives on your machine, not in the cloud.

**Topics:**
- Why run AI locally? Privacy, cost, control, and offline use
- Local models: Ollama, LM Studio, and running open-weight models
- OpenClaw: personal AI assistant with messaging app integration
  - Setup and configuration
  - Persistent memory and skills
  - Browser automation and file system access
  - Connecting to local or cloud models
- Trade-offs: capability vs. privacy vs. cost
- **Exercise:** Set up OpenClaw and automate a personal task via Telegram or Slack

**Key glossary terms:** OpenClaw, Memory, Tool, Agent, Skills

---

### Lesson 18 — Practice: OpenClaw Deep Dive — Build a Marketing Agent with OpenClaw
**Theme:** Advanced local agency — building a production-ready marketing assistant.

**Topics:**
- Defining a complex multi-tool agent: web search, browser automation, and local file access
- Workflow design: research → plan → generate → review
- Using skills for task-specific intelligence
- Connecting OpenClaw to specific local datasets
- Fine-tuning the interaction model for marketing copy and strategy
- **Exercise:** Build a marketing agent that researches a competitor, plans a campaign, and drafts three social media posts
- **Challenge:** Add a skill that allows the agent to analyze brand sentiment using browser automation

---

## Module 8 — Advanced Topics and the Big Picture

### Lesson 19 — Multi-Agent Systems and Orchestration
**Theme:** What happens when agents work together?

**Topics:**
- From single agents to networks of agents
- Orchestrator-worker patterns
- Parallelism: running multiple agents on independent sub-tasks
- Communication between agents: passing context and results
- Failure handling in multi-agent systems
- Real-world example: a pipeline where one agent searches, one summarizes, one writes
- Introduction to agent frameworks: AutoGen, CrewAI, LangGraph
- **Exercise:** Build a two-agent pipeline where one agent gathers data and another formats a report

**Key glossary terms:** Orchestration, Agent, Agentic Loop, Multi-step Reasoning, LangChain

---

### Lesson 20 — Ethics, Safety, and What Comes Next
**Theme:** Being a responsible builder in the age of AI agents.

**Topics:**
- What can go wrong: hallucination, bias, unintended actions, misuse
- Agent safety: sandboxing, human-in-the-loop, permission models
- Privacy and data handling when using cloud models
- The environmental cost of large-scale AI
- AI alignment: why it's hard and why it matters
- Where the field is heading: reasoning models, embodied agents, AGI
- Your role as a builder: building responsibly
- **Capstone challenge:** Design (and optionally build) an agent that solves a real problem you care about

**Key glossary terms:** Hallucination, RLHF, Agent, Memory, Orchestration, Foundation Model





*Lessons are interleaved: concept → guided exercise → independent challenge. Each lesson ends with a short quiz referencing the glossary.*
