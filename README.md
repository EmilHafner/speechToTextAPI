

# Whisper API

This is a Flask web application that serves as an API for transcribing audio files using the Whisper ASR (Automatic Speech Recognition) model from OpenAI.

## Requirements

- Python 3.10
- Flask 3.0.1
- NVIDIA GPU (optional) - The Whisper ASR model is optimized for NVIDIA GPUs. If you don't have a GPU, you can still run the application, but the transcription process will be slower.

## Installation

1. Clone the repository.
2. Install the required Python packages using pip:

    ```bash
    pip3 install -r requirements.txt
    ```

3. Install the Whisper ASR model:

    ```bash
    pip3 install "git+https://github.com/openai/whisper.git"
    ```

## Running the Application

You can run the application using Flask's built-in server:

```bash
python3 -m flask run --host=0.0.0.0
```

The application will be available at `http://localhost:5000`.

## API Endpoints

* `GET /` (Health Check)
* `POST /whisper` Expects the request to contain one or more audio files. The response will contain the transcribed text.
    
### Example Response 
```json
{
  "results":  [
      {
      "filename":  "audio.mp3",
      "transcription":  "hello world"
      },
  ]
}
```
  
## Docker
You can also run the application using Docker. First, build the Docker image:

```bash
docker build -t whisper-api .
```

Then run the Docker container:
```bash
docker run -p 5000:5000 whisper-api
```
The application will be available at `http://localhost:5000`.


