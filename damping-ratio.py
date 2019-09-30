import sys
import os.path
import wave
import json
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


def spectrogram(js, data):
    frameshift = int(js["fft"]["frame shift"])
    samples = int(js["fft"]["samples"])
    numframes = int((len(data) - samples) / frameshift)

    specs = []
    window = np.hamming(samples)
    for i in range(numframes):
        idx = i * frameshift
        windowed = window * data[idx:idx+samples]
        spectrum = np.abs(np.fft.fft(windowed))
        specs.append(spectrum)
    specgram = np.array(specs)

    print("frame shift      : ", frameshift)
    print("samples          : ", samples)
    print("number of frames : ", numframes)

    return specgram


if __name__ == "__main__":
    if len(sys.argv) != 2:
        printhelp()

    configpath = sys.argv[1]
    
    if not os.path.exists(configpath):
        printhelp()
    with open(configpath, "r") as f:
        js = json.load(f)

    wavpath = js["wav"]
    if not os.path.exists(wavpath):
        printhelp()
    
    data, samplerate = readwavefile(wavpath)
    deltatime = 1. / samplerate
    totaltimes = deltatime * len(data)

    specgram = spectrogram(js, data)

    plot.imshow(specgram.T, extent=[0, totaltimes, 0, samplerate], aspect="auto")
    plot.xlabel("-> times")
    plot.ylabel("-> frequency [Hz]")
    plot.colorbar()
    plot.tight_layout()
    plot.show()
    