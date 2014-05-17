from pyecma.semantics import EcmaSemantics
from pyecma.parser import EcmaParser


COMMENT_REGEX=r'\/\/.*$|\/\*(?:[^*]|[\r\n]|(?:\*+(?:[^*/]|[\r\n])))*\*+\/'

def parse(ecmacode, filepath=None):
    parser = EcmaParser()
    return parser.parse(ecmacode, 'program', filename=filepath,
                        semantics=EcmaSemantics(), comments_re=COMMENT_REGEX)


def open(filepath):
    with open(filepath) as f:
        ecmacode = f.read()
    return parse(ecmacode, filepath)


def eval(ecmacode):
    parser = EcmaParser()
    return parser.parse(ecmacode, 'expression', filename=None,
                        semantics=EcmaSemantics(), comments_re=COMMENT_REGEX)()
