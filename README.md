# AI Agents Course

Welcome to the **AI Agents — From Zero to Builder** course repository!

This repository contains all the lesson drafts, code examples, and materials for the 20-hour beginner-friendly course on AI Agents.

## Prerequisites & Installation

We use [uv](https://docs.astral.sh/uv/), an extremely fast Python package and project manager, to handle our Python dependencies and virtual environments.

### 1. Install `uv`

First, you need to install `uv` on your system. 

**Windows**:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS and Linux**:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
*(For alternative installation methods, check the [official uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).)*

### 2. Setup the Project Dependencies

One of the great features of `uv` is that you do not need to install Python manually. `uv` will automatically download and install the required Python version (Python 3.14+) when you install the project dependencies.

Clone this repository (if you haven't already), navigate to the folder, and run the `uv sync` command:

```bash
# Navigate to the project folder
cd ai-course

# Sync the project environment
uv sync
```

This single command will:
1. Download the required Python version in the background.
2. Create a hidden, isolated virtual environment (`.venv` folder).
3. Install all the exact package versions specified in the `uv.lock` file.

### 3. System Dependencies (Optional for OCR)

Some helper scripts (like `src/read_pdf.py`) rely on external system tools to perform Optical Character Recognition (OCR) on image-based PDFs. If you plan to run these specific scripts, you need to install Tesseract and Poppler:

**Windows (using Winget)**:
```powershell
winget install --id UB-Mannheim.TesseractOCR -e
winget install --id oschwartz10612.Poppler -e
```

**macOS (using Homebrew)**:
```bash
brew install tesseract poppler
```

## Running Code

Whenever you need to run a Python script in this project, simply prefix your command with `uv run`. This ensures the script uses the correct Python version and the isolated dependencies from your `.venv`:

```bash
uv run python src/read_pdf.py "helpers/Resume Schoettler 2025.pdf" "helpers/resume.txt"
```
