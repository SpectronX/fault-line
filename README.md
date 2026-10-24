# Fault Line

Fault Line is a local web app that explains embedded systems errors, fault dumps, compiler output, and logs using a model served by Ollama.

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
