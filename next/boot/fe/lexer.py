# Copyright 2022 VincentRPS
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import rply

lexer = rply.LexerGenerator()

NUMS = '1234567890'
STRINGS = 'abcdefghijklmnopqrstuvwxyz'
STRINGS_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# hard builtins
lexer.add('PLUS', r'\+')
lexer.add('MINUS', r'-')
lexer.add('IF', r'if')
lexer.add('METHOD', r'::')
lexer.add('OPEN_PAREN', r'\(')
lexer.add('CLOSE_PAREN', '\)')
lexer.add('OPEN_FN', '{')
lexer.add('CLOSE_FN', '}')
lexer.add('DEF_FN', 'def')
lexer.add('STRING_STATEMENT', "'")
lexer.add('STRING_STATEMENT', '"')
lexer.add('IGNORE', '//')
lexer.add('SPACE', ' ')
lexer.add('EQ', '=')
lexer.add('EQEQ', '==')
lexer.add('STARTER', ':')
lexer.add('METRO', 'metro')
lexer.add('INDENT', r'\n')

# soft builtins
lexer.add('PRINT', 'print')

# constants
for num in NUMS:
    lexer.add('INTEGER', num)

for string in STRINGS:
    lexer.add('STRING', string)

for string in STRINGS_:
    lexer.add('STRING', string)

# ignore
lexer.ignore(r'\n')
lexer.ignore(r'\s+')

listed = [
    'STRING',
    'SPACE',
    'IGNORE',
    'EQ',
    'EQEQ',
    'STARTER',
    'METRO',
    'STRING_STATEMENT',
    'DEF_FN',
    'OPEN_FN',
    'CLOSE_FN',
    'METHOD',
    'IF',
    'PLUS',
    'MINUS',
    'PRINT',
    'INTEGER',
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'OPEN_FN',
    'CLOSE_FN',
    'INDENT'
]
