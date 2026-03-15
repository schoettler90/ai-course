# Lesson 1: Welcome: AI in the Real World

**Theme:** Who is this course for, and why does it matter now?

## 1. Introduction

Welcome to "AI Agents — From Zero to Builder"! This course is a 20-hour journey designed to take you from understanding what AI and AI Agents are, to actually building them to solve real problems. Whether you come from a highly technical background or have no coding experience at all, this course will equip you with the mental models and tools necessary to leverage AI effectively.

### About Your Instructor
Hi, I'm **Ricardo Schoettler**, an AI Engineer specializing in Generative AI and Machine Learning. Throughout my career, I've worked on bringing cutting-edge AI into practical, real-world applications:

*   **Generative AI Specialist (Hengeler Mueller, Frankfurt):** I currently design and build LLM Agents that take complex decisions based on user queries and available tools. I also implement Retrieval Augmented Generation (RAG) frameworks that let top legal professionals securely query millions of documents to solve legal use cases.
*   **Data Scientist (Green Fusion, Berlin):** I worked at a vibrant startup where I developed advanced ML and statistical models. Using Large Language Models (LLMs), I created Natural Language Processing (NLP) models to automatically classify hardware sensors based on text descriptions, optimizing real-time energy systems.
*   **Machine Learning Researcher (Charité, Berlin):** I designed advanced computer vision architectures integrating MRI scans and patient clinical data to predict long-term stroke outcomes (and co-authored a paper on the topic in *NeuroImage: Clinical*).
*   **Teaching & Tutoring:** During my time at TU Berlin—where I completed my BSc and MSc in *Wirtschaftsingenieurwesen* (Industrial Engineering)—I spent five years as an academic tutor, teaching complex statistics and econometrics to students.

I am passionate about making technical AI accessible. My motivation for this course is to help you bridge the gap between AI theory and practical building.

---

## 2. Concept Explanation: What is AI? What is an AI agent?

At its simplest, **Artificial Intelligence (AI)** is a broad field of computer science focused on creating systems capable of performing tasks that typically require human intelligence—like understanding language, recognizing images, or finding patterns in data. Today, the most popular form of AI is driven by **Large Language Models (LLMs)**, which are trained on massive amounts of text to predict and generate human-like language.

But this course is specifically about **AI Agents**.

An **AI Agent** is more than just a chatbot that answers your questions. Think of an LLM as a "brain in a jar" that knows a lot but can't act. 
An AI Agent takes that brain and gives it hands, eyes, and memory. It is a system that can:
1.  **Perceive** an environment or receive a goal.
2.  **Reason** about how to achieve that goal by creating a plan.
3.  **Act** by using tools (like searching the web, executing code, or querying a database).

If you ask a chatbot: *"What's the weather in Berlin?"* it might decline, saying it doesn't have real-time internet access.
If you ask an AI Agent the same thing, it will realize it needs a weather tool, execute a Python script or an API call to get the data, read the result, and report back to you.

---

## 3. Real-World Case Study: AI in the Wild

AI is no longer just an academic pursuit; it is reshaping entire industries:
*   **Business & Law:** As seen in my daily work, agents are dramatically accelerating document discovery. Instead of lawyers reading through millions of pages to find a specific clause, RAG-enabled agents can retrieve, synthesize, and cite the exact answer in seconds.
*   **Science & Healthcare:** In my past research at Charité, AI models analyzed complex patterns in MRI scans that human eyes might miss. This isn't replacing doctors; it's giving them a powerful co-pilot to improve patient outcomes.
*   **Daily Life & Creativity:** From Spotify generating custom playlists to personalized language tutors on your phone, AI agents interact with us constantly, anticipating our needs and personalizing our experiences.

---

## 4. Guided Hands-On Exercise: Claude Code Demo

*Note to self (Instructor): This section will be a live demonstration for the students. Set up the terminal environment before the lecture.*

To show you what a state-of-the-art code agent looks like in action, we'll do a live demo using **Claude Code**—a terminal-based agent. 

**Demo Steps:**
1.  Open an empty directory in the terminal.
2.  Start the agent using the `claude` command.
3.  Ask the agent to: *"Create a simple web application using Python and Flask that displays a random inspirational quote about AI every time the user refreshes the page."*
4.  Observe as the agent:
    *   Thinks about the goal.
    *   Autonomously writes out `app.py`.
    *   Suggests installing Flask.
    *   Instructs you on how to start the server.
5.  Open the browser to `localhost:5000` to show the working app.

This demo illustrates the leap from chatting with an AI to having an AI act as an autonomous builder. Over the next 19 lessons, you will learn the mechanics behind magic like this, and build agents of your own!

---

## 5. Independent Challenge

Your turn to start thinking agentically! 

**Task:** Write down three tasks in your day-to-day work or personal life that are highly repetitive. For each task, write a brief sentence on how an "Agent" might theoretically solve it if it had access to your computer or apps.

*Example:* 
- Task: Summarizing weekly expenses from my inbox. 
- Agent Solution: An agent reads emails securely, extracts any receipts into a spreadsheet, and emails me a summary every Friday.

Keep this list safe; we will refer back to it at the end of the course to see which of your ideas you are ready to build!

---

## 6. Quiz / Knowledge Check

Take 5 minutes to answer these questions:

1. How does an **AI Agent** differ fundamentally from a standard AI chatbot?
2. What does an LLM stand for, and what is its primary function?
3. Name one example from the instructor's background where AI was used outside of tech platforms (e.g., in law, health, or energy).

*(Answers will be discussed collectively during the next lesson.)*

---

**Key Glossary Terms to review:** AI, Agent, LLM, Claude Code
