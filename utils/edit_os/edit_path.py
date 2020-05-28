import os


def get_updir(num, path):
    for i in range(num):
        path = os.path.dirname(path)
    return path
