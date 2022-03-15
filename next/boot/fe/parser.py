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
from .decs import hard_builtins

class Parser:
    def __init__(self, tokens: List[Token]):
        self.current_token = -1
        self.last_token: Token = None
        self.next_token: Token = None
        self.tokens = tokens

    def _parse_next_token(self):
        self.current_token += 1
        token = self.tokens[self.current_token]
        self.next_token = self.tokens[self.current_token + 1]

        if token.type in hard_builtins:
            if token.type == 'METHOD':
                if self.last_token.type != 'METHOD':
                    if self.next_token.type != 'METHOD':
                        raise RuntimeError()
                    else:
                        ...
                elif self.last_token.type == 'METHOD':
                    if self.next_token.type == 'METHOD':
                        # TODO: Builtin erroring.
                        raise RuntimeError()

