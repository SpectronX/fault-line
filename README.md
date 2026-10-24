# Fault Line

Fault Line is a local web app that explains embedded systems errors, fault dumps, compiler output, and logs using a model served by Ollama.

## What we're solving

Embedded and firmware debugging often starts with cryptic output: fault register dumps, linker errors, or compiler messages that take deep datasheet knowledge or hours of forum searching to decode. That knowledge bottleneck slows down beginners and experienced developers alike, especially when they are working outside their usual microcontroller family.

Fault Line turns that lookup and reasoning step into one paste-and-explain action. It runs locally through Ollama, so it can work without a reliable internet connection and keeps debugging data on your device. The default Gemma model uses open weights, making the model pipeline inspectable and forkable.

The goal is not simply to have AI explain errors. Fault Line focuses on embedded debugging and combines that domain focus with local execution and open weights, rather than relying on a closed cloud API.

## Requirements

- Python 3.10 or later
- [Ollama](https://ollama.com/download)

## Install

Create and activate a virtual environment, then install the Python dependencies:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Prepare Ollama

The app uses `gemma3:4b` by default. Download it once before using the app:

```sh
ollama pull gemma3:4b
```

Make sure Ollama is running. The Ollama desktop app can run the local service, or you can start it from a terminal:

```sh
ollama serve
```

When you click **Explain**, Fault Line sends the request to Ollama. Ollama runs the model if it is already available locally; the app does not automatically download missing models. If the selected model is missing, the app displays the corresponding `ollama pull` command.

## Run

With the virtual environment active:

```sh
python app.py
```

Open <http://127.0.0.1:5000> in your browser. Paste an error or log, choose a board, and click **Explain**.

## Choose another model

Pull the model in Ollama first, then set `OLLAMA_MODEL` when starting Fault Line. For example:

```sh
ollama pull llama3.2
OLLAMA_MODEL=llama3.2 python app.py
```

PowerShell:

```powershell
ollama pull llama3.2
$env:OLLAMA_MODEL = "llama3.2"
python app.py
```
