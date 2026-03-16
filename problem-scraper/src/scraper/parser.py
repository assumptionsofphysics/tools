import re

from dataclasses import dataclass
from . import patterns
from pathlib import Path
import yaml
import json


@dataclass
class TechnicalBrief:
    filename: str
    title: str
    author: str
    abstract: str
    category: str
    tags: list
    video: str

    titlePattern = r"\\title{(.*)?}"
    authorPattern = r"\\author{(.*)?}"
    abstractPattern = r"\\begin{abstract}([\s\S]*?)\\end{abstract}"
    categoryPattern = r"\\category{(.*)?}"
    tagsPattern = r"\\tags{(.*)?}"
    videoPattern = r"\\video{(.*)?}"


def matchTechnicalBrief(path: str):
    p = Path(path)
    filename = p.stem
    with open(path, "r", encoding='utf-8') as file:
        content = file.read()
        titleMatch = re.search(TechnicalBrief.titlePattern, content)
        authorMatch = re.search(TechnicalBrief.authorPattern, content)
        abstractMatch = re.search(TechnicalBrief.abstractPattern, content)
        categoryMatch = re.search(TechnicalBrief.categoryPattern, content)
        tagsMatch = re.search(TechnicalBrief.tagsPattern, content)
        videoMatch = re.search(TechnicalBrief.videoPattern, content)
        return TechnicalBrief(filename, titleMatch and titleMatch.group(1).strip(), authorMatch and authorMatch.group(1).strip(), 
                            abstractMatch and abstractMatch.group(1).strip(), categoryMatch and categoryMatch.group(1).strip(), 
                            [item.strip() for item in tagsMatch.group(1).strip().split(",")] if tagsMatch else [], videoMatch and videoMatch.group(1).strip())
