#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# CAVEAT UTILITOR
# This file was automatically generated by Grako.
#    https://bitbucket.org/apalala/grako/
# Any changes you make to it will be overwritten the
# next time the file is generated.
#

from __future__ import print_function, division, absolute_import, unicode_literals
from grako.parsing import * # @UnusedWildImport
from grako.exceptions import * # @UnusedWildImport

__version__ = '14.108.17.04.48'

class EcmaParser(Parser):
    def __init__(self, whitespace=None, nameguard=True, **kwargs):
        super(EcmaParser, self).__init__(whitespace=whitespace,
            nameguard=nameguard, **kwargs)

    @rule_def
    def _K_BREAK_(self):
        with self._group():
            self._pattern(r'break')

    @rule_def
    def _K_DO_(self):
        with self._group():
            self._pattern(r'do')

    @rule_def
    def _K_INSTANCEOF_(self):
        with self._group():
            self._pattern(r'instanceof')

    @rule_def
    def _K_TYPEOF_(self):
        with self._group():
            self._pattern(r'typeof')

    @rule_def
    def _K_CASE_(self):
        with self._group():
            self._pattern(r'case')

    @rule_def
    def _K_ELSE_(self):
        with self._group():
            self._pattern(r'else')

    @rule_def
    def _K_NEW_(self):
        with self._group():
            self._pattern(r'new')

    @rule_def
    def _K_VAR_(self):
        with self._group():
            self._pattern(r'var')

    @rule_def
    def _K_CATCH_(self):
        with self._group():
            self._pattern(r'catch')

    @rule_def
    def _K_FINALLLY_(self):
        with self._group():
            self._pattern(r'finally')

    @rule_def
    def _K_RETURN_(self):
        with self._group():
            self._pattern(r'return')

    @rule_def
    def _K_VOID_(self):
        with self._group():
            self._pattern(r'void')

    @rule_def
    def _K_CONTINUE_(self):
        with self._group():
            self._pattern(r'continue')

    @rule_def
    def _K_FOR_(self):
        with self._group():
            self._pattern(r'for')

    @rule_def
    def _K_SWITCH_(self):
        with self._group():
            self._pattern(r'switch')

    @rule_def
    def _K_WHILE_(self):
        with self._group():
            self._pattern(r'while')

    @rule_def
    def _K_DEBUGGER_(self):
        with self._group():
            self._pattern(r'debugger')

    @rule_def
    def _K_FUNCTION_(self):
        with self._group():
            self._pattern(r'function')

    @rule_def
    def _K_THIS_(self):
        with self._group():
            self._pattern(r'this')

    @rule_def
    def _K_WITH_(self):
        with self._group():
            self._pattern(r'with')

    @rule_def
    def _K_DEFAULT_(self):
        with self._group():
            self._pattern(r'default')

    @rule_def
    def _K_IF_(self):
        with self._group():
            self._pattern(r'if')

    @rule_def
    def _K_THROW_(self):
        with self._group():
            self._pattern(r'throw')

    @rule_def
    def _K_DELETE_(self):
        with self._group():
            self._pattern(r'delete')

    @rule_def
    def _K_IN_(self):
        with self._group():
            self._pattern(r'in')

    @rule_def
    def _K_TRY_(self):
        with self._group():
            self._pattern(r'try')

    @rule_def
    def _P_SCB_(self):
        with self._group():
            self._pattern(r'\{')

    @rule_def
    def _P_ECB_(self):
        with self._group():
            self._pattern(r'\}')

    @rule_def
    def _P_S_FUNC_DELI_(self):
        with self._group():
            self._pattern(r'\(')

    @rule_def
    def _P_E_FUNC_DELI_(self):
        with self._group():
            self._pattern(r'\)')

    @rule_def
    def _P_S_ARRAY_DELI_(self):
        with self._group():
            self._pattern(r'\[')

    @rule_def
    def _P_E_ARRAY_DELI_(self):
        with self._group():
            self._pattern(r'\]')

    @rule_def
    def _P_ACCESSOR_(self):
        with self._group():
            self._pattern(r'\.')

    @rule_def
    def _P_STAT_TERMINATOR_(self):
        with self._group():
            self._pattern(r';')

    @rule_def
    def _P_ARGS_DELIMITER_(self):
        with self._group():
            self._pattern(r',')

    @rule_def
    def _P_LT_(self):
        with self._group():
            self._pattern(r'<')

    @rule_def
    def _P_GT_(self):
        with self._group():
            self._pattern(r'>')

    @rule_def
    def _P_LTE_(self):
        with self._group():
            self._pattern(r'<=')

    @rule_def
    def _P_GTE_(self):
        with self._group():
            self._pattern(r'>=')

    @rule_def
    def _P_EQUAL_(self):
        with self._group():
            self._pattern(r'==')

    @rule_def
    def _P_NOT_EQUAL_(self):
        with self._group():
            self._pattern(r'!=')

    @rule_def
    def _P_E_EQUAL_(self):
        with self._group():
            self._pattern(r'===')

    @rule_def
    def _P_E_NOT_EQUAL_(self):
        with self._group():
            self._pattern(r'!==')

    @rule_def
    def _P_PLUS_(self):
        with self._group():
            self._pattern(r'\+')

    @rule_def
    def _P_MINUS_(self):
        with self._group():
            self._pattern(r'-')

    @rule_def
    def _P_MULTIPLY_(self):
        with self._group():
            self._pattern(r'\*')

    @rule_def
    def _P_DIVIDE_(self):
        with self._group():
            self._pattern(r'\/')

    @rule_def
    def _P_MODULO_(self):
        with self._group():
            self._pattern(r'%')

    @rule_def
    def _P_PLUS_INC_(self):
        with self._group():
            self._pattern(r'\+\+')

    @rule_def
    def _P_MINUS_INC_(self):
        with self._group():
            self._pattern(r'--')

    @rule_def
    def _P_BITWISE_LEFT_(self):
        with self._group():
            self._pattern(r'<<')

    @rule_def
    def _P_BITWISE_RIGHT_(self):
        with self._group():
            self._pattern(r'>>')

    @rule_def
    def _P_BITWISE_RIGHT_UNSIG_(self):
        with self._group():
            self._pattern(r'>>>')

    @rule_def
    def _P_BITWISE_AND_(self):
        with self._group():
            self._pattern(r'&')

    @rule_def
    def _P_BITWISE_OR_(self):
        with self._group():
            self._pattern(r'\|')

    @rule_def
    def _P_BITWISE_XOR_(self):
        with self._group():
            self._pattern(r'\^')

    @rule_def
    def _P_NOT_(self):
        with self._group():
            self._pattern(r'!')

    @rule_def
    def _P_BITWISE_NOT_(self):
        with self._group():
            self._pattern(r'~')

    @rule_def
    def _P_AND_(self):
        with self._group():
            self._pattern(r'&&')

    @rule_def
    def _P_OR_(self):
        with self._group():
            self._pattern(r'\|\|')

    @rule_def
    def _P_CONDITIONAL_OP_(self):
        with self._group():
            self._pattern(r'\(?')

    @rule_def
    def _P_PART_CONDITIONAL_OP_(self):
        with self._group():
            self._pattern(r':')

    @rule_def
    def _P_ASSIGN_(self):
        with self._group():
            self._pattern(r'=')

    @rule_def
    def _P_ASSIGN_PLUS_(self):
        with self._group():
            self._pattern(r'\+=')

    @rule_def
    def _P_ASSIGN_MINUS_(self):
        with self._group():
            self._pattern(r'-=')

    @rule_def
    def _P_ASSIGN_MULTIPLY_(self):
        with self._group():
            self._pattern(r'\*=')

    @rule_def
    def _P_ASSIGN_DIVIDE_(self):
        with self._group():
            self._pattern(r'\/=')

    @rule_def
    def _P_ASSIGN_MODULO_(self):
        with self._group():
            self._pattern(r'%=')

    @rule_def
    def _P_ASSIGN_BITWISE_LEFT_(self):
        with self._group():
            self._pattern(r'<<=')

    @rule_def
    def _P_ASSIGN_BITWISE_RIGHT_(self):
        with self._group():
            self._pattern(r'>>=')

    @rule_def
    def _P_ASSIGN_BITWISE_RIGHT_UNSIG_(self):
        with self._group():
            self._pattern(r'>>>=')

    @rule_def
    def _P_ASSIGN_BITWISE_AND_(self):
        with self._group():
            self._pattern(r'&=')

    @rule_def
    def _P_ASSIGN_BITWISE_OR_(self):
        with self._group():
            self._pattern(r'\|=')

    @rule_def
    def _P_ASSIGN_BITWISE_XOR_(self):
        with self._group():
            self._pattern(r'\^=')

    @rule_def
    def _L_WS_(self):
        self._pattern(r'(?:\s+)')

    @rule_def
    def _L_VARIABLE_(self):
        self._pattern(r'((?:[A-z]+[0-9]*)+)')

    @rule_def
    def _P_S_OPER_DELI_(self):
        with self._group():
            self._pattern(r'\(')

    @rule_def
    def _P_E_OPER_DELI_(self):
        with self._group():
            self._pattern(r'\)')

    @rule_def
    def _T_NUMBER_(self):
        self._pattern(r'[\+-]?[0-9]+(?:\.[0-9]*)?(?:[eE][-\+]?[0-9])?')

    @rule_def
    def _T_UNDEFINED_(self):
        self._pattern(r'undefined')

    @rule_def
    def _T_NULL_(self):
        self._pattern(r'null')

    @rule_def
    def _T_BOOL_(self):
        self._pattern(r'true|false')

    @rule_def
    def _T_STRING_(self):
        with self._choice():
            with self._option():
                self._pattern(r'".*"')
            with self._option():
                self._pattern(r"'.*'")
            self._error('expecting one of: \'.*\' ".*"')

    @rule_def
    def _OPERATORS_(self):
        with self._choice():
            with self._option():
                self._P_MINUS_()
            with self._option():
                self._P_PLUS_()
            with self._option():
                self._P_MULTIPLY_()
            with self._option():
                self._P_MODULO_()
            with self._option():
                self._P_DIVIDE_()
            with self._option():
                self._P_BITWISE_LEFT_()
            with self._option():
                self._P_BITWISE_RIGHT_()
            with self._option():
                self._P_BITWISE_RIGHT_UNSIG_()
            self._error('no available options')

    @rule_def
    def _ASSIGN_OPERATORS_(self):
        with self._choice():
            with self._option():
                self._P_ASSIGN_()
            with self._option():
                self._P_ASSIGN_PLUS_()
            with self._option():
                self._P_ASSIGN_MINUS_()
            with self._option():
                self._P_ASSIGN_MULTIPLY_()
            with self._option():
                self._P_ASSIGN_DIVIDE_()
            with self._option():
                self._P_ASSIGN_MODULO_()
            with self._option():
                self._P_ASSIGN_BITWISE_LEFT_()
            with self._option():
                self._P_ASSIGN_BITWISE_RIGHT_()
            with self._option():
                self._P_ASSIGN_BITWISE_RIGHT_UNSIG_()
            with self._option():
                self._P_ASSIGN_BITWISE_AND_()
            with self._option():
                self._P_ASSIGN_BITWISE_OR_()
            with self._option():
                self._P_ASSIGN_BITWISE_XOR_()
            self._error('no available options')

    @rule_def
    def _CREMENT_OPERATORS_(self):
        with self._choice():
            with self._option():
                self._P_PLUS_INC_()
            with self._option():
                self._P_MINUS_INC_()
            self._error('no available options')

    @rule_def
    def _COMPARE_OPERATORS_(self):
        with self._choice():
            with self._option():
                self._P_LT_()
            with self._option():
                self._P_GT_()
            with self._option():
                self._P_LTE_()
            with self._option():
                self._P_GTE_()
            with self._option():
                self._P_EQUAL_()
            with self._option():
                self._P_NOT_EQUAL_()
            with self._option():
                self._P_E_EQUAL_()
            with self._option():
                self._P_E_NOT_EQUAL_()
            self._error('no available options')

    @rule_def
    def _TYPES_(self):
        with self._choice():
            with self._option():
                self._T_NUMBER_()
            with self._option():
                self._T_UNDEFINED_()
            with self._option():
                self._T_NULL_()
            with self._option():
                self._T_BOOL_()
            with self._option():
                self._T_STRING_()
            with self._option():
                self._L_VARIABLE_()
            self._error('no available options')

    @rule_def
    def _expression_(self):
        self._term_()
        self._cut()
        def block0():
            with self._choice():
                with self._option():
                    with self._group():
                        self._P_PLUS_()
                        self._cut()
                        self._term_()
                with self._option():
                    with self._group():
                        self._P_MINUS_()
                        self._cut()
                        self._term_()
                self._error('no available options')
        self._closure(block0)

    @rule_def
    def _factor_(self):
        with self._choice():
            with self._option():
                with self._optional():
                    self._L_WS_()
                with self._group():
                    self._TYPES_()
                with self._optional():
                    self._L_WS_()
            with self._option():
                self._group_()
            self._error('no available options')

    @rule_def
    def _term_(self):
        self._factor_()
        self._cut()
        def block0():
            with self._choice():
                with self._option():
                    with self._group():
                        self._P_MULTIPLY_()
                        self._cut()
                        self._factor_()
                with self._option():
                    with self._group():
                        self._P_DIVIDE_()
                        self._cut()
                        self._factor_()
                self._error('no available options')
        self._closure(block0)

    @rule_def
    def _group_(self):
        self._P_S_OPER_DELI_()
        self._cut()
        self._expression_()
        self._cut()
        self._P_E_OPER_DELI_()

    @rule_def
    def _program_(self):
        def block0():
            with self._choice():
                with self._option():
                    self._function_()
                with self._option():
                    self._statement_()
                self._error('no available options')
        self._closure(block0)

    @rule_def
    def _assign_(self):
        with self._group():
            with self._choice():
                with self._option():
                    self._variable_create_()
                with self._option():
                    self._variable_set_()
                self._error('no available options')
        self.ast['var'] = self.last_node
        with self._optional():
            self._L_WS_()
        with self._group():
            self._ASSIGN_OPERATORS_()
        self.ast['oper'] = self.last_node
        with self._group():
            self._expression_()
        self.ast['ex'] = self.last_node
        with self._optional():
            self._L_WS_()
        self._P_STAT_TERMINATOR_()

    @rule_def
    def _statement_(self):
        with self._choice():
            with self._option():
                self._assign_()
            with self._option():
                with self._group():
                    self._expression_()
                    with self._optional():
                        self._L_WS_()
                    self._P_STAT_TERMINATOR_()
            self._error('no available options')

    @rule_def
    def _variable_create_(self):
        self._K_VAR_()
        self._L_WS_()
        self._L_VARIABLE_()
        with self._optional():
            self._L_WS_()

    @rule_def
    def _variable_set_(self):
        self._L_VARIABLE_()
        with self._optional():
            self._L_WS_()

    @rule_def
    def _code_block_(self):
        self._P_SCB_()
        with self._optional():
            self._L_WS_()
        def block0():
            with self._choice():
                with self._option():
                    self._return_statement_()
                with self._option():
                    self._statement_()
                self._error('no available options')
        self._closure(block0)
        with self._optional():
            self._L_WS_()
        self._P_ECB_()

    @rule_def
    def _return_statement_(self):
        self._K_RETURN_()
        with self._optional():
            self._L_WS_()
        with self._group():
            self._expression_()
            self.ast['ex'] = self.last_node
            with self._optional():
                self._L_WS_()
            self._P_STAT_TERMINATOR_()

    @rule_def
    def _arguments_(self):
        with self._group():
            with self._optional():
                self._L_WS_()
            def block0():
                self._L_VARIABLE_()
                with self._optional():
                    self._L_WS_()
                self._P_ARGS_DELIMITER_()
                with self._optional():
                    self._L_WS_()
            self._closure(block0)
            with self._optional():
                self._L_VARIABLE_()
            with self._optional():
                self._L_WS_()

    @rule_def
    def _function_(self):
        with self._choice():
            with self._option():
                self._function_classic_()
            with self._option():
                self._function_assign_()
            self._error('no available options')

    @rule_def
    def _function_classic_(self):
        self._K_FUNCTION_()
        with self._optional():
            self._L_WS_()
        self._L_VARIABLE_()
        self.ast['name'] = self.last_node
        self._function_body_()
        self.ast['body'] = self.last_node

    @rule_def
    def _function_assign_(self):
        with self._group():
            with self._choice():
                with self._option():
                    self._variable_create_()
                with self._option():
                    self._variable_set_()
                self._error('no available options')
        self.ast['name'] = self.last_node
        with self._optional():
            self._L_WS_()
        self._P_ASSIGN_()
        with self._optional():
            self._L_WS_()
        self._K_FUNCTION_()
        with self._optional():
            self._L_WS_()
        self._function_body_()
        self.ast['body'] = self.last_node

    @rule_def
    def _function_body_(self):
        with self._optional():
            self._L_WS_()
        self._P_S_FUNC_DELI_()
        with self._optional():
            self._L_WS_()
        self._arguments_()
        self.ast['sign'] = self.last_node
        with self._optional():
            self._L_WS_()
        self._P_E_FUNC_DELI_()
        with self._optional():
            self._L_WS_()
        self._code_block_()
        self.ast['code'] = self.last_node



class EcmaSemanticParser(CheckSemanticsMixin, EcmaParser):
    pass


class EcmaSemantics(object):
    def K_BREAK(self, ast):
        return ast

    def K_DO(self, ast):
        return ast

    def K_INSTANCEOF(self, ast):
        return ast

    def K_TYPEOF(self, ast):
        return ast

    def K_CASE(self, ast):
        return ast

    def K_ELSE(self, ast):
        return ast

    def K_NEW(self, ast):
        return ast

    def K_VAR(self, ast):
        return ast

    def K_CATCH(self, ast):
        return ast

    def K_FINALLLY(self, ast):
        return ast

    def K_RETURN(self, ast):
        return ast

    def K_VOID(self, ast):
        return ast

    def K_CONTINUE(self, ast):
        return ast

    def K_FOR(self, ast):
        return ast

    def K_SWITCH(self, ast):
        return ast

    def K_WHILE(self, ast):
        return ast

    def K_DEBUGGER(self, ast):
        return ast

    def K_FUNCTION(self, ast):
        return ast

    def K_THIS(self, ast):
        return ast

    def K_WITH(self, ast):
        return ast

    def K_DEFAULT(self, ast):
        return ast

    def K_IF(self, ast):
        return ast

    def K_THROW(self, ast):
        return ast

    def K_DELETE(self, ast):
        return ast

    def K_IN(self, ast):
        return ast

    def K_TRY(self, ast):
        return ast

    def P_SCB(self, ast):
        return ast

    def P_ECB(self, ast):
        return ast

    def P_S_FUNC_DELI(self, ast):
        return ast

    def P_E_FUNC_DELI(self, ast):
        return ast

    def P_S_ARRAY_DELI(self, ast):
        return ast

    def P_E_ARRAY_DELI(self, ast):
        return ast

    def P_ACCESSOR(self, ast):
        return ast

    def P_STAT_TERMINATOR(self, ast):
        return ast

    def P_ARGS_DELIMITER(self, ast):
        return ast

    def P_LT(self, ast):
        return ast

    def P_GT(self, ast):
        return ast

    def P_LTE(self, ast):
        return ast

    def P_GTE(self, ast):
        return ast

    def P_EQUAL(self, ast):
        return ast

    def P_NOT_EQUAL(self, ast):
        return ast

    def P_E_EQUAL(self, ast):
        return ast

    def P_E_NOT_EQUAL(self, ast):
        return ast

    def P_PLUS(self, ast):
        return ast

    def P_MINUS(self, ast):
        return ast

    def P_MULTIPLY(self, ast):
        return ast

    def P_DIVIDE(self, ast):
        return ast

    def P_MODULO(self, ast):
        return ast

    def P_PLUS_INC(self, ast):
        return ast

    def P_MINUS_INC(self, ast):
        return ast

    def P_BITWISE_LEFT(self, ast):
        return ast

    def P_BITWISE_RIGHT(self, ast):
        return ast

    def P_BITWISE_RIGHT_UNSIG(self, ast):
        return ast

    def P_BITWISE_AND(self, ast):
        return ast

    def P_BITWISE_OR(self, ast):
        return ast

    def P_BITWISE_XOR(self, ast):
        return ast

    def P_NOT(self, ast):
        return ast

    def P_BITWISE_NOT(self, ast):
        return ast

    def P_AND(self, ast):
        return ast

    def P_OR(self, ast):
        return ast

    def P_CONDITIONAL_OP(self, ast):
        return ast

    def P_PART_CONDITIONAL_OP(self, ast):
        return ast

    def P_ASSIGN(self, ast):
        return ast

    def P_ASSIGN_PLUS(self, ast):
        return ast

    def P_ASSIGN_MINUS(self, ast):
        return ast

    def P_ASSIGN_MULTIPLY(self, ast):
        return ast

    def P_ASSIGN_DIVIDE(self, ast):
        return ast

    def P_ASSIGN_MODULO(self, ast):
        return ast

    def P_ASSIGN_BITWISE_LEFT(self, ast):
        return ast

    def P_ASSIGN_BITWISE_RIGHT(self, ast):
        return ast

    def P_ASSIGN_BITWISE_RIGHT_UNSIG(self, ast):
        return ast

    def P_ASSIGN_BITWISE_AND(self, ast):
        return ast

    def P_ASSIGN_BITWISE_OR(self, ast):
        return ast

    def P_ASSIGN_BITWISE_XOR(self, ast):
        return ast

    def L_WS(self, ast):
        return ast

    def L_VARIABLE(self, ast):
        return ast

    def P_S_OPER_DELI(self, ast):
        return ast

    def P_E_OPER_DELI(self, ast):
        return ast

    def T_NUMBER(self, ast):
        return ast

    def T_UNDEFINED(self, ast):
        return ast

    def T_NULL(self, ast):
        return ast

    def T_BOOL(self, ast):
        return ast

    def T_STRING(self, ast):
        return ast

    def OPERATORS(self, ast):
        return ast

    def ASSIGN_OPERATORS(self, ast):
        return ast

    def CREMENT_OPERATORS(self, ast):
        return ast

    def COMPARE_OPERATORS(self, ast):
        return ast

    def TYPES(self, ast):
        return ast

    def expression(self, ast):
        return ast

    def factor(self, ast):
        return ast

    def term(self, ast):
        return ast

    def group(self, ast):
        return ast

    def program(self, ast):
        return ast

    def assign(self, ast):
        return ast

    def statement(self, ast):
        return ast

    def variable_create(self, ast):
        return ast

    def variable_set(self, ast):
        return ast

    def code_block(self, ast):
        return ast

    def return_statement(self, ast):
        return ast

    def arguments(self, ast):
        return ast

    def function(self, ast):
        return ast

    def function_classic(self, ast):
        return ast

    def function_assign(self, ast):
        return ast

    def function_body(self, ast):
        return ast

def main(filename, startrule, trace=False):
    import json
    with open(filename) as f:
        text = f.read()
    parser = EcmaParser(parseinfo=False)
    ast = parser.parse(text, startrule, filename=filename, trace=trace)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()

if __name__ == '__main__':
    import argparse
    import sys
    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in EcmaParser.rule_list():
                print(r)
            print()
            sys.exit(0)
    parser = argparse.ArgumentParser(description="Simple parser for Ecma.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")
    args = parser.parse_args()

    main(args.file, args.startrule, trace=args.trace)
