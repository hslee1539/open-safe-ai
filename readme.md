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

## 🧩 CLI Commands (powered by Typer)

```
python main.py list
```
✅ Shows a list of installed HuggingFace models.

```
python main.py serve
```
✅ Starts the server.
Exposes the following minimal REST API endpoints:
-	POST /generate : Text generation
-	GET /list : Available models

```
python main.py run <model-name>
```

✅ Loads the specified model and provides a simple chat interface, similar to ollama run model.