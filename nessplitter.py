import os
import sys
if len(sys.argv) != 2:
    raise Exception("Too many or too little arguments!")
file = sys.argv[1]
update = open("update.bat", "w")
update.write('nesgodisasm.exe -a nesasm "' + file + '"')
update.close()
os.system("update.bat")
os.system("del update.bat")
filename = file.replace(".nes", ".asm")
fileread = open(filename, "r")
flag = False
chrrom = []
lines = []
if os.path.getsize(file) != 40976 and os.path.getsize(filename) != 671538:
    raise Exception("The file size must be 40976 bytes!")
while True:
    line = fileread.readline()
    if ".bank 4" in line:
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
asmfile = open(filename, "w")
linesWritten = 0
for line in range(len(lines)):
    if linesWritten == 0:
        asmfile.write(lines[line])
    else:
        asmfile.write("\n" + lines[line])
asmfile.write(' .incbin "' + chrfilename + '"')