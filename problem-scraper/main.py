import re

from src.scraper import matcher

def main():
    problems = matcher.findOpenProblems("tests/scraper/latexsample2.tex")
    with open('test.json', 'w') as file:
        matcher.toJSON(file, problems)



if __name__ == "__main__":
    main()
