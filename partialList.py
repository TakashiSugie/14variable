import numpy as np


class variable:
    def __init__(self, count=0, keyList=None):
        if count == 0:
            self.paraDict = {}
            for key in keyList:
                self.paraDict[key] = 0
            intrisicList = ["F", "Cx", "Cy"]
            for intrinsicKey in intrisicList:
                self.paraDict[intrinsicKey] = 0


def main():

    differentialDict = {}
    keyList = [
        "sz",
        "sz'",
        "theta_x",
        "theta_y",
        "theta_z",
        "theta_x'",
        "theta_y'",
        "theta_z'",
        "tx",
        "ty",
        "tz",
        "tx'",
        "ty'",
        "tz'",
    ]

    var = variable(count=0, keyList=keyList)
    print(type(var.paraDict))
    print(var.paraDict)
    # equList = []
    for key in keyList:
        differentialDict[key] = 0


main()
