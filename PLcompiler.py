import sys
if len(sys.argv) < 2:
    exit("Syntax: PLcompiler.py <program.pain> [-d]")
#tape = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#index = 0
#neg = 1
cmds = {"o" : "index = ((0 if index + 1 > 15 else index + 1) if neg == 1 else (15 if index - 1 < 0 else index - 1)); ", "w" : "tape[index] = ((0 if tape[index] + 1 > 0b11111111 else tape[index] + 1) if neg == 1 else (0b11111111 if tape[index] - 1 < 0b00000000 else tape[index] - 1)); ", "!" : "sys.stdout.write(chr(tape[index])); ", "?" : "tape[index] = ord(sys.stdin.read(1)); ", "O" : "\nif tape[index] != 0:\n    while True: \n        ", "W" : "\n        if tape[index] == 0: break; \n", "a" : "neg *= -1; "}
prog = ""
dbg = False
if len(sys.argv)>2 and sys.argv[2]=="-d": dbg=True
with open(sys.argv[1], "r") as file:
    lines = file.readlines()
    for data in lines:
        for char in data:
            if char=="A":
                break
            if dbg and char=="#":prog+="sys.stdout.write(str(tape)+\",\"+str(index)+\",\"+str(neg)+\"\\n\"); ";print("dbg info written")
            if char in cmds.keys():
                prog += cmds.get(char)
with open(sys.argv[1].split(".")[0]+".py", "w") as file:
    file.write("import sys\ntape = [0]*64; index = 0; neg = 1; "+prog)
print("script compiled")