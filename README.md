# HomeAutomationWithAI_Jarvis

It is a smart home assistant inspired by the AI from Iron Man. This project uses speech recognition, text-to-speech, and home automation controls to create a responsive and interactive assistant. The assistant is capable of recognizing voice commands, processing them using a language model, and controlling smart home devices accordingly. The LLM used here is Gemini-pro. You can run this on Raspberry Pi.

## Features

- **Voice Activation**: Wake up the assistant by saying "Jarvis" or "Computer".
- **Speech Recognition**: Recognize and interpret voice commands.
- **Text-to-Speech**: Provide audible responses and confirmations.
- **Home Automation**: Control smart home devices based on user commands.
- **Error Handling**: Handle unknown or unclear commands gracefully.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- `pyaudio`
- `speech_recognition`
- `pygame`
- `edge-tts`
- `pvporcupine`
- `langchain_google_genai`
- `google-generativeai`

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/jarvis.git
    cd jarvis
    ```

2. **Install dependencies**:
    ```sh
    pip install pyaudio speechrecognition pygame edge-tts pvporcupine langchain_google_genai google-generativeai
    ```

3. **API Keys**:
    - Obtain the necessary API keys for Google Generative AI and Porcupine.
    - Create a file named `api_key.py` and add your Google API key:
        ```python
        GOOGLE_API_KEY = "your_google_api_key"
        ```
    - Create a file named `porcupine_key.py` and add your Porcupine access key:
        ```python
        access_key = "your_porcupine_access_key"
        ```

4. **Audio Files**:
    - Ensure you have the following audio files in the same directory: `yesmaster.mp3`, `jarviscametolive.mp3`, `sorryicouldntunderstand.mp3`, `beep1.mp3`, `beep2.mp3`.

## Code Overview

### `recognize_speech()`

This function uses the `speech_recognition` library to capture and recognize speech from the microphone.

### `good_format(lines)`

This function formats the response received from the language model to a proper JSON format.

### `speak()`

This function plays the generated audio file using `pygame`.

### `yesmaster()`, `jarviscametolive()`, `sorryicouldntunderstand()`, `beep1()`, `beep2()`

These functions play specific audio files for different events (command acknowledgment, activation, error handling, etc.).

### `generate_sound(generated)`

This function uses `edge-tts` to convert text to speech and save it as an audio file.

### `ai()`

This is the core function that:
- Activates on voice command.
- Uses the language model to process the user's query.
- Controls smart home devices based on the interpreted command.
- Provides audible feedback.

### `main()`

This function initializes the wake word detection using Porcupine and listens for the wake words ("Jarvis" or "Computer"). Once activated, it calls the `ai()` function to process commands.

## Running the Project

To start J.A.R.V.I.S., simply run the `main()` function in your Python environment:

```sh
python jarvis.py
