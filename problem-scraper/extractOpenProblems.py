import re

from src.scraper import matcher
import sys

def main():
    print("Output file " + sys.argv[1])
    with open(sys.argv[1], 'w') as output:
        print("Process files " + ", ".join(sys.argv[2:]))
        problems = matcher.findOpenProblemsMultiple(sys.argv[2:])
        matcher.toJSON(output, problems)

if __name__ == "__main__":
    main()
