# Whisper Speech to Text
The purpose of this project is to transcribe audio files using the Whisper API.

## Project Description
The project consists of three files:

+ **api.py**: This is the main file that contains the server implementation using FastAPI, which handles requests to transcribe audio files using the Whisper API.
+ **whisper.html**: This is the HTML file that contains the form to upload an audio file and displays the results of the transcription.
script.js: This is the JavaScript file that handles the UI logic of the whisper.html page.
+ **script.js**: a JavaScript file that handles the file upload and form submission.
+ **WhisperAPI**: class to interact with Whisper API

### Dependencies
The following dependencies are required to run this project:

+ Python 3.8 or higher
+ FastAPI
+ Jinja2
+ Uvicorn
+ aiohttp
+ pydub

### How to Run
To run the project, follow these steps:

1. Obtain OpenAI API key here <https://beta.openai.com/signup/> and save it to the `.env` file as `API_KEY=YOUR_KEY` 

1. Clone the repository:
    ```bash
    git clone https://github.com/kurkuruzo/whisper.git
    ```

    ```bash
    cd whisper-speech-to-text
    ```
2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
2. Install the dependencies:

    ```bash 
    pip install -r requirements.txt
    ```

3. Start the server:

    ```bash
    python api.py
    ```

4. Open your web browser and go to http://localhost:8000/ to access the web app.

### How to Use
1. Open the web app in your web browser.
2. Click the "Choose File" button and select an audio file to upload.
3. Click the "Upload" button to submit the form.
4. Wait for the server to transcribe the audio file.

The transcription will appear on the page once it is complete.

### Credits
This project was created by [Kurkuruzo](https://github.com/kurkuruzo) and uses the [OpenAI Whisper API](https://platform.openai.com/docs/api-reference/audio) for speech-to-text transcription.