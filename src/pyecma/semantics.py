from pyecma import types
from pyecma import parser
from pyecma import elements


class EcmaSemantics(parser.EcmaSemantics):

    def expression(self, ast):
        return elements.Expression(ast.cal, ast.comp)

    def calculation(self, ast):
        return elements.Calculation(ast)

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
        return elements.Statement(ast.var, ast.oper, ast.ex)

    def break_statement(self, ast):
        return elements.BreakStatement()
    
    def return_statement(self, ast):
        return elements.ReturnStatement(ast.ex)

    def ifstatement(self, ast):
        else_ = None
        if ast.else_:
            else_ = ast.else_.else_
        return elements.IfStatement(ast.ex, ast.if_, else_)
    
    def whilestatement(self, ast):
        return elements.WhileStatement(ast.ex, ast.code)

    def dowhilestatement(self, ast):
        return elements.DoWhileStatement(ast.ex, ast.code)

    def program(self, ast):
        return elements.Program(ast)

    def function(self, ast):
        return elements.Function(ast)

    def function_classic(self, ast):
        ast.name.create = True
        return ast

    def callable(self, ast):
        if len(ast.params) == 2:
            params = ast.params[1] + [ast.params[0]]
        else:
            params = ast.params
        return elements.Callable(ast.name, params)


    def code_block(self, ast):
        return elements.CodeBlock(ast)

    def code_singleline(self, ast):
        if isinstance(ast, elements.CodeBlock):
            return ast
        return elements.CodeBlock([ast])
        

    def variable_create(self, ast):
        ast.create = True
        return ast

    def L_VARIABLE(self, ast):
        return elements.Variable(ast)

    def L_WS(self, ast):
        return None

    def P_S_OPER_DELI(self, ast):
        return None

    def P_E_OPER_DELI(self, ast):
        return None

    def T_NUMBER(self, ast):
        return types.Number(ast)

    def T_STRING(self, ast):
        trim = ast[:-1][1:]
        trim = trim.replace(r"\'", "'")
        trim = trim.replace(r'\"', '"')
        return types.String(trim)

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
        return elements.AssignSimple()

    def P_ASSIGN_PLUS(self, ast):
        return elements.Assign(lambda x,y: x+y, '+')

    def P_ASSIGN_MINUS(self, ast):
        return elements.Assign(lambda x,y: x-y, '-')

    def P_ASSIGN_MULTIPLY(self, ast):
        return elements.Assign(lambda x,y: x*y, '*')

    def P_ASSIGN_DIVIDE(self, ast):
        return elements.Assign(lambda x,y: x/y, '/')

    def P_ASSIGN_MODULO(self, ast):
        return elements.Assign(lambda x,y: x%y, '%')

    def P_ASSIGN_BITWISE_LEFT(self, ast):
        return elements.Assign(lambda x,y: x<<y, '<<', True)

    def P_ASSIGN_BITWISE_RIGHT(self, ast):
        return elements.Assign(lambda x,y: x>>y, '>>', True)

    def P_ASSIGN_BITWISE_RIGHT_UNSIG(self, ast):
        return elements.Assign(lambda x,y: (2**32-x) >> y, '>>>', True)

    def P_ASSIGN_BITWISE_AND(self, ast):
        return elements.Assign(lambda x,y: x&y, '&', True)

    def P_ASSIGN_BITWISE_OR(self, ast):
        return elements.Assign(lambda x,y: x|y, '|', True)

    def P_ASSIGN_BITWISE_XOR(self, ast):
        return elements.Assign(lambda x,y: x^y, '^', True)

    def P_LT(self, ast):
        return elements.Compare(lambda x,y: x<y, '<')

    def P_GT(self, ast):
        return elements.Compare(lambda x,y: x>y, '>')

    def P_LTE(self, ast):
        return elements.Compare(lambda x,y: x<=y, '<=')

    def P_GTE(self, ast):
        return elements.Compare(lambda x,y: x>=y, '>=')

    def P_EQUAL(self, ast):
        return elements.Compare(lambda x,y: x==y, '==')

    def P_NOT_EQUAL(self, ast):
        return elements.Compare(lambda x,y: x!=y, '!=')

    def P_E_EQUAL(self, ast):
        return elements.Compare(lambda x,y: x==y, '===', True)

    def P_E_NOT_EQUAL(self, ast):
        return elements.Compare(lambda x,y: x!=y, '!==', True)

