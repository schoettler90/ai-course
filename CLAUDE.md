# AI Agents Course

## Project Goal

Build a 20-hour beginner-friendly course on AI Agents. The course is designed for a general audience — both technical and non-technical learners — who want to understand what AI agents are and how to build them.

## Course Structure

- 20 lessons, each approximately 1 hour
- Each lesson has its own subdirectory containing a lesson draft (`lesson-draft-##.md`), slides (`lesson-slides-##.pptx`), and potentially special notebooks for code examples.
- Lessons are interleaved: concept introduction → hands-on exercise → independent challenge
- Platform-agnostic: teaches concepts first, demonstrates with multiple tools

## Each Lesson Includes

- Concept explanation
- Real-world case study
- Guided hands-on exercise
- Independent challenge
- Quiz / knowledge check

## Course-Wide Elements

- Glossary of AI/agent terminology
- Quizzes after each lesson
- Real-world case studies woven throughout

## Student Outcomes

By the end of the course, students will:
1. Understand what AI agents are and how they work
2. Be able to build working agents using no-code/low-code tools
3. Have practical experience across a range of agent types and use cases

## Environment
- **Python**: Use **`uv`** for all Python-related tasks (e.g., `uv sync`, `uv run python script.py`, `uv pip install`).
- PDF reading requires poppler: `brew install poppler` (note: PDFs in `helper_files/` may be image-based and not machine-readable)
- Instructor reference materials (resume, bios) are in `helper_files/`

## Course Overview

The full course pensum — all 20 lessons, their topics, modules, and tools — is in `pensum.md`. Always check it for the big picture before creating or editing lesson files.

## File Organization

```
lessons/
  01-lesson-name/
    lesson-draft-01.md
    lesson-slides-01.pptx
    notebooks/  (optional)
  02-lesson-name/
    lesson-draft-02.md
    lesson-slides-02.pptx
  ...
  20-lesson-name/
glossary.md
pensum.md
```
