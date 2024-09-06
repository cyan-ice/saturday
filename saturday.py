__version__ = '0.0.1'

import os

from argparse import ArgumentParser, FileType
from sys import stderr, stdin, stdout
from operator import mul, add, sub, mod, and_, or_, xor, not_, inv
from fractions import Fraction
from math import factorial, ceil, trunc
from itertools import chain, tee
from re import sub as rsub
from io import StringIO

parser = ArgumentParser(
    description=f'Saturday {__version__}, the official saturday interpreter')
parser.add_argument('-d', '--debug', action='store_true', help='debug mode')
parser.add_argument('file', type=FileType(), help='path to source file')
args = parser.parse_args()

code: str = rsub(r'#.*[\n]?', '', args.file.read())

i = 0
st = []
ctx = []
loop_ctx = []
left = {}
loop_left = {}
cor = {}


def raise_exception(msg: str):
    print(msg, file=stderr)
    exit(1)


for j, c in enumerate(code):
    match c:
        case '(':
            ctx.append((j, c))
            loop_ctx.append(j)
        case '[':
            ctx.append((j, c))
    if ctx:
        left[j] = ctx[-1][0]
    if loop_ctx:
        loop_left[j] = loop_ctx[-1]
    match c:
        case ')':
            k, b = ctx.pop()
            if b == '[':
                raise_exception('Syntax Error: If Not Closed')
            loop_ctx.pop()
            cor[k] = j
        case ']':
            k, b = ctx.pop()
            if b == '(':
                raise_exception('Syntax Error: Loop Not Closed')
            cor[k] = j

if ctx:
    match ctx[-1][1]:
        case '(':
            raise_exception('Syntax Error: Loop Not Closed')
        case '[':
            raise_exception('Syntax Error: If Not Closed')


def stack_pop(n: int = 1):
    if len(st) < n:
        raise_exception('Invalid Operation: Not enough values on the stack')
    for _ in range(n):
        yield st.pop()


def operation(op, *args, **kwargs):
    try:
        result = op(*args, **kwargs)
        if isinstance(result, Fraction) and result.is_integer():
            result = int(result)
        return result
    except:
        raise_exception('Invalid Operation')


def loop_break():
    global i
    try:
        i = cor[loop_left[i]]
    except:
        raise_exception('Invalid Operation: Not in A Loop')


def loop_continue():
    global i
    try:
        i = loop_left[i]
    except:
        raise_exception('Invalid Operation: Not In A Loop')


def if_skip():
    global i
    i = cor[left[i]]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


dbgout = StringIO()

if args.debug:
    while i < len(code):
        ch = code[i]

        if not ch.isspace(
        ):  # Only show relevant commands and their stack states
            clear_screen()
            print(f'Command: {ch}')
            print(f'Stack: {st}')
            print('Output:')
            print(dbgout.getvalue())
            input("Press Enter to continue..."
                  )  # Wait for user input before proceeding

        match ch:
            case '!':
                st.append(operation(lambda x: int(not_(x)), *stack_pop()))
            case '%':
                st.append(operation(mod, *stack_pop(2)))
            case '&':
                st.append(operation(and_, *stack_pop(2)))
            case '(':
                pass
            case ')' | 'c':
                loop_continue()
            case '*':
                st.append(operation(mul, *stack_pop(2)))
            case '+':
                st.append(operation(add, *stack_pop(2)))
            case '-':
                st.append(operation(sub, *stack_pop(2)))
            case '/':
                st.append(
                    operation(lambda a, b: a * (Fraction(1) / b),
                              *stack_pop(2)))
            case _ if ch.isdigit():
                st.append(int(ch))
            case '<':
                st.append(operation(lambda x, y: int(x < y), *stack_pop(2)))
            case '=':
                st.append(operation(lambda x, y: int(x == y), *stack_pop(2)))
            case '>':
                st.append(operation(lambda x, y: int(x > y), *stack_pop(2)))
            case 'C':
                st.append(operation(ceil, *stack_pop()))
            case 'D':
                st.append(operation(lambda x: x.denominator, *stack_pop()))
            case 'F':
                st.append(operation(factorial, *stack_pop()))
            case 'I':
                st.append(operation(int, *stack_pop()))
            case 'N':
                st.append(operation(lambda x: x.numerator, *stack_pop()))
            case 'R':
                st.append(operation(round, *stack_pop()))
            case 'S':
                st.append(operation(str, *stack_pop()))
            case 'T':
                st.append(operation(trunc, *stack_pop()))
            case '[':
                if not_(*stack_pop()):
                    if_skip()
            case ']':
                pass
            case '^':
                st.append(operation(xor, *stack_pop(2)))
            case '`':
                st.append(operation(chr, *stack_pop()))
            case 'b':
                loop_break()
            case 'd':
                st.extend(chain.from_iterable(tee(stack_pop())))
            case 'g':
                x = ~next(stack_pop())
                try:
                    st[-1], st[x] = st[x], st[-1]
                except:
                    raise_exception('Invalid Index')
            case 'i':
                c = stdin.read(1)
                st.append(ord(c) if c else -1)
            case 'o':
                operation(print,
                          *stack_pop(),
                          end='',
                          file=dbgout if args.debug else stdout)
            case 'p':
                next(stack_pop())
            case 's':
                st.extend(tuple(stack_pop(2)))
            case 't':
                exit(0)
            case 'x':
                try:
                    st.append(st[~next(stack_pop())])
                except:
                    raise_exception('Invalid Index')
            case '|':
                st.append(operation(or_, *stack_pop(2)))
            case '~':
                st.append(operation(inv, *stack_pop()))
            case _ if ch.isspace():
                pass
            case _:
                raise_exception(f'Invalid command {repr(ch)}')

        i += 1

dbgout.close()
