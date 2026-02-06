from scraper import matcher
import io

def test_findOpenProblems():
        problemList = list(matcher.findOpenProblems("tests/scraper/latexsample1.tex"))
        assert len(problemList) == 1
        assert problemList[0].Title == "Title"
        assert problemList[0].Label == "label"
        assert problemList[0].Tags == ["Tag1", "Tag2"]
        assert problemList[0].Description == "This is the description"

def sampleProblems():
        problemList = [matcher.OpenProblem("Title1", "label1", ["Tag1", "Tag2"], "First description"),
                       matcher.OpenProblem("Title2", "label2", ["Tag1", "Tag3"], "Second description")]
        for problem in problemList:
                yield problem

def test_toYaml():
        output = io.StringIO()
        matcher.toYaml(output, sampleProblems())
        output.seek(0)
        assert output.read() == """- Description: First description
  Label: label1
  Tags:
  - Tag1
  - Tag2
  Title: Title1
- Description: Second description
  Label: label2
  Tags:
  - Tag1
  - Tag3
  Title: Title2

"""


def test_toJSON():
        output = io.StringIO()
        matcher.toJSON(output, sampleProblems())
        output.seek(0)
        assert output.read() == """[{"Title": "Title1", "Label": "label1", "Tags": ["Tag1", "Tag2"], "Description": "First description"}, {"Title": "Title2", "Label": "label2", "Tags": ["Tag1", "Tag3"], "Description": "Second description"}]
"""
