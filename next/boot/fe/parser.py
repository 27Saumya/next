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
from .ast import Print, Integer
from .lexer import listed
from ..be import Configurator

class Parser:
    def __init__(self, ir: Configurator):
        self._parser = rply.ParserGenerator(listed)
        self.ir = ir

    def start(self):
        @self._parser.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def print_(p):
            return Print(self.ir, p[2])
        @self._parser.production('expression : INTEGER')
        def integer(p):
            return Integer(self.ir, p[0].value)

    def build(self):
        return self._parser.build()
