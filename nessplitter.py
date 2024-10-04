import os
import sys
if len(sys.argv) != 2:
    raise Exception("Too many or too little arguments!")
file = sys.argv[1]
os.system('nesgodisasm.exe -a nesasm "' + file + '"')
filename = file.replace(".nes", ".asm")
fileread = open(filename, "r")
flag = False
chrrom = []
lines = []
banks = []
lineCount = 0
while True:
    line = fileread.readline()
    if not line:
        lineCount += 1
    else:
        lineCount = 0
    if ".bank" in line:
        banks.append(line)
    if lineCount > 2:
        break
fileread.close()
fileread = open(filename, "r")
while True:
    line = fileread.readline()
    if banks[len(banks) - 1] in line:
        flag = True
        lines.append(line)
        continue
    if flag == True:
        line = line.replace(" .byte $", "")
        line = line.split(", $")
        if len(line) == 1:
            break
        for bytes in range(len(line)):
            line[bytes] = line[bytes].replace("\\n", "")
            chrrom.append(int(line[bytes], 16))
    else:
        lines.append(line)
fileread.close()
chrfilename = filename.replace(".asm", ".chr")
chr = open(chrfilename, "wb")
chr.write(bytearray(chrrom))
chr.close()
asmfile = open(filename, "w")
linesWritten = 0
for line in range(len(lines)):
    if linesWritten == 0:
        asmfile.write(lines[line])
    else:
        asmfile.write("\n" + lines[line])
asmfile.write(' .incbin "' + chrfilename + '"')
asmfile.close()