import numpy as np
def read_file(filename):
    f = open(filename, "r")
    return f.read()


def split_file(data):
    Array = list(map(int,data.split()))
    return Array[0], Array[1], Array[2:]

