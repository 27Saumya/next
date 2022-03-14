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
from typing import List
from .token import Token
from .decs import nums

STRINGS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
strings = 'abcdefghijklmnopqrstuvwxyz'

class Lexer:
    def __init__(self, f: str):
        self.line_num = -1
        self._lines = f.split(' ')
        self.lines = self._lines
        self.tokens: List[Token] = []
        self.last_letter = ''

    def run(self):
        self.scroll_up()

    def _parse_method(self):
        next_line = self.lines[self.line_num + 1]
        if next_line != ':':
            raise RuntimeError(f'Syntax Mispell at line {self.line_num}')
        else:
            return 'METHOD', next_line[-1]

    def _parse_comment(self):
        next_line = self.lines[self.line_num + 1]
        if next_line != '/':
            raise RuntimeError(f'Syntax Mispell at line {self.line_num}')
        else:
            return True
    
    def scroll_up(self) -> None:
        self.line_num += 1

        try:
            _line = self.lines[self.line_num]
        except IndexError:
            # we have reached the end
            return
        letters = _line

        cur_letter = 0

        cur_letter += 1

        token = None
        value = None

        # NOTE: This is only for builtin functions, and is not finished.
        for letter in letters:
            if letter == ':':
                token = 'METHOD'
                value = None

            elif letter == '/':
                skip = self._parse_comment()
                if skip == True:
                    self.scroll_up()
                    return

            elif letter in ' \t':
                self.scroll_up()
                return

            elif letter in nums.split(' '):
                token = 'INTEGER'
                value = int(letter)
            
            elif letter == '.' and self.last_letter in nums.split(' '):
                token = 'FLOAT'
                value = float(letter)
            
            elif letter == '!':
                token = 'MACRO'
                value = self.lines[self.line_num + 1]
            
            elif letter == '\n':
                self.scroll_up()
                return
            
            elif letter == '=':
                token = 'EQ'
                value = None
            
            elif letter == '==':
                token = 'EQEQ'
                value = None
            
            elif letter == '\'' or letter == '"':
                token = 'QUOTE'
                value = None

            elif letter in strings or letter in STRINGS:
                token = 'STRING'
                value = letter

            else:
                raise NotImplementedError(f'Invalid Syntax: {letter} is an illegal character')

            self.tokens.append(Token(token, value))
            self.last_letter = letter
