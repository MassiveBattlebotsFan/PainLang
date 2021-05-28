# PainLang, an esoteric programming language  
A programming language whose commands are based off of the words "ow?", "OW!", and "AAAAAAAAAAAAAAAAA"  
Loosely based off of Brainfuck, file extension is `.pain`.
# Standard  
Given an index `i` and an eight cell tape `t`, with each cell being one byte:  
`o` sets `i` to `(i + 1) % 8`  
`w` increments `t[i]`, and wraps to zero upon exceeding one byte  
`!` prints `t[i]`  
`?` reads one character from the console into `t[i]`  
`O` jumps to the matching `W` character if `t[i]` is zero  
`W` jumps to the matching `O` character if `t[i]` is nonzero  
`a` sets `t[i]` to zero  
`A` sets `i` to zero
Please don't nest loops
