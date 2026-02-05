import re

from src.scraper import matcher

def main():
    problems = matcher.findOpenProblems("tests/scraper/latexsample2.tex")
    with open('test.yaml', 'w') as file:
        matcher.toYaml(file, problems)



if __name__ == "__main__":
    main()
