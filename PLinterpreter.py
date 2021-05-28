import sys

dbg = False
if "-d" in sys.argv[1:]: dbg=True;print("Debug mode active")
tape = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
index = 0
neg = 1
cmds = {"o" : f"index = ((0 if index + 1 > 15 else index + 1) if neg == 1 else (15 if index - 1 < 0 else index - 1)); ", "w" : "tape[index] = ((0 if tape[index] + 1 > 0b11111111 else tape[index] + 1) if neg == 1 else (0b11111111 if tape[index] - 1 < 0b00000000 else tape[index] - 1)); ", "!" : "sys.stdout.write(chr(tape[index])); ", "?" : "tape[index] = ord(sys.stdin.read(1)); ", "O" : "\nif tape[index] != 0:\n    while True: \n        ", "W" : "\n        if tape[index] == 0: break; \n", "a" : "neg *= -1; "}
def interpret(data):
    prog = ""
    for char in data:
        if char=="A":break
        if dbg and char=="#":prog+="sys.stdout.write(str(tape)+\",\"+str(index)+\",\"+str(neg)+\"\\n\"); "
        if char in cmds.keys():prog += cmds.get(char)
    return prog

while True:
    print("\nReady")
    ipt = input("PainLang> ")
    if ipt == "exit":
        break
    if ipt == "reset":
        tape = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        index = 0
        neg = 1
        print("State reset")
    exec(interpret(ipt))