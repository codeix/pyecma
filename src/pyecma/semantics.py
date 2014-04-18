from pyecma import parser
from pyecma import elements


class EcmaSemantics(parser.EcmaSemantics):

    def expression(self, ast):
        return elements.Expression(ast)

    def factor(self, ast):
        return ast

    def term(self, ast):
        f, s = ast
        if len(s):
            return ast
        return f

    def statement(self, ast):
        if isinstance(ast, elements.Expression):
            return elements.Statement(None, None, ast)
        return elements.Statement(ast['var'], ast['oper'], ast['ex'])

    def program(self, ast):
        return elements.Program(ast)

    def function(self, ast):
        return elements.Function(ast)

    def code_block(self, ast):
        return elements.CodeBlock(ast)

    def L_VARIABLE(self, ast):
        return elements.Variable(ast)

    def L_WS(self, ast):
        return None

    def P_S_OPER_DELI(self, ast):
        return None

    def P_E_OPER_DELI(self, ast):
        return None

    def T_NUMBER(self, ast):
        return elements.Number(ast)

    def P_STAT_TERMINATOR(self, ast):
        return None
    
    def K_VAR(self, ast):
        return None

    def P_SCB(self, ast):
        return None

    def P_ECB(self, ast):
        return None

    def P_ARGS_DELIMITER(self, ast):
        return None

    def P_PLUS(self, ast):
        return elements.Operator(lambda x,y: x+y, '+')

    def P_MINUS(self, ast):
        return elements.Operator(lambda x,y: x-y, '-')

    def P_MULTIPLY(self, ast):
        return elements.Operator(lambda x,y: x*y, '*')

    def P_DIVIDE(self, ast):
        return elements.Operator(lambda x,y: x/y, '/')

    def P_ASSIGN(self, ast):
        return elements.Operator(lambda x,y: y, '=')

    def P_ASSIGN_PLUS(self, ast):
        return elements.Operator(lambda x,y: x+y, '+')

    def P_ASSIGN_MINUS(self, ast):
        return elements.Operator(lambda x,y: x-y, '-')

    def P_ASSIGN_MULTIPLY(self, ast):
        return elements.Operator(lambda x,y: x*y, '*')

    def P_ASSIGN_DIVIDE(self, ast):
        return elements.Operator(lambda x,y: x/y, '/')

    def P_ASSIGN_MODULO(self, ast):
        return elements.Operator(lambda x,y: x%y, '%')

    def P_ASSIGN_BITWISE_LEFT(self, ast):
        return elements.Operator(lambda x,y: x<<y, '<<')

    def P_ASSIGN_BITWISE_RIGHT(self, ast):
        return elements.Operator(lambda x,y: x>>y, '>>')

    def P_ASSIGN_BITWISE_RIGHT_UNSIG(self, ast):
        return elements.Operator(lambda x,y: (2**32-x) >> y, '>>>')

    def P_ASSIGN_BITWISE_AND(self, ast):
        return elements.Operator(lambda x,y: x&y, '&')

    def P_ASSIGN_BITWISE_OR(self, ast):
        return elements.Operator(lambda x,y: x|y, '|')

    def P_ASSIGN_BITWISE_XOR(self, ast):
        return elements.Operator(lambda x,y: x^y, '^')

