from pyecma.semantics import EcmaSemantics
from pyecma.parser import EcmaParser



def parse(ecmacode, filepath=None):
    parser = EcmaParser()
    return parser.parse(ecmacode, 'program', filename=filepath, semantics=EcmaSemantics())


def open(filepath):
    with open(filepath) as f:
        ecmacode = f.read()
    return parse(ecmacode, filepath)


def eval(ecmacode):
    return parser.parse(ecmacode, 'expression', filename=filepath, semantics=EcmaSemantics())