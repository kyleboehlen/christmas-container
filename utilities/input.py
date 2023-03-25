import os

def openInput(day):
    path = os.path.realpath(__file__)
    dir = os.path.dirname(path)
    dir = dir.replace('utilities', 'input/')
    
    with open(dir + day + ".txt", "r") as i:
        return i.read().splitlines()
    