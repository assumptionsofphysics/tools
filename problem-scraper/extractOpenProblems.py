import re

from src.scraper import matcher
import sys

def main():
    print("Output file " + sys.argv[1])
    with open(sys.argv[1], 'w') as output:
        for filename in sys.argv[2:]:
            print("Process file " + filename)
            problems = matcher.findOpenProblems(filename)
            matcher.toYaml(output, problems)

if __name__ == "__main__":
    main()
