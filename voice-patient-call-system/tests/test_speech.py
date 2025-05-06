import unittest
from services.speech import transcribe_audio

class TestSpeech(unittest.TestCase):
    def test_transcribe_audio(self):
        transcription = transcribe_audio('test_audio.wav')
        self.assertIsNotNone(transcription)

if __name__ == '__main__':
    unittest.main()