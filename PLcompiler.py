import sys
if len(sys.argv) < 2:
    exit("Syntax: PLcompiler.py <program.ow> [-d]")
#tape = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#index = 0
#neg = 1
cmds = {"o" : "index = ((0 if index + 1 > 15 else index + 1) if neg == 1 else (15 if index - 1 < 0 else index - 1)); ", "w" : "tape[index] = ((0 if tape[index] + 1 > 0b11111111 else tape[index] + 1) if neg == 1 else (0b11111111 if tape[index] - 1 < 0b00000000 else tape[index] - 1)); ", "!" : "sys.stdout.write(chr(tape[index])); ", "?" : "tape[index] = ord(sys.stdin.read(1)); ", "O" : "\nif tape[index] != 0:\n    while True: \n        ", "W" : "\n        if tape[index] == 0: break; \n", "A" : "neg = 1; ", "a" : "neg = -1; "}
prog = ""
with open(sys.argv[1], "r") as file:
    data = file.read()
    for char in data:
        if char in cmds.keys():
            prog += cmds.get(char)+("sys.stdout.write(str(tape)+\",\"+str(index)+\",\"+str(neg)); " if len(sys.argv)>2 and sys.argv[2]=="-d" else "")
with open(sys.argv[1].split(".")[0]+".py", "w") as file:
    file.write("import sys\ntape = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]; index = 0; neg = 1; "+prog)
print("script compiled")