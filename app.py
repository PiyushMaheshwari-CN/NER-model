# app.py
from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from ner_processing import process_resumes

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 300 * 1024 * 1024  # 300 MB max (adjust if needed)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_files():
    if "files[]" not in request.files: 
        return "No files uploaded", 400

    files = request.files.getlist("files[]")
    if not files:
        return "No files uploaded", 400

    saved_paths = []
    for file in files:
        if file.filename == "":
            continue
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)
        saved_paths.append(filepath)

    try:
        # call the NER pipeline (end-to-end)
        success = process_resumes(saved_paths)
    except Exception as e:
        return f"Processing failed: {e}", 500

    if success:
        return f"Processing completed. Processed {len(saved_paths)} resume(s).", 200
    else:
        return "Processing finished with errors (check server logs).", 500


if __name__ == '__main__':
    # use host="0.0.0.0" if you want to access from other machines
    app.run(debug=True, host='0.0.0.0', port=5000)
