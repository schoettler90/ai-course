# Glossary of AI & Agent Terms

A reference for all key terms used throughout this course.

---

## A

**Agent**
A software system that perceives its environment, makes decisions, and takes actions to achieve a goal — often autonomously and over multiple steps. Modern AI agents combine a language model with tools, memory, and a control loop.

**AI (Artificial Intelligence)**
The broad field of computer science concerned with building systems that can perform tasks that typically require human intelligence, such as reasoning, learning, and problem-solving.

**AlexNet**
A deep convolutional neural network that won the 2012 ImageNet competition by a large margin, demonstrating the power of deep learning at scale and kickstarting the modern deep learning era.

**Anthropic**
The AI safety company that created Claude. Known for research into AI alignment and interpretability.

**Antigravity (Google Antigravity)**
An agent-first IDE developed by Google, announced in late 2025 alongside Gemini 3. Unlike traditional code editors, Antigravity is built around autonomous AI agents that can plan, execute, and verify complex coding tasks across your editor, terminal, and browser. Features a Manager view for orchestrating multiple agents in parallel, a built-in knowledge base for persistent learning, and support for multiple models (Gemini, Claude, GPT). Free for individuals.

**API (Application Programming Interface)**
A set of rules that lets one software system communicate with another. In this course, you'll use APIs to send messages to language models and receive responses.

**Agentic Loop**
The cycle an AI agent runs through: receive input → reason → choose a tool or action → observe the result → repeat until the goal is complete.

---

## C

**ChatGPT**
A conversational AI assistant built on GPT models by OpenAI. One of the first large language model products to reach mainstream adoption.

**Claude**
A family of large language models developed by Anthropic. Claude Code is an agentic coding assistant built on Claude.

**Claude Code**
Anthropic's official AI coding agent. It runs in the terminal, reads and edits files, executes commands, uses tools, and maintains memory across sessions through `CLAUDE.md` files and skills.

**CLAUDE.md**
A Markdown file placed in a project (or globally in `~/.claude/`) that gives Claude persistent context and instructions. It functions as long-term memory and project-specific configuration.

**Client (LLM Client)**
An application or interface used to interact with a language model. Examples include the ChatGPT web app, Claude.ai, Gemini, and terminal-based tools like Claude Code.

**CNN (Convolutional Neural Network)**
A type of neural network designed to process grid-like data such as images. Uses convolutional layers to detect local patterns (edges, shapes, textures). Became dominant in computer vision after AlexNet.

**Computer Use**
The ability of an AI agent to perceive and interact with graphical user interfaces — taking screenshots, moving the mouse, clicking, and typing — rather than only calling structured APIs. Enables agents to use any software a human can use. Introduced by Anthropic in Claude.

**Context Window**
The maximum amount of text (measured in tokens) a language model can "see" at once — including the conversation history, system prompt, and any documents provided.

**Control Loop**
See *Agentic Loop*.

---

## D

**Deep Learning**
A subfield of machine learning that uses neural networks with many layers ("deep" networks). Enabled breakthroughs in image recognition, speech, and language tasks.

---

## E

**Embedding**
A numerical vector representation of text (or other data) that captures semantic meaning. Embeddings are used in RAG to find relevant documents by similarity.

---

## F

**Fine-tuning**
Adapting a pre-trained model to a specific task or domain by training it further on a smaller, task-specific dataset.

**Foundation Model**
A large model trained on broad data at scale, designed to be adapted to many downstream tasks. GPT-4, Claude, and Gemini are foundation models.

---

## G

**Gemini**
A family of large language models developed by Google DeepMind. Available through Google AI Studio and the Gemini API.

**Gemini CLI**
Google's terminal-based agentic coding assistant, similar to Claude Code, powered by Gemini models.

**GPT (Generative Pre-trained Transformer)**
OpenAI's series of language models (GPT-2, GPT-3, GPT-4, etc.). "Generative" means they produce text; "Pre-trained" means trained on large corpora before fine-tuning; "Transformer" refers to the underlying architecture.

**GPU (Graphics Processing Unit)**
Originally designed for rendering graphics, GPUs became essential for training neural networks due to their ability to perform many parallel computations simultaneously.

---

## H

**Hallucination**
When a language model confidently generates information that is factually incorrect or fabricated. A known limitation of current LLMs.

---

## J

**JSON (JavaScript Object Notation)**
A lightweight text format for structured data. Commonly used for API requests, tool call results, and structured outputs from language models.

---

## L

**LangChain**
A popular open-source framework for building LLM-powered applications. Provides abstractions for chains, agents, memory, and retrieval. Used in this course to build RAG pipelines and agents.

**LLM (Large Language Model)**
A neural network trained on massive amounts of text data, capable of generating, summarizing, translating, and reasoning about text. Examples: GPT-4, Claude, Gemini.

**LLM Client**
See *Client*.

---

## M

**MCP (Model Context Protocol)**
An open standard created by Anthropic for connecting AI models to external tools, data sources, and services in a consistent way. Replaces fragile one-off integrations with a common protocol: any MCP-compatible model can use any MCP server (filesystem, GitHub, databases, Slack, etc.) without custom glue code. Used extensively with Claude Code.

**Multimodal**
Describes AI models or systems that can process and generate multiple types of data — text, images, audio, video — rather than just text. Examples: GPT-4V (vision), Claude (images + text), Whisper (audio → text), DALL-E (text → image).

**Machine Learning (ML)**
A subset of AI where systems learn patterns from data rather than being explicitly programmed. Includes supervised learning, unsupervised learning, and reinforcement learning.

**Memory (Agent)**
The ability of an agent to retain information across turns or sessions. Types include:
- **In-context memory**: information in the current context window
- **External memory**: databases or files retrieved at runtime (see *RAG*)
- **Persistent memory**: files like `CLAUDE.md` that survive across sessions

**Model**
In ML, a mathematical function trained on data that makes predictions or generates outputs. In everyday usage, "model" often refers to an LLM like GPT-4 or Claude Sonnet.

**Multi-step Reasoning**
The ability of an agent to break a goal into sub-tasks, execute them in sequence, and combine results — rather than answering in a single step.

---

## N

**N8N**
An open-source workflow automation platform that lets you connect apps, services, and AI models through a visual node-based interface — no code required. Each node performs an action (call an API, send an email, query a database). Includes a dedicated AI Agent node that can reason, choose tools, and loop until a goal is complete. Can be self-hosted for privacy or used via N8N Cloud. In this course, used to build no-code AI agent workflows.

**Neural Network**
A computational model loosely inspired by the brain, consisting of layers of interconnected nodes (neurons) that transform input data into output predictions through learned weights.

**Notebook (Jupyter Notebook)**
An interactive computing environment that combines code, output, and explanatory text in a single document. Used in this course for hands-on ML exercises.

---

## O

**OpenAI**
The AI company behind the GPT series and ChatGPT. One of the leading AI labs alongside Anthropic and Google DeepMind.

**OpenClaw**
An open-source personal AI assistant that runs locally on your machine (Mac, Windows, Linux). Created by Peter Steinberger, it integrates with messaging apps (WhatsApp, Telegram, Discord, Slack) as its interface. Features persistent memory, browser automation, file system access, shell execution, and extensible skills. Supports multiple models (Claude, GPT, or local models). Represents a decentralized, user-controlled alternative to cloud-hosted AI assistants.

**Orchestration**
Coordinating multiple agents, tools, or steps to accomplish a complex task. An orchestrator decides which sub-agent or tool to invoke at each step.

---

## P

**Prompt**
The input text sent to a language model. Includes the user's question, any instructions, and context. Prompt engineering is the practice of designing effective prompts.

**Prompt Engineering**
The practice of crafting inputs to language models to elicit better, more accurate, or more useful outputs.

---

## R

**RAG (Retrieval-Augmented Generation)**
A technique where relevant documents are retrieved from a knowledge base (using embeddings and vector search) and injected into the model's context before it generates a response. Used to ground answers in specific, up-to-date information.

**Reinforcement Learning (RL)**
A training approach where an agent learns by receiving rewards or penalties based on actions. Used in RLHF to align language models with human preferences.

**RLHF (Reinforcement Learning from Human Feedback)**
A technique used to fine-tune language models using human ratings of model outputs, making them more helpful and less harmful.

---

## S

**Scaling Laws**
Empirical findings (notably from OpenAI) showing that model performance improves predictably as you increase model size, dataset size, and compute — following power-law relationships.

**Skills (Claude Code)**
Reusable instruction files that extend Claude Code's behavior for specific workflows (e.g., writing plans, debugging, TDD). Stored as Markdown files and invoked as slash commands.

**Structured Output**
When a language model is instructed to respond in a specific format (e.g., JSON with defined fields) rather than free-form text. Useful for integrating LLM outputs into code.

**System Prompt**
Instructions given to a language model before the conversation begins. Sets the model's role, tone, constraints, and any persistent context.

---

## T

**Token**
The basic unit of text that a language model processes. Roughly 4 characters or ¾ of a word in English. Models have a fixed context window measured in tokens.

**Tool (Agent Tool)**
A function an agent can call to interact with the outside world — e.g., search the web, read a file, run code, call an API. Tools extend what an agent can do beyond generating text.

**Tool Calling (Function Calling)**
The ability of a language model to request that a specific function be executed, passing structured arguments. The result is then fed back to the model.

**Transformer**
The neural network architecture introduced in the 2017 paper *"Attention Is All You Need"*. Uses self-attention mechanisms to process sequences in parallel. The foundation of virtually all modern LLMs including GPT, Claude, and Gemini.

---

## V

**Vector Database**
A database optimized for storing and searching high-dimensional vectors (embeddings). Used in RAG to find semantically similar documents. Examples: Chroma, Pinecone, Weaviate.

---

## W

**Weight**
A numerical parameter in a neural network that is adjusted during training. A model's "knowledge" is encoded in its billions of weights.

**Workflow Automation**
The practice of connecting apps, triggers, and actions into automated pipelines that run without manual intervention. Tools like N8N let you build visual workflows where AI models are just another node alongside databases, email, APIs, and more.

---

*This glossary is updated as new terms are introduced throughout the course.*
