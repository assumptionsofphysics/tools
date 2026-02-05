import re

from dataclasses import dataclass
from . import patterns
import yaml

@dataclass
class Conjecture:
    label: str
    text: str

@dataclass
class OpenProblem:
    Title: str
    Label: str
    Tags: []
    Description: str

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
                                  [item.strip() for item in match.group(3).strip().split(",")], match.group(4).strip())
            yield problem

def printOpenProblems(filename: str):
    for problem in findOpenProblems(filename):
        print(problem)

#def toYaml(outstream, problems):
#    print(yaml.dump_all(problems), file=outstream)
def toYaml(outstream, problems):
    data = [obj.__dict__ for obj in problems]
#    problemList = list()
#    for problem in problems:
#       problemList.append({'Title': problem.title, 'Label': problem.label, 'Tags': problem.tags, 'Description': problem.description})
    print(yaml.dump(data), file=outstream)