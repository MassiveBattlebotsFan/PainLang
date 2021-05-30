l = 16
tape = {}
index = 0;
neg = 1
local dbg = false
local full_dbg = false
local cmds = {["o"] = "index = index+neg; if index<0 then index=#tape-1 end; if index>#tape-1 then index=0 end; " , ["w"] = "tape[index] = tape[index]+neg; if tape[index]<0 then tape[index]=255 end; if tape[index]>255 then tape[index]=0 end; ", ["!"] = "io.write(string.char(tape[index])); ", ["?"] = "tape[index] = string.byte(io.read(1)); ", ["O"] = "if tape[index]>0 then while true do ", ["W"] = " if tape[index] == 0 then break end end end ", ["a"] = "neg=neg*-1; "};
for i = 0,#arg do
    if arg[i] == "-d" then dbg=true;io.write("Debug mode active\n") end
    if arg[i] == "-l" then l=tonumber(arg[i+1]) end
    if arg[i] == "-fd" then full_dbg=true;dbg=true;io.write("Full debug mode active\n") end
end
for i = 0,l-1 do tape[i] = 0 end
local function interpret(data)
    local prog = ""
    for i = 1,#data do
        local char = data:sub(i,i)
        if char == "A" then break end
        if char == "#" and dbg then prog = prog.."io.write(\"[\"..tape[0]); for i = 1,#tape-1 do io.write(\",\"..tape[i]) end; io.write(\"],\"..index..\",\"..neg)" end
        --if dbg and char=="#" then prog = prog + "io.write(tape[0,tape:len()]..\",\"..index..\",\"..neg..\"\\n\"); " end
        for op,cmd in pairs(cmds) do
            if char == op then prog = prog..cmd end
        end
    end
    --print(prog)
    return prog
end
while true do
    io.write("\nReady\n")
    io.write("PainLang> ")
    local ipt = io.read()
    if ipt == "reset" then 
        for i = 0,15 do tape[i] = 0 end
        neg = 1
        index = 0
        io.write("State reset\n")
    end
    if ipt == "exit" then
        break
    end
    --print(interpret(ipt))
    if full_dbg then print(load(interpret(ipt))) end
    local f = load(interpret(ipt));f()
end