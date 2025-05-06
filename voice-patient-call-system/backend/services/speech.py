import azure.cognitiveservices.speech as speechsdk
from backend.config import SPEECH_KEY, SPEECH_REGION

class FileLikeObject(speechsdk.audio.PullAudioInputStreamCallback):
    def __init__(self, file_stream):
        super().__init__()
        self.file_stream = file_stream

    def read(self, size):
        """Reads 'size' bytes from the file stream and returns them as bytes."""
        data = self.file_stream.read(size)
        return data if data else b''  # Ensure bytes are returned, even on EOF

    def close(self):
        """Closes the file stream."""
        self.file_stream.close()

def transcribe_audio(audio_file, language="en-US"):
    """
    Transcribes an audio file using Azure Speech-to-Text.
    
    Args:
        audio_file: A file-like object containing the audio.
        language: Language for transcription (default: "en-US").
    
    Returns:
        Transcribed text if successful, else None.
    """
    try:
        # Configure speech recognition
        speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
        speech_config.speech_recognition_language = language  # Set language dynamically

        # Wrap file stream in a custom stream object
        audio_stream_callback = FileLikeObject(audio_file.stream)
        pull_stream = speechsdk.audio.PullAudioInputStream(audio_stream_callback)
        audio_input = speechsdk.audio.AudioConfig(stream=pull_stream)

        # Create the recognizer
        recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

        # Perform recognition
        result = recognizer.recognize_once()

        # Handle different recognition results
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech recognized.")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print(f"Speech recognition canceled: {cancellation_details.reason}")
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print(f"Error details: {cancellation_details.error_details}")
        
    except Exception as e:
        print(f"Error in transcribe_audio: {e}")

    return None
