# VoiceMemo - Audio Transcription Tool

VoiceMemo is a desktop application that allows you to transcribe audio files into text using OpenAI’s Whisper model. The transcription is saved as a .txt file in the same directory as the audio file, using the audio file’s name.

## Features

- Audio Transcription: Convert audio files to text using OpenAI’s Whisper model.
- Supports Multiple Formats: Works with .mp3, .wav, .ogg, .flac, .m4a, and other common audio formats.
- Minimalist Design: Simple, user-friendly interface with easy audio file selection.
- Automated Text File Creation: Automatically saves the transcription as a .txt file in the same folder as the audio file.

## How it works

1. Select an Audio File: The user is prompted to select an audio file from their device.
2. Transcription: The app sends the audio file to OpenAI’s Whisper model and returns the transcription.
3. Save as Text: The transcription is saved as a .txt file with the same name as the audio file.

## Installation

### Prerequisites

- Python 3.9 or later
- OpenAI API key

### Clone the Repository

```bash
git clone https://github.com/your-username/VoiceMemo.git
cd VoiceMemo
```

### Install Required Dependencies

First, ensure that you have all required dependencies installed. You can install them using pip:

```bash
pip install -r requirements.txt
```

This will install the following libraries:
- openai
- tkinter
- PyInstaller (for generating executables)

### Running the Application

To run the application locally:

```bash
python3 VoiceMemo.py
```

The application will open a dialog to select an audio file. After the file is selected, the transcription will be generated and saved as a .txt file in the same directory as the audio file.

## Create Executable (Optional)

You can package the Python script into a standalone executable using `PyInstaller`. This allows users to run the app without needing to install Python or dependencies.

Run the following command to build the executable:

```bash
pyinstaller --onefile --windowed VoiceMemo.py
```

The executable will be found in the `dist/` directory.

## Configuration

To use the OpenAI API, the application requires an API key. You can hardcode the key directly in the script, or set it via environment variables:

1. Hardcode the API Key:

In the `VoiceMemo.py` file, replace the placeholder in the `set_openai_api_key()` function with your OpenAI API key.

```Python
def set_openai_api_key():
    openai.api_key = "your-api-key-here"
```

2. Set the API Key via Environment Variable:

Alternatively, set the key in your shell or terminal:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Contributing

We welcome contributions to improve the VoiceMemo project! Here’s how you can get started:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

## License

This project is completely open-source.

## Future Improvements

- UI Enhancements: Improve the user interface for a more seamless experience.
- Language Detection: Automatically detect the language of the audio file.
- Batch Transcription: Allow multiple files to be transcribed at once.
