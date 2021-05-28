# PainLang, an esoteric programming language  
A programming language whose commands are based off of the words "ow?", "OW!", and "AAAAAAAAAAAAAAAAA"  
Loosely based off of Brainfuck, file extension is `.pain`.
# Standard  
Given an index `i`, a negation bit `neg`, and a sixteen cell tape `t`, with each cell being one byte:  
`o` sets `i` to `(i + 1) % 8`  
`w` increments `t[i]`, and wraps to zero upon exceeding one byte  
`!` prints `t[i]`  
`?` reads one character from the console into `t[i]`  
`O` jumps to the matching `W` character if `t[i]` is zero  
`W` jumps to the matching `O` character if `t[i]` is nonzero  
`a` sets `neg` to -1  
`A` sets `neg` to 1  
Please don't nest loops
