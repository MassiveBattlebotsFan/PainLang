import sys
if len(sys.argv) < 2:
    exit("Syntax: PLcompiler.py [-d] [-l <tape length>] <program.pain>")
#tape = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#index = 0
#neg = 1
prog = "";dbg = False;lnt = None
if "-d" in sys.argv[1:]: dbg=True
try: 
    if "-l" in sys.argv[1:]: lnt=int(sys.argv[sys.argv.index("-l")+1])
except:exit("-l option requires a length integer")
cmds = {"o" : "index = index+neg; if index<0 then index=#tape-1 end; if index>#tape-1 then index=0 end; ", "w" : "tape[index] = tape[index]+neg; if tape[index]<0 then tape[index]=255 end; if tape[index]>255 then tape[index]=0 end; ", "!" : "io.write(string.char(tape[index])); ", "?" : "tape[index] = string.byte(io.read(1)); ", "O" : "if tape[index]>0 then while true do ", "W" : " if tape[index] == 0 then break end end end ", "a" : "neg=neg*-1; "}
with open(sys.argv[-1], "r") as file:
    lines = file.readlines()
    for data in lines:
        for char in data:
            if char=="A":break
            if dbg and char=="#":prog+="io.write(\"[\"..tape[0]); for i = 1,#tape-1 do io.write(\",\"..tape[i]) end; io.write(\"],\"..index..\",\"..neg)";print("dbg info written")
            if char in cmds.keys():prog += cmds.get(char)
with open(sys.argv[-1].split(".")[0]+".lua", "w") as file:lnt = ("16" if lnt==None else str(lnt));file.write("local tape={}; local index=0; local neg=1; "+f"for i = 0,{lnt} do tape[i] = 0 end; "+prog);print("script compiled")