from speech.microphone import Microphone


mic = Microphone()


file = mic.record(
    duration=5
)


print("Saved:", file)