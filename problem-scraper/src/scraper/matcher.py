import re

from dataclasses import dataclass
from . import patterns

@dataclass
class Conjecture:
    label: str
    text: str

@dataclass
class OpenProblem:
    title: str
    label: str
    tags: str
    description: str

def findConjectures(filename: str):
    print(filename)
    with open(filename, "r") as file:
        content = file.read()
        matches = re.finditer(patterns.conjecture, content)
        for match in matches:
            conj = Conjecture(None if match.group(2) is None else match.group(2).strip(),
                              None if match.group(3) is None else match.group(3).strip())
            print(conj)

def findOpenProblems(filename: str):
    with open(filename, "r") as file:
        content = file.read()
        matches = re.finditer(patterns.openproblem, content)
        for match in matches:
            problem = OpenProblem(match.group(1).strip(), match.group(2).strip(),
                                  match.group(3).strip(), match.group(4).strip())
            yield problem

def printOpenProblems(filename: str):
    for problem in findOpenProblems(filename):
        print(problem)
