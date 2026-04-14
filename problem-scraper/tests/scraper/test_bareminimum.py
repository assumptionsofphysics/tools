from scraper import parser
import io

def test_matchBareMinimum1():
        brief = parser.matchBareMinimum("tests/scraper/bareminimum1.tex")
        assert brief.filename == "bareminimum1"
        assert brief.topic == "Set Theory"
        assert brief.category == "Mathematics"
        assert brief.tags == ["Foundations of Mathematics", "Set Theory"]
        assert brief.video == None

def test_matchBareMinimum2():
        brief = parser.matchBareMinimum("tests/scraper/bareminimum2.tex")
        assert brief.filename == "bareminimum2"
        assert brief.topic == None
        assert brief.category == None
        assert brief.tags == []
        assert brief.video == None

def test_matchBareMinimum3():
        brief = parser.matchBareMinimum("tests/scraper/bareminimum3.tex")
        assert brief.filename == "bareminimum3"
        assert brief.topic == "Set Theory"
        assert brief.category == "Mathematics"
        assert brief.tags == ["Foundations of Mathematics", "Set Theory"]
        assert brief.video == "https://youtube.com/lskdnfei"
