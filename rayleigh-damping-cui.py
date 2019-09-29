import os.path
import sys
import json
import numpy as np


def printhelp():
    print("python rayleigh-damping-cui.py [configure json file]")
    sys.exit()


def computerayreigh(js):
    fa = float(js["low freq"])
    fb = float(js["high freq"])
    da = float(js["low damp"])
    db = float(js["high damp"])

    oa = 2. * np.pi / fa
    ob = 2. * np.pi / fb
    under = ob**2. - oa**2.
    a = (2. * oa * ob * (da * ob - db * oa)) / under
    b = (2. * (db * ob - da * oa)) / under
    return (a, b)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        printhelp()
    
    confpath = sys.argv[1]
    if not os.path.exists(confpath):
        printhelp()
    
    with open(confpath, "r") as f:
        js = json.load(f)
    
    print("low  freq: ", js["low freq"])
    print("high freq: ", js["high freq"])
    print("low  damp: ", js["low damp"])
    print("high damp: ", js["high damp"])

    alpha, beta = computerayreigh(js)
    print("alpha : ", alpha)
    print("beta  : ", beta)
