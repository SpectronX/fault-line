from flask import Flask, jsonify, render_template, request
from ollama import RequestError, ResponseError, chat
import os

app = Flask(__name__)

BOARDS = (
    "AVR (ATmega328P)",
    "STM32 (Blue Pill)",
    "ESP32",
    "Generic/Unknown",
)

MODEL = os.environ.get("OLLAMA_MODEL", "gemma3:4b")


def system_prompt(board: str) -> str:
    return (
        f"You are an embedded systems debugging assistant specialized in {board}. "
        "Given a raw error, fault dump, compiler error, or log snippet, explain "
        "what's happening in plain terms and give concrete next steps to fix it. "
        "Be concise and technical, assume the reader knows C and basic electronics."
    )


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/explain")
def explain():
    data = request.get_json(silent=True) or {}
    log = data.get("log")
    board = data.get("board")

    if not isinstance(log, str) or not log.strip():
        return jsonify({"error": "Provide a non-empty log string."}), 400
    if board not in BOARDS:
        return jsonify({"error": f"board must be one of: {', '.join(BOARDS)}"}), 400

    try:
        response = chat(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt(board)},
                {"role": "user", "content": log},
            ],
            stream=False,
        )
    except (ConnectionError, RequestError):
        return (
            jsonify(
                {
                    "error": "Ollama not running — start it with `ollama serve`",
                }
            ),
            503,
        )
    except ResponseError as exc:
        if getattr(exc, "status_code", None) == 404:
            return jsonify({"error": f"Ollama model '{MODEL}' is unavailable. Run `ollama pull {MODEL}` and try again."}), 503
        return jsonify({"error": str(exc)}), 503

    explanation = ""
    message = getattr(response, "message", None)
    if message is not None:
        explanation = getattr(message, "content", "") or ""
    if not explanation and isinstance(response, dict):
        explanation = (response.get("message") or {}).get("content") or ""

    return jsonify({"explanation": explanation})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
