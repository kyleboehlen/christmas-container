import utilities.input as inputReader
import importlib

day = input("What day would you like to run? ")

input = inputReader.openInput(day)

s = importlib.import_module("scripts." + day)

s.solvePuzzle(input)