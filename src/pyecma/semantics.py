from pyecma import parser
from pyecma import elements


class EcmaSemantics(parser.EcmaSemantics):

    def L_WS(self, ast):
        return None

    def P_S_OPER_DELI(self, ast):
        return None

    def P_E_OPER_DELI(self, ast):
        return None

    def T_NUMBER(self, ast):
        return elements.Number(ast)

    def expression(self, ast):
        return elements.Expression(ast)

    def factor(self, ast):
        return ast

    def term(self, ast):
        f, s = ast
        if len(s):
            return ast
        return f

    def group(self, ast):
        return ast

    def P_PLUS(self, ast):
        return elements.Operator(lambda x,y: x+y, '+')

    def P_MINUS(self, ast):
        return elements.Operator(lambda x,y: x-y, '-')

    def P_MULTIPLY(self, ast):
        return elements.Operator(lambda x,y: x*y, '*')

    def P_DIVIDE(self, ast):
        return elements.Operator(lambda x,y: x/y, '/')
