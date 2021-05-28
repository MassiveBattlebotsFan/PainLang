import sys
if len(sys.argv) < 2:
    exit("Syntax: PLcompiler.py <program.ow>")
#tape = [0,0,0,0,0,0,0,0]
#index = 0
cmds = {"o" : "index = (0 if index + 1 > 8 else index + 1); ", "w" : "tape[index] = (0 if tape[index] + 1 > 0b11111111 else tape[index] + 1); ", "!" : "sys.stdout.write(chr(tape[index])); ", "?" : "tape[index] = ord(sys.stdin.read(1)); ", "O" : "\nwhile True: \n    ", "W" : "\n    if tape[index] == 0: break; ", "A" : "index = 0; ", "a" : "tape[index] = 0; "}
prog = ""
with open(sys.argv[1], "r") as file:
    data = file.read()
    for char in data:
        if char in cmds.keys():
            prog += cmds.get(char)
with open(sys.argv[1].split(".")[0]+".py", "w") as file:
    file.write("import sys\ntape = [0,0,0,0,0,0,0,0]; index = 0; "+prog)
print("script compiled")
#exec(prog)