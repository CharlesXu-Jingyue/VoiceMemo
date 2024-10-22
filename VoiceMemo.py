import openai
import os
from tkinter import Tk, simpledialog, filedialog, messagebox

# Function to set your OpenAI API key
def set_openai_api_key():
    """
    Prompt the user to input the OpenAI API key using a pop-up window.
    """
    Tk().withdraw()  # Hide the root window
    api_key = simpledialog.askstring("OpenAI API Key", "Please enter your OpenAI API key:", show="*")
    
    if not api_key:
        messagebox.showerror("API Key Error", "No API key was provided. Exiting application.")
        exit()
    
    print(api_key)
    openai.api_key = api_key

# Function to transcribe an audio file using the new API
def transcribe_audio(file_path):
    """
    Transcribe an audio file using the OpenAI API.
    Saves the transcription as a .txt file in the same directory as the audio file.
    
    :param file_path: The path to the audio file.
    """
    try:
        with open(file_path, 'rb') as audio_file:
            # Call the OpenAI Whisper API
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
        
        # Extract the directory and the file name without extension
        file_dir = os.path.dirname(file_path)
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # Define the path for the output text file
        output_file = os.path.join(file_dir, f"{file_name}_transcription.txt")
        
        # Write the transcription to the text file
        with open(output_file, "w") as f:
            f.write(transcript['text'])
        
        print(f"Transcription saved to: {output_file}")
    
    except Exception as e:
        print(f"Error transcribing audio: {e}")


# Function to prompt user for an audio file
def get_audio_file():
    """
    Prompt the user to select an audio file using a file dialog.
    """
    # Hide the root Tkinter window
    Tk().withdraw()
    
    # Open a file dialog for the user to choose the audio file
    file_path = filedialog.askopenfilename(
        title="Select an audio file",
        filetypes=[("Audio Files", "*.mp3 *.wav *.ogg *.flac *.m4a")]
    )
    
    return file_path

# Example usage
if __name__ == "__main__":
    # Set your OpenAI API key
    set_openai_api_key()

    # Prompt the user to select an audio file
    audio_file_path = get_audio_file()

    if audio_file_path:
        # Transcribe the audio file and save it to a text file
        transcribe_audio(audio_file_path)
    else:
        print("No file selected.")