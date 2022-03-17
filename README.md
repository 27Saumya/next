# This is the next programming language version 0.1

The language itself it a purely pythonic implementation.

## Building

There is currently no way to *properly* build.

## Compiling Code

first make your test file, i.e. `test.py`

and add the following:

```py
import next

config = next.Configurator()

lexed = """
print(1)
"""

built = next.lexer.build()

tokens = built.lex(lexed)

_parser = next.Parser(config)
_parser.start()
parser = _parser.build()
parser.parse(tokens).eval()

config.create_output('.cachedir/CACHE_MAIN.ll')
print('Done')
```

Replacing `print(1)` with whatever you want of course.

Once it's done, you will want to compile the LLVM IR code to a object file,
this can be done using `llc`.

Firstly, download llc, it's just a google search.

Then type the following `llc .cachedir/CACHE_MAIN.ll -filetype=obj -o main.o`.

it should then give you a `main.o` file, you will now want to compile this to a executable.

You can do this using any compiler you want, for this we will use `gcc`, 

like so: `gcc main.o -o main` 
and it should finally give you a `.exe`(or something else for unix-like systems) which you can run.
