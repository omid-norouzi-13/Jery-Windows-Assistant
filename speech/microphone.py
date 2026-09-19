import sounddevice as sd
from scipy.io.wavfile import write


class Microphone:


    def __init__(self, sample_rate=44100):

        self.sample_rate = sample_rate



    def record(self, duration=5, filename="recording.wav"):

        print("Recording...")


        audio = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1
        )


        sd.wait()


        write(
            filename,
            self.sample_rate,
            audio
        )


        print("Recording finished.")

        return filename