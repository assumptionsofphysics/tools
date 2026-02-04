from scraper import matcher

def test_findOpenProblems():
        problemList = list(matcher.findOpenProblems("tests/scraper/latexsample1.tex"))
        assert len(problemList) == 1
        assert problemList[0].title == "Title"
        assert problemList[0].label == "label"
        assert problemList[0].tags == "Tag1, Tag2"
        assert problemList[0].description == "This is the description"
