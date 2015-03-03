# -*- coding: utf-8 -*-
"""
    defines the RedBarrel DSL.

    :copyright: Copyright 2011 by the RedBarrel team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
import ply.lex as lex
import ply.yacc as yacc
from pprint import pprint
import sys
import os

#
# Lex
#
reserved = {
    'path': 'PATH',
    'meta': 'META',
    'worker': 'WORKER',
    'arbiter': 'ARBITER',
    'unless': 'UNLESS',
    'validates': 'VALIDATES',
    'with': 'WITH',
    'not': 'NOT',
    'is': 'IS',
    'on': 'ON',
    'error': 'ERROR',
    'return': 'RETURN',
    'type': 'TYPE',
    'set': 'SET',
    'alter': 'ALTER',
    'describe': 'DESCRIBE',
    'description': 'DESCRIPTION',
    'global': 'GLOBAL',
    'root': 'ROOT'}


tokens = ['DOTTED_NAME', 'PREFIXED_NAME', 'NAME', 'LP', 'RP', 'COMMA', 'CODE',
          'INT', 'FILE', 'DIRECTORY', 'FLOAT', 'METHOD', 'VERB', 'URL',
          'URLVALUE', 'TEXT', 'SEMI', 'PROXY', 'PIPE'] + reserved.values()

literals = ''


def t_FILE(t):
    r'file:[a-zA-Z0-9_\./\\]*'
    return t


def t_DIRECTORY(t):
    r'directory:[a-zA-Z0-9_\./\\]*'
    return t


def t_DOTTED_NAME(t):
    r'([a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)+)+'
    return t


def t_PREFIXED_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*:([a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)+)+'  # NOQA
    return t


# will do better later -- more chars allowed
def t_PROXY(t):
    r'proxy:(http|https):\/\/[a-zA-Z0-9_:~\-]*'  # NOQA
    return t


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_\-]*'
    if t.value in VERBS:
        t.type = 'VERB'
    else:
        t.type = reserved.get(t.value, 'NAME')
    return t


def t_CODE(t):
    r'\d\d\d'
    t.value = int(t.value)
    return t


def t_TEXT(t):
    r'(?ms)("""(.*?)""")|(\"([^\\\n]|(\\.))*?\")'
    if t.value.startswith('"""'):
        t.value = t.value[3:-3]
    else:
        t.value = t.value[1:-1]
    return t


t_PIPE = r'\|'
t_SEMI = r';'
t_URL = r'url'
t_URLVALUE = r'/[a-zA-Z0-9\.~\{\}:\[\]+\-_/\*\$\(\)\?\<\>]*'  # incomplete
t_METHOD = r'method'
t_COMMA = r','
t_LP = r'\('
t_RP = r'\)'
t_INT = r'\d+'
t_FLOAT = r'\d+\.\d+'
t_ignore = " \t"
t_ignore_COMMENT = r'\#.*?$'


VERBS = ('POST', 'GET', 'DELETE', 'PUT', 'HEAD', 'TRACE',
         'OPTIONS', 'CONNECT')


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    raise SyntaxError("%r, line %d" % (t.value[0], t.lineno))
    #t.lexer.skip(1)


#
# Yacc
#
def p_program(p):
    """program : definitions
    """
    p[0] = p[1]


def p_path_definitions(p):
    """definitions :
                   | definitions definition
    """
    if len(p) == 1:
        p[0] = list()
    else:
        p[1].append(p[2])
        p[0] = p[1]


def p_path_definition(p):
    """definition : PATH NAME LP statements RP SEMI
                  | META LP statements RP SEMI
                  | GLOBAL NAME value SEMI
                  | TYPE NAME PREFIXED_NAME SEMI
                  | WORKER NAME PREFIXED_NAME SEMI
                  | ARBITER NAME PREFIXED_NAME SEMI
                  | ROOT URLVALUE SEMI
    """
    if p[1] == 'meta':
        p[0] = ('meta', p[3])
    elif p[1] in ('global', 'type', 'worker', 'arbiter'):
        p[0] = (p[1], p[2], p[3])
    elif p[1] == 'socket':
        p[0] = ('socket', p[2])
    elif p[1] == 'root':
        p[0] = ('root', p[2])
    else:
        p[0] = ('def', p[2], p[4])


def p_statements(p):
    """statements : statements COMMA statement
                  | statements COMMA
                  | statement
    """
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        p[0] = p[1]
    else:
        p[0] = p[1] + [p[3]]


def p_values(p):
    """values : value
              | values COMMA value
              | values COMMA
    """
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        p[0] = p[1]
    else:
        p[0] = p[1] + [p[3]]


def p_command(p):
    """command : UNLESS TYPE  IS        NAME RETURN      CODE
               | UNLESS TYPE  IS        NOT  NAME        RETURN CODE
               | UNLESS NAME  TYPE      IS   NAME        RETURN CODE
               | UNLESS NAME  TYPE      IS   NOT         NAME   RETURN CODE
               | UNLESS NAME  VALIDATES WITH NAME        RETURN CODE
               | UNLESS NAME  VALIDATES WITH PREFIXED_NAME RETURN CODE
               | ON     ERROR RETURN    CODE
               | SET    NAME  value
               | DESCRIBE CODE TEXT
               | DESCRIPTION TEXT
               | ALTER  WITH PREFIXED_NAME
    """
    if len(p) == 7:
        p[0] = ('check_type', p[4], p[6])
    elif len(p) == 8 and p[2] != 'type':
        if p[3] == 'type':
            op = 'check_type'
        else:
            op = 'validates_with'
        p[0] = (op, p[2], p[5], p[7])
    elif len(p) == 5:
        p[0] = ('onerror', p[4])
    elif len(p) == 9:
        p[0] = ('check_not_type', p[2], p[6], p[8])
    elif len(p) == 4:
        if p[1] == 'describe':
            p[0] = (p[1], p[2], p[3])
        elif p[1] == 'alter':
            p[0] = (p[1], p[3])
        else:
            p[0] = ('assign', p[2], p[3])
    elif len(p) == 3:
        p[0] = (p[1], p[2])


def p_verbs(p):
    """verbs : VERB
             | verbs PIPE VERB
    """
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]


def p_value(p):
    """value : command
             | INT
             | FLOAT
             | verbs
             | URLVALUE
             | TEXT
             | FILE
             | DIRECTORY
             | PROXY
             | DOTTED_NAME
             | PREFIXED_NAME
    """
    p[0] = ('val', p[1])


# do we want to define those ?
def p_variable(p):
    """variable : METHOD
                | URL
                | NAME
    """
    p[0] = ('var', p[1])


def p_statement(p):
    """statement : variable LP values RP
                 | variable value
                 | DESCRIPTION TEXT
    """
    if p[2] == '(':
        p[0] = ('assign', p[1], p[3])
    else:
        p[0] = ('assign', p[1], p[2])


def p_error(t):
    if t is None:
        # eof
        raise SyntaxError('Could not read the file.')
    else:
        raise SyntaxError("%r, line %d" % (t.value, t.lineno))

lex.lex()
yacc.yacc()


def build_ast(path, debug=False):
    if os.path.exists(path):
        with open(path) as f:
            data = f.read()
    else:
        data = path
    return yacc.parse(data, debug=debug)


if __name__ == '__main__':
    pprint(build_ast(sys.argv[1]))
