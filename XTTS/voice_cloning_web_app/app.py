from flask import Flask, render_template, request, send_file, redirect, url_for
from TTS.api import TTS
import os
from pathlib import Path
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = Path("recordings")
UPLOAD_FOLDER.mkdir(exist_ok=True)
MODEL = TTS("tts_models/multilingual/multi-dataset/your_tts", gpu=False)

output_path = Path("output.wav")

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    generated = False
    recordings = [f.name for f in UPLOAD_FOLDER.glob("*.wav")]

    if request.method == "POST":
        if "recording" in request.files and request.form.get("rec_name"):
            file = request.files["recording"]
            name = request.form["rec_name"].strip()
            if file and file.filename.endswith(".wav"):
                save_path = UPLOAD_FOLDER / f"{name}.wav"
                file.save(save_path)
                message = f"Recording '{name}' uploaded."
                recordings = [f.name for f in UPLOAD_FOLDER.glob("*.wav")]

        if request.form.get("text") and request.form.get("language") and request.form.get("speaker"):
            text = request.form["text"]
            lang = request.form["language"]
            speaker_file = UPLOAD_FOLDER / request.form["speaker"]

            MODEL.tts_to_file(text=text, speaker_wav=str(speaker_file), language=lang, file_path=str(output_path))
            generated = True

    return render_template("index.html", recordings=recordings, message=message, generated=generated)

@app.route("/download")
def download():
    return send_file(output_path, as_attachment=True)

@app.route("/play")
def play():
    return send_file(output_path, mimetype="audio/wav")

if __name__ == "__main__":
    app.run(debug=True)