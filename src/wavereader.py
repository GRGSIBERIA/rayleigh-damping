import wave
import numpy as np

class NotSupportSampleWidthError(Exception):
    pass


class WaveData:
    def __init__(self, path):
        with wave.open(path, "rb") as wav:
            self.samplingRate = wav.getframerate()
            self.frames = wav.getnframes()
            self.channels = wav.getnchannels()
            self.sampleWidth = wav.getsampwidth()

        buf = wav.readframes(frames)
        
        dtype = "int16"
        if self.sampleWidth == 4:
            dtype = "int32"
        elif self.sampleWidth == 3:
            raise NotSupportSampleWidthError("Use int24")
        
        self.deltaTime = 1. / self.lamplingRate
        self.totalTime = self.frames * self.deltaTime
        self.data = np.frombuffer(buf, dtype=dtype).astype("float64")