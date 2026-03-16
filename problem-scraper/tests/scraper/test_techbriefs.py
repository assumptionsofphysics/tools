from scraper import parser
import io

def test_matchTechBrief1():
        brief = parser.matchTechnicalBrief("tests/scraper/techbrief1.tex")
        assert brief.title == "Directional vectors vs quantum state vectors"
        assert brief.author == "Gabriele Carcassi"
        assert brief.abstract == """We show why a direction in physical space is represented by a vector for the form $\\cos \\varphi \\sin \\theta e_x + \\sin \\varphi \\sin \\theta e_y + \\cos \\theta e_z$ while the state vector for a qubit, which also corresponds to a direction in physical space, is of the form $\\cos \\frac{\\theta}{2} e^{-\\imath \\frac{\\varphi}{2}} | z^+ \\> + \\sin \\frac{\\theta}{2} e^{\\imath \\frac{\\varphi}{2}} | z^+ \\>$."""
        assert brief.category == "Quantum mechanics"
        assert brief.tags == ["Superposition", "Projective geometry"]
        assert brief.video == None

def test_matchTechBrief2():
        brief = parser.matchTechnicalBrief("tests/scraper/techbrief2.tex")
        assert brief.title == None
        assert brief.author == None
        assert brief.abstract == None
        assert brief.category == None
        assert brief.tags == []
        assert brief.video == None

def test_matchTechBrief3():
        brief = parser.matchTechnicalBrief("tests/scraper/techbrief3.tex")
        assert brief.title == "Directional vectors vs quantum state vectors"
        assert brief.author == "Gabriele Carcassi"
        assert brief.abstract == """We show why a direction in physical space is represented by a vector for the form $\\cos \\varphi \\sin \\theta e_x + \\sin \\varphi \\sin \\theta e_y + \\cos \\theta e_z$ while the state vector for a qubit, which also corresponds to a direction in physical space, is of the form $\\cos \\frac{\\theta}{2} e^{-\\imath \\frac{\\varphi}{2}} | z^+ \\> + \\sin \\frac{\\theta}{2} e^{\\imath \\frac{\\varphi}{2}} | z^+ \\>$."""
        assert brief.category == "Quantum mechanics"
        assert brief.tags == ["Superposition", "Projective geometry"]
        assert brief.video == "https://youtube.com/lskdnfei"
