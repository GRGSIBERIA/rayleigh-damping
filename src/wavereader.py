import wave
import numpy as np

class NotSupportSampleWidthError(Exception):
    pass


class WaveData:
    def __init__(self, path: str, fftSample: int, frameShift: int):
        self.fftSample = fftSample
        self.frameShift = frameShift

        with wave.open(path, "rb") as wav:
            self.samplingRate = wav.getframerate()
            self.frames = wav.getnframes()
            self.channels = wav.getnchannels()
            self.sampleWidth = wav.getsampwidth()

            buf = wav.readframes(self.frames)
        
        dtype = "int16"
        if self.sampleWidth == 4:
            dtype = "int32"
        elif self.sampleWidth == 3:
            raise NotSupportSampleWidthError("use int24")
        
        self.deltaFreq = self.samplingRate / self.fftSample
        self.deltaTime = 1. / self.samplingRate
        self.totalTime = self.frames * self.deltaTime
        self.data = np.frombuffer(buf, dtype=dtype).astype("float64")

        self.spectrogram = []
        appendSpec = self.spectrogram.append
        shiftedLoop = int(self.frames / self.frameShift)
        windowFunction = np.hanning(self.fftSample)
        self.frameCount = 0

        for i in range(shiftedLoop):
            offset = i * self.frameShift
            stop = offset + self.fftSample
            try:
                window = windowFunction * self.data[offset:stop]
            except ValueError:
                break   # 配列の要素数オーバーで抜ける
            spec = np.abs(np.fft.fft(window))[:self.fftSample]
            appendSpec(spec)
            self.frameCount += 1

        deltaCnt = self.frameShift * self.deltaTime
        
        self.hLabels = ["f:{:.3f}".format((i+1) * self.deltaFreq / 2.) for i in range(self.fftSample)]
        self.vLabels = ["t:{:.3f}".format(i * deltaCnt) for i in range(self.frameCount)]
