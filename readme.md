# 🔒 Open Safe AI

Open Safe AI is a lightweight project aiming to provide a safe and transparent local LLM server.

## 🚀 Overview

Many local LLM projects claim to be secure, but the reality is that their codebases are often too large and complex to verify easily.
Open Safe AI is built with a different philosophy:

 -	✅ Minimal features
 -	✅ Short, readable code
 -	✅ Transparent and verifiable data flow

The goal is to make AI systems that anyone can inspect, understand, and trust.

---

## ⚙️ Installation

```bash
git clone https://github.com/hslee1539/open-safe-ai.git
cd open-safe-ai
pip install .
```

> ✅ This will install `open-safe-ai` along with its dependencies.

You’ll then be able to run commands using:

```bash
open-safe-ai
```

## 🧩 CLI Commands (powered by Typer)

```bash
open-safe-ai list
```
✅ Shows a list of installed HuggingFace models.

```bash
open-safe-ai serve
```
✅ Starts the server.
Exposes the following minimal REST API endpoints:
-	POST /generate : Text generation
-	GET /list : Available models

```bash
open-safe-ai run <model-name>
```

✅ Loads the specified model and provides a simple chat interface, similar to ollama run model.