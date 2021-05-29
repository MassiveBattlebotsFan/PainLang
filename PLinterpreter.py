import sys,os

dbg = False
if "-d" in sys.argv[1:]: dbg=True;print("Debug mode active")
tape = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
index = 0
neg = 1
cmds = {"o" : "index=index+(1*neg); if index<0 then index=tape:len() elseif index>tape:len() then index=0 end; " , "w" : "tape[index]=tape[index]+(1*neg); if tape[index]<0 then tape[index]=255 elseif tape[index]>255 then tape[index]=0 end; ", "!" : "io.write(string.byte(tape[index])); ", "?" : "tape[index] = string.char(io.read(1)); ", "O" : "while tape[index]>0 do", "W" : "end", "a" : "neg=neg*-1; "}
def interpret(data):
    prog = ""
    for char in data:
        if char=="A":break
        if dbg and char=="#":prog+="io.write(tape[0,tape:len()]..\",\"..index..\",\"..neg..\"\\n\"); "
        if char in cmds.keys():prog += cmds.get(char)
    return "tape={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};index=0;neg=1;"+prog

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
    os.system(f"lua54.exe -W -i -e \"{interpret(ipt)}\"")