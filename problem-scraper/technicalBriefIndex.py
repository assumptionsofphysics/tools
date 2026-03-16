import re
import glob

from src.scraper import matcher
from src.scraper import parser
import sys
import json


def main():
    outputFile = sys.argv[1]
    articlePattern = sys.argv[2]
    print("Output file " + outputFile)
    briefs = []
    with open(outputFile, 'w') as output:
        for pattern in sys.argv[2:]:
            print("Processing pattern " + pattern)
            for filename in glob.glob(pattern):
                print(f'Processing {filename}')
                briefs.append(parser.matchTechnicalBrief(filename))
        data = [obj.__dict__ for obj in briefs]
        print(json.dumps(data), file=output)

if __name__ == "__main__":
    main()
