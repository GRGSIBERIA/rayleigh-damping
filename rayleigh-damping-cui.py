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
    zetaA = float(js["low zetaAmp"])
    zetaB = float(js["high damp"])

    oa = 2. * np.pi / fa
    ob = 2. * np.pi / fb
    under = oa**2. - ob**2.
    a = (2 * oa * ob * (oa * zetaB - ob * zetaA)) / under
    b = (2. * (oa * zetaA - ob * zetaB)) / under
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
