from scraper import matcher
import io

def test_findOpenProblems():
        problemList = list(matcher.findOpenProblems("tests/scraper/latexsample1.tex"))
        assert len(problemList) == 1
        assert problemList[0].title == "Title"
        assert problemList[0].label == "label"
        assert problemList[0].category == "Category"
        assert problemList[0].tags == ["Tag1", "Tag2"]
        assert problemList[0].video == "VideoURL"
        assert problemList[0].description == "This is the description"

def test_findOpenProblemsMultiple():
        problemList = list(matcher.findOpenProblemsMultiple(["tests/scraper/latexsample1.tex","tests/scraper/latexsample2.tex"]))
        assert len(problemList) == 3
        assert problemList[0].title == "Title"
        assert problemList[0].label == "label"
        assert problemList[0].category == "Category"
        assert problemList[0].tags == ["Tag1", "Tag2"]
        assert problemList[0].video == "VideoURL"

def sampleProblems():
        problemList = [matcher.OpenProblem("Title1", "label1", "Category", ["Tag1", "Tag2"], "VideoURL", "First description"),
                       matcher.OpenProblem("Title2", "label2", "Cat", ["Tag1", "Tag3"], "", "Second description")]
        for problem in problemList:
                yield problem

def test_toYaml():
        output = io.StringIO()
        matcher.toYaml(output, sampleProblems())
        output.seek(0)
        assert output.read() == """- category: Category
  description: First description
  label: label1
  tags:
  - Tag1
  - Tag2
  title: Title1
  video: VideoURL
- category: Cat
  description: Second description
  label: label2
  tags:
  - Tag1
  - Tag3
  title: Title2
  video: ''

"""


def test_toJSON():
        output = io.StringIO()
        matcher.toJSON(output, sampleProblems())
        output.seek(0)
        assert output.read() == """[{"title": "Title1", "label": "label1", "category": "Category", "tags": ["Tag1", "Tag2"], "video": "VideoURL", "description": "First description"}, {"title": "Title2", "label": "label2", "category": "Cat", "tags": ["Tag1", "Tag3"], "video": "", "description": "Second description"}]
"""
