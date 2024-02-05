from flask import Flask, abort, request
from tempfile import NamedTemporaryFile
import whisper
import torch

# Check if NVIDIA GPU is available
torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Using {DEVICE} device.")
print("Loading Whisper model ...")
# Load Whisper model
model = whisper.load_model("medium", device=DEVICE)

print("Whisper model loaded!")

app = Flask(__name__)


@app.route("/")
def hello():
    return "Whisper API is running!"


@app.route("/whisper", methods=['POST'])
def handler():
    if not request.files:
        # If the user didn't submit any files, return 400
        abort(400)

    # Result for each file
    results = []

    # Loop over all submitted files
    for filename, handle in request.files.items():
        temp = NamedTemporaryFile()
        # Write the uploaded file to a temporary file
        handle.save(temp)
        # Get the transcription
        result = model.transcribe(temp.name)
        # Store the result in the results list
        results.append({
            'filename': filename,
            'transcription': result['text'],
        })

    return {'results': results}
