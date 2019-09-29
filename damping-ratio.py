import sys
import os.path
import wave
import numpy as np
from scipy import signal
import matplotlib.pyplot as plot

def printhelp():
    print("python damping-ratio.py [wave file]")
    sys.exit()


def calcenvelope(x, ind):
    x_abs = np.abs(x)
    loc = np.where(np.diff(np.sign(np.diff(x_abs))) < 0)[0] + 1
    peak = x_abs[loc]
    envelope = np.interp(ind, loc, peak)
    return envelope


def readwavefile(path):
    with wave.open(path, "rb") as wav:
        samplingrate = wav.getframerate()
        frames = wav.getnframes()
        channels = wav.getnchannels()
        samplewidth = wav.getsampwidth()

        print(path)
        print("sampling rate : ", samplingrate)
        print("channels      : ", channels)
        print("sample width  : ", samplewidth)
        print("frames        : ", frames)
        print("total times   : ", 1./samplingrate * frames)

        buf = wav.readframes(frames)

    dtype = "int16"
    if samplewidth == 4:
        dtype = "int32"
    elif samplewidth == 3:
        print("ERROR: 24 bit audio cannot be reading")
        sys.exit()
    return (np.frombuffer(buf, dtype=dtype).astype("float64"), samplingrate)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        printhelp()

    wavpath = sys.argv[1]
    if not os.path.exists(wavpath):
        printhelp()
    
    data, samplerate = readwavefile(wavpath)
    deltatime = 1. / samplerate
    x = np.arange(0, len(data) * deltatime, deltatime)[:-1]

    envelope = np.imag(signal.hilbert(data, 1024))
    plot.plot(envelope)

    for _ in range(5):
        envelope = np.imag(signal.hilbert(envelope))
    plot.plot(envelope)

    plot.show()
    