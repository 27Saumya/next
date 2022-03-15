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
import sys
from typing import Any

class Token:
    def __init__(self, type: str, value: Any = None):
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        return f'{self.type!r}:{self.value!r}'

    def _raise_error(self, msg: str, type: str):
        sys.stderr.write(f'{type}: {msg}')
