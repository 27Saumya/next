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
from llvmlite import ir
from ..be import ir_core

class Print:
    def __init__(self, ir_core: ir_core.Configurator, value):
        self.ir = ir_core
        self.value = value

    def eval(self):
        val = self.value.eval()

        voidptr_type = ir.IntType(8).as_pointer()
        fmt = '%i \n\0'
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)), bytearray(fmt.encode('utf8')))
        global_fmt = ir.GlobalVariable(self.ir.module, c_fmt.type, 'fstr')
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.ir.builder.bitcast(global_fmt, voidptr_type)

        self.ir.builder.call(self.ir._funcs.print, [fmt_arg, val])

class Integer:
    def __init__(self, ir_core: ir_core.Configurator, value: str):
        self.ir = ir_core
        self.value = value
    
    def eval(self):
        return ir.Constant(ir.IntType(len(self.value)), int(self.value))
